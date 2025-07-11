import os
from winreg import QueryInfoKey
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
import psutil
import pyjokes
import wikipedia

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()

    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        
from INTRO import play_gif
play_gif
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    import pyttsx3

   
#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query or "bye bye jarvis" in query:
                    speak("Ok sir , You can  call me anytime")
                    break 
                elif "change password" in query:
                      speak("What's the new password")
                      new_pw = input("Enter the new password\n")
                      new_password = open("password.txt","w")
                      new_password.write(new_pw)
                      new_password.close()
                      speak("Done sir")
                      speak(f"Your new password is{new_pw}")
                
                
                elif "open" in query:   #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                         
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576      #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com//"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "what about you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                     from SearchNow import searchGoogle
                     searchGoogle(query)
                elif "youtube" in query:
                     from SearchNow import searchYoutube
                     searchYoutube(query)
                elif "pause" in query:
                      pyautogui.press("k")
                      speak("video paused")
                elif "play" in query:
                      pyautogui.press("k")
                      speak("video played")
                elif "mute" in query:
                      pyautogui.press("m")
                      speak("video muted")

                elif "volume up" in query:
                  from keyboard import volumeup
                  speak("Turning volume up,sir")
                  volumeup()
                elif "volume down" in query:
                  from keyboard import volumedown
                  speak("Turning volume down, sir")
                  volumedown()
                elif "wikipedia" in query:
                     from SearchNow import searchWikipedia
                     searchWikipedia(query)
                elif "news" in query:
                     from NewsRead import latestnews
                     latestnews()
                elif "temperature" in query:
                        search = "temperature in beed"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                        print(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in beed"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(f"current{search} is {temp}")
                #play songs
                elif ("songs" in query):
                    speak("Playing...")
                    songs_dir = "C:\Songs"
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir, songs[0]))
                    quit()

                elif "what's the time" in query:
                      strTime = datetime.datetime.now().strftime("%H:%M")    
                      speak(f"Sir, the time is {strTime}")

                elif " Bye Bye jarvis" in query:
                      speak("Going to sleep,sir")
                      exit()
                elif "remember that" in query:
                     rememberMessage = query.replace("remember that","")
                     rememberMessage = query.replace("jarvis","")
                     speak("You told me to remember that"+rememberMessage)
                     remember = open("Remember.txt","a")
                     remember.write(rememberMessage)
                     remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                elif "Getting bored" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                       webbrowser.open("https://www.youtube.com/watch?v=bUDIm1SstAE&list=PLldRXoeaXPNm2wL1iy2fBMc55c1T8ZLhp")
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

               
                 #searching on wikipedia
                elif ('wikipedia' in query or 'what' in query or 'who' in query
                    or 'when' in query or 'where' in query):
                    speak("searching...")
                    query = query.replace("wikipedia", "")
                    query = query.replace("search", "")
                    query = query.replace("what", "")
                    query = query.replace("when", "")
                    query = query.replace("where", "")
                    query = query.replace("who", "")
                    query = query.replace("is", "")
                    result = wikipedia.summary(query, sentences=2)
                    print(query)
                    print(result)
                    speak(result)

                #cpu and battery usage
                elif ("cpu and battery" in query or "battery" in query
                    or "cpu" in query):
                    cpu()

                #jokes
                elif ("tell me a joke" in query or "joke" in query):
                    jokes()

                #time
                elif ('time' in query):
                    time()

                #date
                elif ('date' in query):
                    date()

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "focus mode" in query:
                                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                                    if (a==1):
                                        speak("Entering the focus mode....")
                                        os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                                        exit()

                                    
                                    else:
                                        pass
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "send message" in query:
                     from Whatsapp import sendMessage
                     sendMessage()

                #jarvis features
                elif ("tell me your powers" in query or "help" in query
                    or "features" in query):
                    features = ''' i can help to do lot many things like..
                    i can set alarm for you,
                    i can open any application in your system,
                    i can tell your internet and wifi speed,
                    i can tell you news,
                    i can tell you current temperature,
                    i can calculate any value,
                    i can send whatsapp messages, 
                    i can play songs,
                    i can tell you the current time and date,
                    i can tell you battery and cpu usage,
                    i can create the reminder list,
                    i can tell you non funny jokes,
                    i can open any website,
                    i can search the thing on wikipedia,
                    i can make your assistant secure by providing password,
                    i can shut down or restart your system,
                    And yes one more thing, My boss is working on this system to add more features...,
                    tell me what can i do for you??
                    '''
                    print(features)
                    speak(features)

                #sysytem logout/ shut down etc
                elif ("logout" in query):
                    os.system("logout -1")
                elif ("restart" in query):
                    os.system("restart /r /t 1")
                elif ("shutdown" in query):
                    os.system("shutdown /s /t 1")

