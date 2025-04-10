order_size = "Small"    #Small, Medium, Large
extra_shot = False

if(extra_shot):
    coffee = order_size + " coffee with extra short"
else:
    coffee = order_size + " coffee with no extra short"

print(coffee)