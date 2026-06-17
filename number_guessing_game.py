import random
while True:
    num=random.randint(1,100)
    guess=int
    while guess!=num:
        guess=int(input("Enter a number between 1 and 100: "))
        if guess<num:
            print("Its higher than that")
        elif guess>num:
            print("Its lower than that")
        else:
            print("You guessed it right!")
    if input("Do you want to play again? (y/n): ").lower() != 'y':
        break
print("Thanks for playing!")