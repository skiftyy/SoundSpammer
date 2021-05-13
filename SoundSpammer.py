import pyautogui, time, winsound

f = 100

for i in range(50):
    pyautogui.press("volumeup")

while 0==0:
    winsound.Beep(f, 200)
    pyautogui.press("volumeup")
    if f < 8000:
        f += 100
