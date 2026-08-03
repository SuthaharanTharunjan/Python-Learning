number=str(input("Enter number with space as seperator: "))
list=number.split()
list2=[]
for i in list:
    if int(i) not in list2:
        list2.append(int(i))

list2.sort()
print(list2)