word_count=str(input("Enter a word or phrase you want to count: "))
letters=0
numbers=0
special_characters=0
spaces=0
for i in word_count:
    if i.isspace():
        spaces+=1
    elif i.isalpha():
        letters+=1
    elif i.isdigit():
        numbers+=1
    else:
        special_characters+=1
print("Letters:", letters) 
print("Numbers:", numbers)
print("Special Characters:", special_characters)
print("Spaces:", spaces)

        