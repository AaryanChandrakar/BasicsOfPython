age = int(input("Enter Age: "))

if(age<13):
    print("Person is Child")
elif(age>=13 and age<19):
    print("Person is Teenager")
elif(age>=20 and age<59):
    print("Person is Adult")
elif(age>=60):
    print("Person is Senior")
