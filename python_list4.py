numbers=str(input("Enter numbers with space as separator: "))
list=[int(x) for x in numbers.split()]
list2=[]
while max(list) >= 10:
    for i in list:
        digit=[int(x) for x in str(i)]
        list2.append(sum(digit))
    print(list2)
    list.clear()
    list=list2.copy()
    list2.clear()
print(f"Final list is: {list}")