n = int(input("Enter Number: "))
flag = False
if n==0 or n==1:
    print(n," is not a prime number.")
elif(n>1):
    for i in range(2, n):
        if (n%i)==0:
            flag = True
            break
        else:
            flag = False
            

    if (flag == True):
        print(n," is not a prime number.")
    else:
        print(n," is a prime number.")

