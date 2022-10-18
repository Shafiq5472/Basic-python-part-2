#write a program to mine a log file and find out weather it contain python

with open("logfile.txt") as f:
    a = f.read()
a.lower()
print(a.find('Python'))

if 'python' in a:
    print("Yes python is present")
#%%
print("\nfor line number")
content = True
i = 1
with open("logfile.txt") as f:
    while content:
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"yes python is present on line number {i}")
        i +=1