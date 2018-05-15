Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.position()
(200, 90)
>>> pyautogui.position()
(442, 218)
>>> pyautogui.size()
(1366, 768)
>>> pyautogui.onscreen(2000,1900)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    pyautogui.onscreen(2000,1900)
AttributeError: module 'pyautogui' has no attribute 'onscreen'
>>> pyautogui.onScreen(2000,1900)
False
>>> pyautogui.moveTo(704,55,4)
>>> pyautogui.moveTo(442,218,5)
>>> pyautogui.position()
(876, 89)
>>> pyautogui.moveTo(867,89,4)
>>> pyautogui.moveTo(867,89,4)
>>> pyautogui.dragTo(1272,258,2)
>>> pyautogui.click(1272,258,1)
>>> import pyautogui as pg

>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
>>> import pyautogui as pg
>>> pyautogui.position ()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pyautogui.position ()
NameError: name 'pyautogui' is not defined
>>> pyautogui.position()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pyautogui.position()
NameError: name 'pyautogui' is not defined
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
Traceback (most recent call last):
  File "C:/Users/csci/Desktop/tessaaaaaa loverro.py", line 4, in <module>
    pg.tripleClick ("442=moveTo442, 218=moveTo218")
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 495, in tripleClick
    click(x, y, 3, interval, button, _pause=False)
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 356, in click
    x, y = _unpackXY(x, y)
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 180, in _unpackXY
    raise ValueError('The supplied sequence must have exactly 2 elements ({0} were received).'.format(len(x)))
ValueError: The supplied sequence must have exactly 2 elements (28 were received).
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
Traceback (most recent call last):
  File "C:/Users/csci/Desktop/tessaaaaaa loverro.py", line 4, in <module>
    pg.tripleClick ("442=moveTo442, 218=moveTo218")
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 495, in tripleClick
    click(x, y, 3, interval, button, _pause=False)
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 356, in click
    x, y = _unpackXY(x, y)
  File "C:\Program Files\Python36\lib\site-packages\pyautogui\__init__.py", line 180, in _unpackXY
    raise ValueError('The supplied sequence must have exactly 2 elements ({0} were received).'.format(len(x)))
ValueError: The supplied sequence must have exactly 2 elements (28 were received).
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
>>> 
============ RESTART: C:/Users/csci/Desktop/tessaaaaaa loverro.py ============
>>> 
