run = "yes"
gravity = 9.81
print("""
=====================================
     Potential Energy Calculator
=====================================
""")
while run == "yes":
    while True:
        try:
            mass=float(input("Enter your mass: "))
            if mass<=0:
                print("Mass value must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for mass.")
    while True:
        try:
            unit_of_mass=input("Enter the unit of mass (kg or g): ")
            unit_of_mass=unit_of_mass.lower()
            if unit_of_mass not in ["kg", "g"]:
                print("Invalid unit of mass. Please enter 'kg' or 'g'.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter 'kg' or 'g' for the unit of mass.")
    if unit_of_mass=="g":
        mass=mass/1000
    
    while True:
        try:
            height=float(input("Enter your height: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for height.")    
    while True:
        try:
            unit_of_height=input("Enter the unit of height (m or km): ")
            unit_of_height=unit_of_height.lower()  
            if unit_of_height not in ["m", "km"]:    
                print("Invalid unit of height. Please enter 'm' or 'km'.")    
                continue   
            break    
        except ValueError:
            print("Invalid input. Please enter 'm' or 'km' for the unit of height.")            
    if unit_of_height=="km":
                height=height*1000            
    
    potential_energy=mass*gravity*height
    
    print("Mass is:",f"{mass}{unit_of_mass}")
    print("Height is:",f"{height}{unit_of_height}")
    print("Potential Energy is:", potential_energy, "Joules")
    run=input("Do you want to calculate again? (yes or no): ").lower()