import json


def load_json():
    global birthdays
    with open('birthdays.json', 'r') as f:
        birthdays = json.load(f)


def print_json():
    for i in birthdays:
        print(i+' '+birthdays[i])


def add_entry():
    global birthdays
    name = input("Enter name: ")
    birth = input("Enter date of birth(dd/mm/yyyy: ")
    birthdays[name] = birth
    with open('birthdays.json', 'w') as f:
        json.dump(birthdays, f)


def print_menu():
    print()
    print("-----------------------------------")
    print("What do you want to do?")
    print("1. Print all names & dates of birth")
    print("2. Add entry")
    print("3. Exit")
    print("-----------------------------------")
    print(">>> Your choose(1/2/3): ")


if __name__ == '__main__':
    birthdays = {}
    while 1:
        load_json()
        print_menu()
        choose = int(input())
        if choose == 1:
            print_json()
        elif choose == 2:
            add_entry()
        elif choose == 3:
            break


