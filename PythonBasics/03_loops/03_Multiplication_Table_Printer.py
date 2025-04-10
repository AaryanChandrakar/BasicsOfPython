n = int(input("Enter a number to print a table: "))

for i in range(1, 10+1):
    if(i==5):
        print("5th Iteration Skiped")
        continue
    
    print(i,"*",n,"=",i*n)