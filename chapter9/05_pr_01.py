#read the text from a given file "poem.txt" and findout whether it contain the word twinkle

f = open("poem.txt","r")
txt = f.read()

if 'twinkles' in txt.lower():
    print("Yes Twinkle Is Present")
else:
    print("No Twinkle Is Not Present")
f.close()