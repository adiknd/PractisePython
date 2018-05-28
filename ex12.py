import random


def generate_random_list():
    rand_list = [random.randint(0, 30) for k in range(random.randint(5, 10))]
    print("Random list: "+str(rand_list))
    return rand_list


def first_and_last_list(old_list):
    new_list = [old_list[0], old_list[-1]]
    return new_list


print("New list: "+str(first_and_last_list(generate_random_list())))


