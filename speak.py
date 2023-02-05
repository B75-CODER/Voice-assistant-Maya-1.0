from gtts import gTTS
from playsound import playsound
import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice',voices[2].id)
Assistant.setProperty('rate',190)

def Speak(audio):
    tts = gTTS(audio, lang="hi")
    print("")
    print(f"Maya : {audio}.")
    print("")

    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
   

Speak("Having survived the Cultural Revolution, the White Dagoba, which was designed by the Nepali architect Arniko, is the oldest and largest Tibetan Buddhist shrine in China and perhaps the last remaining building of the Yuan Dynasty in Beijing today.")