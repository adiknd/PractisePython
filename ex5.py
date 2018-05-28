import random

a = [random.randint(1,50) for i in range(random.randint(10,20))]
b = [random.randint(1,50) for i in range(random.randint(10,20))]

print (a)
print (b)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

mylist = []

for elem in a:
    if elem in b:
        if elem not in mylist:
            mylist.append(elem)

print (mylist)