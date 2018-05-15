import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')

pg.hotkey('winleft')
pg.typewrite('chrome\n',0.2)
pg.hotkey('winleft','up')
time.sleep(3)
pg.typewrite('www.sephora.com',0.2)
pg.click()







