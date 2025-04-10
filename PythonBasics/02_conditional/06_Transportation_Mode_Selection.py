distance = 12

if distance < 3:
    mode = "Walk"
elif distance <= 15 and distance > 3:
    mode = "Bike"
elif distance > 15:
    mode = "Car"

print("Suitable mode of transportation for", distance,"km is: ", mode)