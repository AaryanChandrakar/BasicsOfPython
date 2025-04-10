n = int(input("Enter Any Integer Number: "))
sum=0

for i in range(n+1):
    if i%2==0:
        sum+=i
    
print("Sum of Even Number from 0 to",n,"is: ",sum)