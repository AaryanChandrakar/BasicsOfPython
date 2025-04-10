is_wednesday = bool(input("type anything only if it is wednesday: "))

age = int(input("Enter Age: "))

tp_adults = 12
tp_children = 8

if(is_wednesday):
    if(age<18):
        print("Ticket Price for children on wednesday is: $",tp_children - 2)
    elif(age>=18):
        print("Ticket Price for adults on wednesday is: $",tp_adults - 2)
else:
    if(age<18):
        print("Ticket Price for children is: $", tp_children)
    elif(age>=18):
        print("Ticket Price for adults is: $", tp_adults)