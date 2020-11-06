
one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
two = ["D", "G"]
three = ["B", "C", "M", "P"]
four = ["F", "H", "V", "W", "Y"]
five = ["K"]
eight = ["J", "X"]
ten = ["Q", "Z"]

def calc_word(word):
    letter_count = 0

    for i in word:
        if i in num_list.one:
            letter_count += 1
        elif i in num_list.two:
            letter_count += 2
        elif i in num_list.three:
            letter_count += 3

    print(letter_count)

    # calc_word('zoo')
    # calc_word('hffgdhnbgfn')
    # calc_word('nhgnmfhgsnsfgngrsnhnrsf')