import os
import subprocess

for file in os.listdir("ui"):
    name, rassh = file.split(".")
    subprocess.run(["pyside6-uic", f".\\ui\\{name}.ui", "-o", f".\\widgets\\{name}.py"])
    