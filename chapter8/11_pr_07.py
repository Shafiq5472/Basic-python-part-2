#remove a word from the string and strip it at a same tym

def remove_and_strip(string,word):
    newStr = string.replace(word,"shanu")
    return newStr.strip()

a = "   Harry is a good    "
n = remove_and_strip(a,"Harry")
print(n)