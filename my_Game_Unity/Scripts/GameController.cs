using UnityEngine;
using UnityEngine.UI; // помогает работать с пользовательским интерфейсом
using System; //Cтандартная библиотека позволяющая работать с классом Convert
using System.Collections; //Позволит запускать различные куратины
using System.Collections.Generic; //Позволяет использовать класс List
using UnityEngine.EventSystems;

public class GameController : MonoBehaviour
{
    //Создаем объект на основе структуры CubePos
    //nowCube - кубик расположенный в игре последним за начало берутся координаты 1-го кубика (Maincube)
    private CubePos nowCube = new CubePos(0, 1, 0);
    //Скорость кубика который меняет позициию и показывает где установить новый куб
    public float cubeChangePlaceSpeed = 0.5f;
    //Ссылка неа объект CubeToPlace
    public Transform cubeToPlace;
    private float camMoveToYPositions, camMoveSpeed = 2f;

    //Публичная переменная для передачи очков при наборе (ссылка для переноса на объект)
    public Text scoreTxt;

    //Разнацветные кубики
    public GameObject[] cubesToCreate;

    public GameObject allCubes, vfx;
    public GameObject[] canvasStartPage;
    private Rigidbody allCubesRb;

    //Масив с цветами фона
    public Color[] bgColors;
    private Color toCameraColor;

    private bool isLose, firstCube;

    //Динамический массив который хранит координат мест на которые кубик поставить нельзя
    private List<Vector3> allCubesPossitions = new List<Vector3>
    {
        new Vector3 (0, 0, 0), 
        new Vector3 (1, 0, 0),
        new Vector3 (-1, 0, 0), 
        new Vector3 (0, 1, 0),
        new Vector3 (0, 0, 1),
        new Vector3 (0, 0, -1),
        new Vector3 (1, 0, 1),
        new Vector3 (-1, 0, -1),
        new Vector3 (-1, 0, 1),
        new Vector3 (1, 0, -1)
    };

    // Переменная хранящая максимальное значение координаты по горизонитали
    private int prevCountMaxHorizontal;
    private Transform mainCam;
    private Coroutine showCubePlace;
    //Массив хранит открытые кубики
    private List<GameObject> posibleCubesToCreate = new List<GameObject>();



    private void Start()
    {   //Удаляет рекорд
        //PlayerPrefs.SetInt("score", 0);

        //Вызываем метод AddPossibleCubes который перебирает массив с открытыми за рекорд кубиками
        if (PlayerPrefs.GetInt("score") < 5)
            posibleCubesToCreate.Add(cubesToCreate[0]);
        else if (PlayerPrefs.GetInt("score") < 10)
            AddPossibleCubes(2);
        else if (PlayerPrefs.GetInt("score") < 20)
            AddPossibleCubes(3);
        else if (PlayerPrefs.GetInt("score") < 30)
            AddPossibleCubes(4);
        else if (PlayerPrefs.GetInt("score") < 40)
            AddPossibleCubes(5);
        else if (PlayerPrefs.GetInt("score") < 60)
            AddPossibleCubes(6);
        else if (PlayerPrefs.GetInt("score") < 75)
            AddPossibleCubes(7);
        else if (PlayerPrefs.GetInt("score") < 90)
            AddPossibleCubes(8);
        else if (PlayerPrefs.GetInt("score") < 100)
            AddPossibleCubes(9);
        else
            AddPossibleCubes(10);

        // Первоначальные значения для очков игры
        scoreTxt.text = "<size=40><color=\"#B24947\"> BEST:</color></size>" + PlayerPrefs.GetInt("score") + "\n <size=35> nov:</size> 0";

        //Первоначальный цвет
        toCameraColor = Camera.main.backgroundColor;

        //Движение камеры по координате Y
        mainCam = Camera.main.transform;
        camMoveToYPositions = 5.9f + nowCube.y - 1f;

        allCubesRb = allCubes.GetComponent<Rigidbody>();

        //Переменная которая запускает куратину поиска кубов
        showCubePlace = StartCoroutine(ShowCubePlace());
    }

    void Update()
    {
        //Управление в игре
        if ((Input.GetMouseButtonDown(0) || Input.touchCount > 0) && cubeToPlace != null && allCubes != null && !EventSystem.current.IsPointerOverGameObject())
        {
            //Управление не в Unity
#if !UNITY_EDITOR
             if (Input.GetTouch(0).phase != TouchPhase.Began ||
             EventSystem.current.IsPointerOverGameObject(Input.GetTouch(0).fingerId))
                return;
#endif

            if (!firstCube)
            {
                firstCube = true;
                foreach(GameObject obj in canvasStartPage)
                {
                    Destroy(obj);
                }
            }


            //Если все кубы кроме первого закрыты
            GameObject createCube = null;
            if (posibleCubesToCreate.Count == 1)
                createCube = posibleCubesToCreate[0];
            else
                createCube = posibleCubesToCreate[UnityEngine.Random.Range(0, posibleCubesToCreate.Count)];


            //Создаем оъекты из createCube
            GameObject newCube = Instantiate(
            createCube,
            cubeToPlace.position,
            Quaternion.identity) as GameObject;

            newCube.transform.SetParent(allCubes.transform);
            nowCube.setVector(cubeToPlace.position);
            allCubesPossitions.Add(nowCube.getVector());

            //Звук  при установке кубика
            if (PlayerPrefs.GetString("music") != "No")
                GetComponent<AudioSource>().Play();

            //Эфект при установке кубика
            GameObject newVfx = Instantiate(vfx, cubeToPlace.position, Quaternion.identity) as GameObject;
            //Удаление эфекта после создания через полторы секунды
            Destroy(newVfx, 1.5f);

            allCubesRb.isKinematic = true;
            allCubesRb.isKinematic = false;

            SpawnPositions();
            //Вызываем функцию движения камеры
            MoveCameraBg();

        }

        // Проигрыш
        if (!isLose && allCubesRb.velocity.magnitude > 0.1f)
        {
            Destroy(cubeToPlace.gameObject);
            isLose = true;
            StopCoroutine(showCubePlace);
        }

        //Плавность движения камеры по оси Y (вверх и вниз)
        mainCam.localPosition = Vector3.MoveTowards(mainCam.localPosition, new Vector3(mainCam.localPosition.x, camMoveToYPositions, mainCam.localPosition.z), camMoveSpeed * Time.deltaTime);

        //Плавность изменения цветов фонов
        if (Camera.main.backgroundColor != toCameraColor)
            Camera.main.backgroundColor = Color.Lerp(Camera.main.backgroundColor, toCameraColor, Time.deltaTime / 1.5f);

    }

    //Куратина которая меняет позициию для установки куба бесконечно
    IEnumerator ShowCubePlace()
    {
        while (true)
        {
            SpawnPositions();

            // yeield позволяет запускать куратину в определенные промежутки времени
            yield return new WaitForSeconds(cubeChangePlaceSpeed);
        }
    }

    //Проверяем места и добавляем кубики 
    private void SpawnPositions()
    {
        List<Vector3> positions = new List<Vector3>();
        if (isPositionEmpty(new Vector3(nowCube.x + 1, nowCube.y, nowCube.z))
        && nowCube.x + 1 != cubeToPlace.position.x)
            positions.Add(new Vector3(nowCube.x + 1, nowCube.y, nowCube.z));
        if (isPositionEmpty(new Vector3(nowCube.x - 1, nowCube.y, nowCube.z))
        && nowCube.x - 1 != cubeToPlace.position.x)
            positions.Add(new Vector3(nowCube.x - 1, nowCube.y, nowCube.z));
        if (isPositionEmpty(new Vector3(nowCube.x, nowCube.y + 1, nowCube.z))
        && nowCube.y + 1 != cubeToPlace.position.y)
            positions.Add(new Vector3(nowCube.x, nowCube.y + 1, nowCube.z));
        if (isPositionEmpty(new Vector3(nowCube.x, nowCube.y - 1, nowCube.z))
        && nowCube.y - 1 != cubeToPlace.position.y)
            positions.Add(new Vector3(nowCube.x, nowCube.y - 1, nowCube.z));
        if (isPositionEmpty(new Vector3(nowCube.x, nowCube.y, nowCube.z + 1))
        && nowCube.z + 1 != cubeToPlace.position.z)
            positions.Add(new Vector3(nowCube.x, nowCube.y, nowCube.z + 1));
        if (isPositionEmpty(new Vector3(nowCube.x, nowCube.y, nowCube.z - 1))
        && nowCube.z - 1 != cubeToPlace.position.z)
            positions.Add(new Vector3(nowCube.x, nowCube.y, nowCube.z - 1));

        if (positions.Count > 1)
            cubeToPlace.position = positions[UnityEngine.Random.Range(0, positions.Count)];
        else if (positions.Count == 0)
            isLose = true;
        else
            cubeToPlace.position = positions[0];
    }

    //Функция которая возвращает свободное ли место для кубика
    private bool isPositionEmpty(Vector3 targetPos)
    {
        if (targetPos.y == 0)
            return false;

        foreach (Vector3 pos in allCubesPossitions)
        {
            if (pos.x == targetPos.x && pos.y == targetPos.y && pos.z == targetPos.z)
                return false;
        }
        return true;
    }

    //Движение камеры (данная функция позволяет получить максимальный элемент по 3-м координатам
    private void MoveCameraBg()
    {
        int maxX = 0, maxY = 0, maxZ = 0, maxHor;
        foreach (Vector3 posi in allCubesPossitions)
        {
            if (Mathf.Abs(Convert.ToInt32(posi.x)) > maxX)
                maxX = Convert.ToInt32(posi.x);

            if (Mathf.Abs(Convert.ToInt32(posi.y)) > maxY)
                maxY = Convert.ToInt32(posi.y);

            if (Mathf.Abs(Convert.ToInt32(posi.z)) > maxZ)
                maxZ = Convert.ToInt32(posi.z);
        }

        //Счетчик для правильного вывода очков 
        maxY--;
        //Счет в игре
        if (PlayerPrefs.GetInt("score") < maxY)
            PlayerPrefs.SetInt("score", maxY);
       
         //Набор очков в игре 
        scoreTxt.text = "<size=40><color=\"#B24947\"> BEST:</color></size>" + PlayerPrefs.GetInt("score") + "\n <size=35> nov:</size>" + maxY;


        camMoveToYPositions = 5.9f + nowCube.y - 1f;

        //Тернарная операция отодвегает камеру горизонтально
        maxHor = maxX > maxZ ? maxX : maxZ;

        if(maxHor % 3 == 0 && prevCountMaxHorizontal != maxHor)
        {
            mainCam.localPosition -= new Vector3(0, 0, 2.5f);
            prevCountMaxHorizontal = maxHor;
        }

        //Меняем фон игры при добавлении кубиков по оси Y
        if (maxY >= 28)
            toCameraColor = bgColors[0];
        else if (maxY >= 21)
            toCameraColor = bgColors[2];
        else if (maxY >= 14)
            toCameraColor = bgColors[1];
        else if (maxY >= 7)
            toCameraColor = bgColors[0];
    }

    //Функция перебирает масив открывшихся кубиков
    private void AddPossibleCubes( int till)
    {
        for (int i = 0; i < till; i++)
        {
            posibleCubesToCreate.Add(cubesToCreate[i]);
        }
    }

    //Структура создания объектов
    struct CubePos
    {
        public int x, y, z;

        public CubePos(int x, int y, int z)
        {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public Vector3 getVector()
        {
            return new Vector3(x, y, z);
        }

        public void setVector(Vector3 pos)
        {
            x = Convert.ToInt32(pos.x);
            y = Convert.ToInt32(pos.y);
            z = Convert.ToInt32(pos.z);
        }
    }
}
