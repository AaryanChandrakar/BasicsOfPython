year = 2025

if(year%400==0):
    print(year, "is leap year")
elif(year%4==0 and year%100!=0):
    print(year, "is a leap year.")
else:
    print(year, "is NOT a leap year")