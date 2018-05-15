import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak= wincl.Dispatch ("SAPI.SpVoice")

speak. Speak ("What's your favorite dessert?")

answer= pg.prompt("Enter your favorite dessert")

if answer== "chocolate mousse":
    speak.Speak("Wow that sounds good!")
elif answer== "coconut cookies":
    speak. Speak ("Ew. Who likes those?")
elif answer== "rainbow cake":
    speak. Speak ("Rainbow cake is AMAZING.")
else:
    speak. Speak ("Your favorite dessert is " + answer)

