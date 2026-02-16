import os
import subprocess

for file in os.listdir("ui"):
    name, rassh = file.split(".")
    subprocess.run(["pyside6-uic", f".\\ui\\{name}.ui", "-o", f".\\widgets\\{name}.py"])
    
for file in os.listdir("resources"):
    try:
        name, rassh = file.split(".")
        if rassh == "qrc":
            subprocess.run(["pyside6-rcc", f".\\resources\\{name}.qrc", "-o", f".\\resources\\{name}_rc.py"])
    except:
        ...