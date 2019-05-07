import datetime
import os
from pathlib import Path

t = datetime.datetime.now() # Get the date with which is going to be the file name
fn = str(Path.home())+"/.entry/" + str(t.strftime("%Y-%m-%d") + ".txt")
p = str(t.strftime("%X")) + "\n"

# Write the content
while True:
    tx = str(input("Text: "))
    if(len(tx) < 1):
        exists = os.path.isfile(fn)
        if exists:
            os.system("openssl enc -aes-256-cbc -d -a -in " + fn + " -out " + fn + ".tmp" )
        with open(fn+".tmp", "a+") as f:
            f.write(p)
        os.system('clear')
        os.system("openssl enc -aes-256-cbc -salt -a -in " + fn + ".tmp -out " + fn)
        os.system("rm "+fn+".tmp")
        print("Saved")
        break

    p += tx + "\n"

