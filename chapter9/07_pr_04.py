#A file contain a word Donkey multiple time replace this word with ##### by updating the same file

with open("replace.txt","r") as f:
    x = f.read()
p=x.lower()
z = p.replace("donkey","$$$")

with open("replace.txt","w") as f:
    f.write(z)

#%%
#repeat above for a list of such word to be censoered

words = ["snake","mental","dog"]

with open("replace.txt","r") as f:
    content = f.read()
content.lower()
for word in words:
    content = content.replace(word,"$$$")

    with open("replace.txt","w") as f:
        f.write(content)
