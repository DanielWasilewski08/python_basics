#searching max value in list. Could be done by max()
list2= [12,88,50,1,-1,33,67]
temp_max = list2[0]
for i in range(1,len(list2)):
    if temp_max < list2[i]:
        temp_max = list2[i]
print(temp_max)