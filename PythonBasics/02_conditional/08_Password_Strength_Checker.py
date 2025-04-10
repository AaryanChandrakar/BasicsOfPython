password = "123456789012345"

if (len(password)<6):
    strength = "Weak"
elif (len(password)>6 and len(password)<10):
    strength = "Medium"
elif (len(password)>10 ):
    strength = "Strong"


print("Password Strenght is: ",strength)