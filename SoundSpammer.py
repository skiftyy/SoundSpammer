import pyautogui, time, winsound

f = 100
l = 100

while 0==0:
    pyautogui.press("volumeup")
    winsound.Beep(f, l)
    l += 100
    if f < 20000:
        f += 100
