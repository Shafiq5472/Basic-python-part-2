#generate table from 2 to 20 write it to the diff. file and place it in a folder

for i in range(2,21):
    with open(f"tables/multiplication table of {i}","w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}\n")
            