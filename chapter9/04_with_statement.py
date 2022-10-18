with open ("another.txt","r") as f:
    a = f.read()

with open ("another.txt","a") as f:
    a = f.write("\ni am appending with with statement")
print(a)