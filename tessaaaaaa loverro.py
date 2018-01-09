import pyautogui as pg
pg.dragTo(67,845,4)
pg.Click

def a(x,y,n):
    pg.moveTo(x,y,n)

def c(x,y,n,i):
    pg.click(x,y,n,i)
    
a(200,300,4)

c(1000,400,3,.1)


    

