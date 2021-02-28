# Given a two list. Create a third list by picking an even-index element from the first list and odd-index from the second list
list1 = [2,4,6,8,4,3,5,7,9]
list2 = [1,3,5,7,9]
list3 = []

evenchars = list1[0::2]
oddchars = list2[1::2]

print("from list1 printing out the chars in even position " + str(evenchars))
print("from list2 printing out the chars in odd position " + str(oddchars))

list3.extend(evenchars)
list3.extend(oddchars)

print(list3)