
f = open("sample.txt",'r')
data = f.read()
#data = f.read(15) --> read 15 alphabet 
print(data)
f.close()