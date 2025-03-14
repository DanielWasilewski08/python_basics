name = input("enter your name: ")
if len(name) < 3:
    print("name must have at least 3 characters")
elif len(name) > 50:
    print("Name can have a maximum of 50 characters")
else:
    print("name looks great!")