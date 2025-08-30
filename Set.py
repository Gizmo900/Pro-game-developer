# Sets-unordered and unique (no duplicate)
#Creating sets 
new_set = set()
num = {53,89,3,8,69,23,23,53}

print(num)

#type cast lists to become a set
Mylist=[3,75,34,76,43,90]

myset=set(Mylist)
print(myset)

#if indexing is needed, we type cast set to list.

Mylist1=list(num)
print(Mylist1)
for i in range(len(Mylist1)):
    print(Mylist1[i])

num1 = {63,89,67,84,69,23,23,53}
num2 = {53,89,3,8,69,23,23,53}

#union-returns all elements from the set without duplicates
num=num1.union(num2)
print(num)

#intersection- display all common elements
num=num1.intersection(num2)
print(num)

#difference-elements present in first set
num=num1.difference(num2)
print(num)

#symmetric diffrence-returns elements which is not common
num=num1.symmetric_difference(num2)
print(num)






