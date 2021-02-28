# given 2 list of ints create a 3rd list such that should contain only odd numbers
#from the first list and even numbers from the second list
list1=[12,42,2,4,67,43,45,23,45,56,23,45]
list2=[2,42,52,63,56,23,21,56,32,67,21,5]
list3=[]
list4=[]
for val in list1:
    if (val % 2) != 0:
        list3.append(val)
print(list3)
for val2 in list2:
    if (val2 % 2) == 0:
        list4.append(val2)
print(list4)
list3.extend(list4)
print(list3)
        
        
    
    
