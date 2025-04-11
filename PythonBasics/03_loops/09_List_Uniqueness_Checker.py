items = ["apple", "banana", "orange","apple","banana", "mango"]
unique_item = set()

for i in items:
    if i in unique_item:
        print("Duplicate: ",i)
    unique_item.add(i)

print("This are non repeated items: ", unique_item)


    