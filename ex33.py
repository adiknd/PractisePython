import time

def write_all_names():
    for i in names_and_births:
        time.sleep(0.7)
        print('-'+i)


names_and_births ={
    'Adrian Konkel':'03/01/1996',
    'Ewelina Krówka':'24/07/1996',
    'Andrzej Grabowski':'15/03/1952'
}


if __name__ == '__main__':
    print(">>>Welcome to the birthday dictionary. We know the birthdays of:")
    time.sleep(1)
    write_all_names()
    name = input('>>>Who\'s birthday do you want to look up?: ')
    if name in names_and_births:
        print(names_and_births[name])
    else:
        print("No data found")