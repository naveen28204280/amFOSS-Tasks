import subprocess
import platform

system = platform.system()
if system == "Linux":
    popen = subprocess.Popen(
        [".linuxDist/dist/Kharnok the BloodForged/Kharnok the BloodForged"]
    )
    popen.wait()
elif system == "Darwin":
    popen = subprocess.Popen(
        [".macDist/dist/Kharnok the BloodForged/Kharnok the BloodForged"]
    )
    popen.wait()
elif system == "Windows":
    print("What are you doing on windows?")
