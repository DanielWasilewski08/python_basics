unit = input("enter (K)g or (P)ounds: ")
unit = unit.upper()
weight = int(input("enter you weight: "))
if unit == "K":
    print(f"You weigh {weight/0.45} in pounds")
elif unit == "P":
    print(f"You weigh {weight *0.45} in kilograms")
else:
    print("you entered wrong data!!!")