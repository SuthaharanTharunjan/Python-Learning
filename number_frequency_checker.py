number=str(input("Enter number with space as separator: "))
list=[int(x) for x in number.split()]
count=0
for i in list:
    for j in list:
        if i==j:
            list.remove(j)
            count=count+1
    list.remove(i)        
    print(f"{i} occurs {count} times")     
    count=1
list.remove(0)

#scrappped