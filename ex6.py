word = str(input("Enter some string: "))
reverse_word = word[::-1]
if word==reverse_word:
    print("The word is a polindrome! ")
else:
    print("The world is NOT a polindrome! ")