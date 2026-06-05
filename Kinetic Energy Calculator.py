run=str
run="yes"
while run=="yes":
    while True:
        try:
            mass=float(input("Enter your mass: "))
            if mass<=0:
                print("Mass value must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for mass.")
    unit_of_mass=input("Enter the unit of mass (kg or g): ")
    unit_of_mass=unit_of_mass.lower()
    if unit_of_mass=="g":
        mass=mass/1000
    
    while True:
        try:
            velocity=float(input("Enter your velocity: "))
            unit_of_velocity=input("Enter the unit of velocity (m/s or km/h): ")
            unit_of_velocity=unit_of_velocity.lower()
            if unit_of_velocity=="km/h":
                velocity=velocity/3.6
            if velocity>=299792458:
                print("Velocity cannot exceed the speed of light.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for velocity.")
    
    kinetic_energy=0.5*mass*velocity**2
    
    print("Mass is:",f"{mass}{unit_of_mass}")
    print("Velocity is:",f"{velocity}{unit_of_velocity}")
    print("Kinetic Energy is:", kinetic_energy, "Joules")
    run=input("Do you want to calculate again? (yes or no): ").lower()