import platform
import subprocess
import os

if platform.system() == "Linux":
    p = subprocess.Popen([".linuxDist/dist/Chest/Chest"])
    p.wait()
if platform.system() == "Darwin":
    p = subprocess.Popen([".macDist/dist/Chest/Chest"])
    p.wait()
elif platform.system() == "Windows":
    print("What are you doing on windows?")

try:
    os.rename("DarkBookI.txt", "DarkBookII.txt")
except:
    pass
