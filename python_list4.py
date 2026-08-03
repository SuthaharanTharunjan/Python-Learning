numbers=str(input("Enter numbers with space as separator: "))
list=[int(x) for x in numbers.split()]
list2=[]
for i in list:
    digit=[int(x) for x in str(i)]
    list2.append(sum(digit))
print(list2)
