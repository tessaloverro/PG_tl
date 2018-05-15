import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=sLKPtPA2G40","https://www.youtube.com/watch?v=rOS5Nfz2S_k"]

music = ["https://www.spotify.com/us/", "https://soundcloud.com/"]

answer = pg.prompt (
"""
Which would you rather do?
a) Watch videos
b)Listen to music


"""
)

if answer == "a":
    for i in vidoes:
        webbrowser.open(i)

        
elif answer == "b":
    for i in music:
        webbrowser. open (i)
