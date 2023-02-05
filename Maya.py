import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import os
import pyjokes
from playsound import playsound
import datetime
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import speedtest_cli
from pywikihow import search_wikihow
import sys

#speak
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice',voices[0].id)
Assistant.setProperty('rate',195)

def Speak(audio):
    print("")
    Assistant.say(audio)
    print(f"Maya : {audio}.")
    print("")
    Assistant.runAndWait()

#Listen
def takecommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1   
        audio = command.listen(source,0,6)   #stock problem solve

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='en')
            print(f"You : {query}")

        except:
            return""

        query = str(query).lower()
        return(query)


def Pass(pass_inp):

    password = "b75 gamer"
    pas = str(password)


    if pas==str(pass_inp):
        playsound("C:\\Users\\B75GAMER\\Music\\assed.mp3")
        Speak("Access Granted !!")
        playsound("C:\\Users\\B75GAMER\\Music\\mixkit-sci-fi-confirmation-914.wav")
        import Maya

    else:
        playsound("C:\\Users\\B75GAMER\\Music\\accesed denied.mp3")
        Speak("Access not granted please try again!!")
        playsound("C:\\Users\B75GAMER\\Music\\alarm-furious-laboratory-cinematic-trailer-sound-effects-123873.mp3")
        Speak("Sorry sir, We detected unuthorized person try to access your system so we are closing this Beta Testing Maya 1.0 program.")
        os.system("TASKKILL /F /im code.exe")

if __name__ == "__main__" :
    Speak("Welcome back sir, i am Your voice assistant Maya 1.0 .")
    Speak("i was developed by B75 TEAM!")
    Speak("If you want to access me !")
    Speak("please give your voice command Password.")
    Passss = takecommand()
    #input(": Enter the password :")

    Pass(Passss)

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        Speak("Good Morning, Sir")
    elif hour>12 and hour<18:
        Speak("Good Afternoon, sir")
    else:
        Speak("Good Evening, sir")
    Speak("How can i help you sir? ")
        

wishme()
   
def TaskExe():

    def Music():

        Speak("Tell me the name of the song?")
        musicName = takecommand()

        if 'play date' in musicName:
            os.startfile("C:\\Users\\B75GAMER\\Music\\play date.mp3")
            Speak("Your song (play date) has been started!, Enjoy sir !")

        if 'dance monkey' in musicName:
            os.startfile("C:\\Users\\B75GAMER\\Music\\Dance Monkey.mp3")
            Speak("Your song (Dance monkey) has been started!, Enjoy sir !")
    
    
    def OpenApps():
        Speak("ok sir, wait a second!")

        if 'code' in query:
            Speak("Ok sir, visual studio code is openning now")
            os.startfile("C:\\Users\\B75GAMER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif 'chrome' in query:
            Speak("Ok sir, chrome is openning now")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'discord' in query:
            Speak("Ok sir, Discord is opening Now....")
            os.startfile("C:\\Users\\B75GAMER\\AppData\\Local\\Discord\\app-1.0.9010\\Discord.exe")

    def closeApps():
        Speak("Ok sir, wait a second")

        if 'code' in query:
            os.system("TASKKILL /F /im code.exe")
            Speak("visual studio code is close now.....")

        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
            Speak("youtube is close now......")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            Speak("chrome is close now......")

        elif 'discord' in query:
            os.system("TASKKILL /F /im Discord.exe")
            Speak("Discord is close now......")

    def tran():
        Speak("Tell me the line?")
        line = takecommand()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak(f"The Translation of line is :"+ Text)


    def SpeedTest():
        
        Speak("Ok sir, wait a second !!!")
        Speak("I am checking Your Internet speed")
        speed = speedtest_cli.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctupload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctupload} Mbps.")

        elif 'downloading' in query:
            Speak(f"The downloading speed is {correctDown} Mbps.")

        else:
            Speak(f"Sir, Your downloading speed is {correctDown} Mbps and your uploading speed is {correctupload} Mbps.")






    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir, I am your voice assistant Maya.")
            Speak("How can i help Your sir?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("What About You?")
        
        elif 'your name' in query:
            Speak("I am Maya, Your voice assistant.")
            Speak("i was developed by B75 Team.")


        elif 'bye' in query:
            Speak("Ok sir Bye sir, You call me Anytime!")
            Speak("Have a good day sir...")
            os.system("TASKKILL /F /im code.exe")

        elif 'shutdown' in query:
            Speak("Ok sir Bye sir, You call me Anytime!")
            Speak("Have a good day sir...")
            os.system("TASKKILL /F /im code.exe")


        elif'youtube search' in query:
            Speak("Ok sir, This is what i found on Youtube ! ....")
            query = query.replace("Maya","")
            query = query.replace("youtube search","")
            #web = 'https://www.youtube.com/results?search_query=' + query
            #webbrowser.open(web)
            pywhatkit.playonyt(query)
            Speak("Done sir, Here is your searching Result !")

        elif'play song' in query:
            Speak("Ok sir, your request song is playing from youtube....")
            query = query.replace("Maya","")
            query = query.replace("youtube search","")
            #web = 'https://www.youtube.com/results?search_query=' + query
            #webbrowser.open(web)
            pywhatkit.playonyt(query)
            Speak("Done sir, Here is your song, Please Enjoy song !")

        elif'google search' in query:
            Speak("Ok sir, This is what i found on Google ! ....")
            query = query.replace("Maya","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done sir, Here is your searching Result on Google !")

        elif'visit website' in query:
            Speak("Tell me the name of the websites")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done sir, Here is your searching website!")
        
        elif "open" in query:
            Nameofweb = query.replace("open ","")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            Speak("opening your request sir")

        elif "launch" in query:
            Nameofweb = query.replace("launch ","")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            Speak("launcing your request sir")
            
        elif "wikipedia" in query:
            Speak("Searching wikipedia....")
            query = query.replace("Maya","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            Speak("ok boss, what should i name that file?")
            path = takecommand()
            query = query.replace("Maya","")
            path1name = path + ".png"
            path1 = "C:\\Users\\B75GAMER\\Pictures\\maya\\"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("C:\\Users\\B75GAMER\\Pictures\\maya")
            Speak("Here is your screenshot")

        elif 'music' in query:
            Music()

        elif 'start code' in query:
            OpenApps()

        elif 'start chrome' in query:
            OpenApps()

        elif 'start discord' in query:
            OpenApps()
        
        elif 'close code' in query:
            closeApps()

        elif 'close youtube' in query:
            closeApps()

        elif 'close chrome' in query:
            closeApps()

        elif 'close discord' in query:
            closeApps()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif "time" in query:
            time=datetime.datetime.now().strftime('%I:%M %p')        
            Speak(f"Sir the current time is now {time}")

        elif 'repeat' in query:
            Speak("Speak sir !.....")
            jj = takecommand()
            Speak(f"You said : {jj}")

        elif "temperature" in query:
            search = "temperature in kathmandu"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"The current {search} is {temp}")

        elif "weather" in query:
            search = "weather in kathamandu"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"The current {search} is {temp}")

        elif 'translate' in query:
            tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("maya","")
            Speak("Ok Boss i will remember that : "+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("I know sir, i remember that"+remember.read())

        #elif 'temperature' in query:
            #Temp()
        elif 'internet speed' in query:
            SpeedTest()

        elif 'uploading' in query:
            SpeedTest()

        elif 'downloading' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Sir, Getting data from internet !")
            op = query.replace("maya","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0]
            Speak(how_to_func[0].summary)

        elif 'maya' in query:
            import wikipedia as googleScrap
            query = query.replace("maya","")
            query = query.replace("scrap","")
            query = query.replace("goggle scrap","")
            query = query.replace("google","")
            

            try:
                #pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("Sorry sir, No more data avaiable.")



        elif 'set alarm' in query:
            Speak("Set the alarm for when?")
            time = input("For what time : ")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak ("Sir, Time to wake up sir !")
                    playsound("C:\\Users\\B75GAMER\\Music\\mixkit-alert-alarm-1005.wav")
                    Speak("Alaram has been Closed sir !")

                elif now>time:
                    break

        


 
TaskExe()
            


