
y=int(input("Enter a number from 1 to 500: "))
while y<1 or y>500:
    print("Invalid input. Please enter a number from 1 to 500.")
    y=int(input("Enter a number from 1 to 500: "))
x=int(input("Enter a number from 500 to 1000: "))
while x<500 or x>1000:
    print("Invalid input. Please enter a number from 100 to 1000.")
    x=int(input("Enter a number from 500 to 1000: "))
z=x-y
if   0<z<166.67:
    print("1")
elif 166.67<=z<333.34:
    print("2")
elif 333.34<=z<500:
    print("3")     
elif 500<=z<666.67:
    print("4")
elif 666.67<=z<833.34:
    print("5")
elif 833.34<=z<1000:
    print("6")