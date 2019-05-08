import os, sys
from pathlib import Path
import getpass


pr = str(Path.home())+"/.entry/"
c = 0
items = os.listdir(pr)

#Hate this four lines of code but didn't find another way
lf = []
for names in items:
    if names.endswith(".txt"):
        lf.append(names)
        print(str(lf.index(names))+".-   "+names)

#Which file is going to be opened
ftp = int(input("Select the file's number: "))
p = getpass.getpass("What's your password: ")


os.system( "openssl enc -aes-256-cbc -d -a -k "+p+" -in " + pr + lf[ftp] + " -out .dfile.txt")
if os.path.isfile(".dfile.txt"):
    os.system("vim .dfile.txt" )
    os.system("rm .dfile.txt")
