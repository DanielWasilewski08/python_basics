#removing duplicates
list3 = [5,78,-4,5,33,43,5,12,82,33]
for item in list3:
    our_range = list3[list3.index(item)+1::]
    if item in our_range:
        list3.pop(list3.index(item))
print(list3)