#rename file
import os

oldname="prob10.txt"
newname = "rename by python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove("prob10.txt")