'''print the lengths of list1,tuple1,set1,dict1
print the first element of list1 and tuple1
print the value of lion key of dict1
change the 2nd position element of list1 to "rabbit"
try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
add "monkey" to list1
remove "rabbit" from list1
in dict1 the number of feet is written as value to each animal the fixh has wrong value just fix it. '''


list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

items=[list1,tuple1,set1,dict1]
for i in items:
    iter_len=len(i)
    print(f'lenght of {i} is {iter_len}')
    
    if i==list1 or i==tuple1:
        print(f'first element of {i} is {i[0]}')
        
    if i==dict1:
        print(f"value of key 'lion' is {dict1['lion']}")

list1[1]='rabbit'
print(f'second element of {list1} is {list1[1]}')

##tuples are immutable

list1.append('monkey')
print(f'list1 is: {list1}')

list1.pop(1)
print(f'list1 is: {list1}')

dict1['fish']='wrong'
print(f'dict1 is: {dict1}') ##non ho ben capito la traccia al numero 8