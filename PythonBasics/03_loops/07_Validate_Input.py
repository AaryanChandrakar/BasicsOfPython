# my_input = int(input("Enter Your Input: "))

# while(my_input>=1 and my_input<=10):
#     print("Valid Input")
#     break

# while(my_input>10 or my_input<0):
#     my_input = int(input("Enter Your Input: "))

while True:
    num = int(input("Enter a number b/w 1 to 10: "))
    if 1<= num <=10:
        print("Valid input")
        break
    else:
        print("Invalid input please verify.")