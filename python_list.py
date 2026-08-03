number=str(input("Enter number with space as seperator: "))
list1=number.split()
list2=[int(x) for x in list1]
list2.sort()
print(list2)
largest=max(list2)
smallest=min(list2)
print("Largest:", largest)
print("Smallest:", smallest)