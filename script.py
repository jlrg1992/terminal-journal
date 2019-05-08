import os
import sys
from pathlib import Path


home = str(Path.home())
directory = os.path.exists(home + "/.entry")
if not directory:
    os.system("mkdir ~/.entry")
if len(sys.argv) < 2:
    os.system("python3.7 " + os.path.dirname(os.path.realpath(__file__)) + "/leer.py")
elif sys.argv[1] == "w":
    os.system("python3.7 " + os.path.dirname(os.path.realpath(__file__)) + "/escribir.py")
else:
    print("That command doesn't exists")
