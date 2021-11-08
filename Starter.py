import shutil

original = r'C:\GitHub\SoundSpammer\SoundSpammer Executable.exe'
target = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'

shutil.copy(original, target)