while True:
    try:
        x=float(input("Enter a number to create its multiplication chart: "))
        if x <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
while True:
    try:        
        i=int(input("Enter the number of multiples to display: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
    if i <= 0:
        print("Please enter a positive integer.")
        continue
    break
for i in range(1, i+1):
    print(i,"X",x,"=", i*x)

