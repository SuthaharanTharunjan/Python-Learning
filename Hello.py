mass=float(input("Enter your mass: "))
unitofmass=input("Enter the unit of mass (kg or g): ")
if unitofmass=="g":
    mass=mass/1000
velocity=float(input("Enter your velocity in m/s: "))
kinetic_energy=0.5*mass*velocity**2
print("Your kinetic energy is:", kinetic_energy, "Joules")
print("Thank you for using this programme")