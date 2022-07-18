using UnityEngine;
using UnityEngine.UI; //Библиотека для работы с пользовательским интерфейсом
using UnityEngine.SceneManagement;


public class CanvasButtons : MonoBehaviour
{
    //Картинки при включении отключении звука
    public Sprite musicOn, musicOff;

    public void Start()
    {   //Картинка звука при старет
        if(PlayerPrefs.GetString("music") == "No" && gameObject.name == "Music")
        {   
            GetComponent<Image>().sprite = musicOff;
        }
    }

    public void RestartGame()
    {
        //Звук для кнопки
        if (PlayerPrefs.GetString("music") != "No")
            GetComponent<AudioSource>().Play();
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }


    //Функция перехода в инстаграмм
    public void LoadInstagram()
    {
        //Звук для кнопки
        if (PlayerPrefs.GetString("music") != "No")
            GetComponent<AudioSource>().Play();
        Application.OpenURL("https://www.instagram.com/");
    }

    //Метод открытия магазина в игре
    public void LoadShop()
    {
        //Звук для кнопки
        if (PlayerPrefs.GetString("music") != "No")
            GetComponent<AudioSource>().Play();
        SceneManager.LoadScene("Shop");
    }

    //Метод закрытия магазина в игре
    public void CloseShop()
    {
        //Звук для кнопки
        if (PlayerPrefs.GetString("music") != "No")
            GetComponent<AudioSource>().Play();
        SceneManager.LoadScene("Main");
    }

    //Функция работы звука
    public void MusicWork()
    {
        //Сейчас музыка выключена и её нужно включить
        if(PlayerPrefs.GetString("music") == "No")
        {
            GetComponent<AudioSource>().Play();
            PlayerPrefs.SetString("music", "Yes");
            //Меняем картинку звука 
            GetComponent<Image>().sprite = musicOn;
        }
        //Сейчас музыка включена и её нужно выключить
        else
        {
            PlayerPrefs.SetString("music", "No");
            GetComponent<Image>().sprite = musicOff;
        }

    }
}
