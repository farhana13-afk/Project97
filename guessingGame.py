from random import randint

print("Guessing Game!")

chances = 0
number = 6

print("Guess the number the computer is thinking! Hint: (1-9)")
  
while chances < 5:

    guess = int(input("is the number: "))
    chances = chances + 1
    if guess == number :
        print("Congratuialtions You Won!!!")
        break

if not chances < 5: 
    print("You LOSE!!! The number is", number)