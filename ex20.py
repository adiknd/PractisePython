def is_num_in_list(list_of_numbers, num):
    if num in list_of_numbers:
        return True
    else:
        return False


my_list = [1, 2, 3, 5, 7, 9]
print(is_num_in_list(my_list, 6))


