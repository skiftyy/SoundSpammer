import winsound, pyautogui

f = 100

while 0==0:
    for i in range(50):
      pyautogui.press("volumeup")
      winsound.Beep(f, 200)
      pyautogui.press("volumeup")
      f += 100
    for i in range(50):
      pyautogui.press("volumeup")
      winsound.Beep(f, 200)
      pyautogui.press("volumeup")
      f -= 100
