from ex17 import r_html

if __name__ == '__main__':
    name_of_file = input("Enter name of file: ")
    with open(name_of_file+'.txt', 'w') as file_with_html_code:
            file_with_html_code.write(r_html)
