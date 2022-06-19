import requests


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)


if __name__ == '__main__':

    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=98a00a1c7e754a6a97e74b200d7c3e94')
    response = requests.get(url)
    # print(response.json())
    results = response.json()
    news = results['articles']
    print("Todays news")
    speak("Todays news")
    for i in range(1, 11):

        print("Source : ")
        speak("Source")
        print(news[i]['source']['name'])
        speak(str(news[i]['source']['name']))

        print("Title : ")
        speak("Title")
        print(news[i]['title'])
        speak(str(news[i]['title']))

        print("Description : ")
        speak("Description")
        print(news[i]['description'], '\n')
        speak(str(news[i]['description']))

        if i < 9:
            print("Moving to our next news\n")
            speak("Moving to our next news")
        elif i == 9:
            print("Moving to our last news\n")
            speak("Moving to our last news")
