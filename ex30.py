import  random

with open("sowpods.txt" ,'r') as sowpods:
    list_of_sowpods = []
    for line in sowpods:
        list_of_sowpods.append(line)
random_number =random.randint(0, len(list_of_sowpods))


