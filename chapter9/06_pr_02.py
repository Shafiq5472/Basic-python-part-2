'''The game function in a program lets a user play a game and return the score as an integar.
You need to write a file "Hiscore.txt" which is either blank and contain the previous Hi-score
You need to write a program to update the Hi-score Whenever game break the Hi-score
'''
a = int(input("Your score is:?\n "))
def game():
    return a
score = game()
with open ("Hi_score.txt","r") as f:
    hiscore = f.read()

if hiscore == "":
    with open("Hi_score.txt","w") as f:
        f.write(str(score))

elif int(hiscore) < score:
    with open("Hi_score.txt","w") as f:
        f.write(str(score))
