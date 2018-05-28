def construct_list():
    my_list = [1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8]
    return my_list


def remove_duplicates(temp_list):
    return list(set(temp_list))


print(remove_duplicates(construct_list()))
