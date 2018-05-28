list_of_categories = {}
with open("C:\\Users\\akonkelx\Documents\\list_of_images.txt") as open_list:
    line = open_list.readline()[3:-26]
    while line:
        if line not in list_of_categories:
            list_of_categories[line] = 1
        else:
            list_of_categories[line] += 1
        line = open_list.readline()[3:-26]

for i in list_of_categories:
    print(i + ": " + str(list_of_categories[i]))

