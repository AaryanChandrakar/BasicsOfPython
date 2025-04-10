marks = int(input("Enter Marks: "))

if(marks>=90 and marks<100):
    print("Student recieved Grade A")
elif(marks>=80 and marks<89):
    print("Student recieved Grade B")
elif(marks>=70 and marks<79):
    print("Student recieved Grade C")
elif(marks>=60 and marks<69):
    print("Student recieved Grade D")
elif(marks<60):
    print("Student recieved Grade F")
else:
    print("Invalid Marks")