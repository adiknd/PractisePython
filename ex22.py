list_of_names = {}

with open("C:\\Users\\akonkelx\Documents\\nameslist.txt", 'r') as open_file:
    line = open_file.readline()
    line = line.strip()
    while line:
        if line not in list_of_names:
            list_of_names[line] = 1
        else:
            list_of_names[line] += 1
        line = open_file.readline()
        line = line.strip()
print(list_of_names)






