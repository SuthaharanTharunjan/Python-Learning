mass=float(input("Enter your mass: "))
if mass<=0:
    print("Mass value must be greater than zero.")
    mass=float(input("Enter your mass: "))
unit_of_mass=input("Enter the unit of mass (kg or g): ")
if unit_of_mass=="g":
    mass=mass/1000


velocity=float(input("Enter your velocity: "))
unit_of_velocity=input("Enter the unit of velocity (m/s or km/h): ")
if unit_of_velocity=="km/h":
    velocity=velocity/3.6
if velocity>=299792458:
    print("Velocity cannot exceed the speed of light.")
    velocity=float(input("Enter your velocity: "))
    unit_of_velocity=input("Enter the unit of velocity (m/s or km/h): ")


kinetic_energy=0.5*mass*velocity**2


print("Your kinetic energy is:", kinetic_energy, "Joules")
print("Thank you for using this programme")