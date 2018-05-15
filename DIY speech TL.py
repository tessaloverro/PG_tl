import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")

r= sr. Recognize()
with sr. Microphone() as source:
    speak. Speak ("Hi Tessa, what video should we watch?")
    print ("Listening...")
    audio= r.listen(source)
    print ("Thinking...")

speak. Speak ("What video do you want to watch?")

video = pg.prompt ("Enter the video below.")

speak. Speak ("OK, let's go find some " + video + "on Youtube.")

wb.open("https://www.youtube.com/results?search_query=" + video)

try:
    words= r.recognize_google(audio)
    speak.Speak("Ok Tessa, let's look for " + r.recognize_google(audio))
    wb.open("http://www.youtube.com/results?search_query=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr. RequestError as e:
    print("Could not request results from Google Search Recognition service; {0}". format (e))




