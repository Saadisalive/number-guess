import random #importing module
playing = True #initialize
number = str(random.randint(10,20)) #random in-built function

print("I will generate a number from 0 to 9,and you have to guess the number one digit at a time")
print("the game ends when you get 1 hero!")
#ilterate loop till the condition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("you win the game.You are great")
        print("The numberwas",number)
        break
    else:
        print("your guess isn't quite right,try again. \n")