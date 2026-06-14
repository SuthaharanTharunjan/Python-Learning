while True:
    try:
        x=float(input("Enter a number to create its multiplication chart: "))
        if x <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
i=int(input("Enter the number of multiples to display: "))
for i in range(1, i+1):
    print(i,"X",x,"=", i*x)

