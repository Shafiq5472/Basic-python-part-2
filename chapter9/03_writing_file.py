f = open ("another.txt","w")
f.write("Please write this to the file\n")
f.close

f=open("another.txt","a")
f.write(" I am appending")
f.close()