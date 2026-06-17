num=10
guess=int
while guess!=num:
    guess=int(input("Enter a number between 1 and 100: "))
    if guess<num:
        print("Its higher than that")
    elif guess>num:
        print("Its lower than that")
    else:
        print("You guessed it right!")        