using UnityEngine;

public class IsEnabled : MonoBehaviour
{
    //Переменная хранит рекорд после которой новый кубик будет открыт
    public int needToUnlock;
    //Переменная хранит материал
    public Material blackMaterial;

    private void Start()
    {
        //Проверка на очки для открытия кубика
        if(PlayerPrefs.GetInt("score") < needToUnlock)
        {
            GetComponent<MeshRenderer>().material = blackMaterial;
        }
    }
}
