numbers=str(input("Enter numbers with space as separator: "))
list=[int(x) for x in numbers.split()]
list.sort()
list2=[]
[list2.append(x) for x in list if x not in list2]
print(f"Second largest number is: {list2[-2]}")
list3=[]
[list3.append(x) for x in list2 if x%2==0]
print(f"Even numbers are: {list3}")
list4=[]
[list4.append(x) for x in list2 if x%2!=0]
print(f"Odd numbers are: {list4}")