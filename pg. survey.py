import pyautogui as pg
import time
import webbrowser
points = 0

#Question goes here
answer = pg.prompt(
"""

Que est-ce que tu aimes faire?

a) J'aime me maquiller.
b) J'aime jouer au mon chat.
c) J'aime voyager.

"""
    )

pg.alert("You chose " + answer)

#Answers and points go here
if answer== "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""

Que est-ce que tu mange?

a) Je mange une pizza.
b) Je mange les fruits.
c) Je mange une salad.

"""
    )

pg.alert("You chose " + answer)

#Answers and points go here
if answer== "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
#Question goes here
answer = pg.prompt(
"""

Que est-ce que tu fais dans la nuit.

a) Dans la nuit, je danse dans un club.
b) Dans la nuit, je regarde la télé.
c) Dans la nuit, je mange dans un bon restaurant.

"""
    )


#Answers and points go here
if answer== "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
pg.alert("You chose " + answer)


#END OF SURVEY
pg.alert ("OK, here's your character...")
#Teala
if points <=3:
    pg.alert("You are Teala!")
    webbrowser.open("https://www.youtube.com/user/Tealaxx2")
#Sierra
elif points >3 and points <=6:
    pg.alert("You are Sierra!")
    webbrowser.open("https://www.youtube.com/user/SierraMarieMakeup")
#Eva
elif points >6:
    pg.alert("You are Eva!")
    webbrowser.open("https://www.youtube.com/user/mylifeaseva")

    
