print("Oscar López")
import random
y=0
x = random.randrange(1,100)
while(y!=x):
    y = int(input("Guess the random number from 1 to 100 "))
    if(y>x):
        print("The number is too high")
    else:
        if(y==x):
            print("You guessed right! the number is ",x)
        if(y<x):
            print("The number is too low")
