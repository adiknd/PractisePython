divisors_list = []
num = int(input("Enter a number ...: "))
for i in range(1,num+1):
    if num % i == 0:
        divisors_list.append(i)

for i in divisors_list:
    print (i, end = ', ')