def get_string_from_user():
    words = input("Enter your string: ")
    return words


def string_in_backward_order(some_words):
    some_words = str(some_words).split()
    some_words.reverse()
    some_words = " ".join(some_words)
    return some_words


print(string_in_backward_order(get_string_from_user()))




