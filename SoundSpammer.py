import pyautogui, time, winsound

f = 100

for i in range(50):
    pyautogui.press("volumeup")

while 0==0:
    pyautogui.press("volumeup")
    winsound.Beep(f, 500)
    if f < 8000:
        f += 100
