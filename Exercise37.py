sides=int(input("Enter the number of sides: "))
if sides == 3:
    a = "Triangle"
elif sides == 4:
    a = "Square"
elif sides == 5:
    a = "Pentagon"
elif sides == 6:
    a = "Hexagon"
elif sides == 7:
    a = "Heptagon"
elif sides == 8:
    a = "Octagon"
elif sides == 9:
    a = "Nonagon"
elif sides == 10:
    a = "Decagon"
else:
    a = "Invalid number of sides"
print(f"The shape with {sides} sides is {a}")

