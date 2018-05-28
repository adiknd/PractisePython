import json
from collections import Counter


birthdays = {}
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def load_json():
    global birthdays
    with open('birthdays.json', 'r') as file:
        birthdays = json.load(file)


def print_json():
    for i in birthdays:
        print(i+' '+birthdays[i])


if __name__ == '__main__':
    load_json()
    birthdays_count = []

    for i in birthdays:
        birthdays_count.append(int((birthdays[i])[3] + (birthdays[i])[4]))

    for i in range(0, len(birthdays_count)):
        birthdays_count[i] = months.get(birthdays_count[i])

    print(birthdays_count)
    # for i in birthdays_count:
    #     if i in months.keys():
    #         birthdays_count[birthdays_count.index(i)] = months[i]

    birthdays_count = Counter(birthdays_count)

    # for i in birthdays_count:
    #     print(i+': '+str(birthdays_count[i]))








