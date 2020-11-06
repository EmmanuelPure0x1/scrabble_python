class NumbersLetters:
    def __init__(self):
        self.one = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
        self.two = ["d", "g"]
        self.three = ["b", "c", "m", "p"]
        self.four = ["f", "h", "v", "w", "y"]
        self.five = ["k"]
        self.eight = ["j", "x"]
        self.ten = ["q", "z"]

        # # I am going to create the letter arrays which will be stored in variables
        # # These are the arrays.
        # one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        # two = ["D", "G"]
        # three = ["B", "C", "M", "P"]
        # four = ["F", "H", "V", "W", "Y"]
        # five = ["K"]
        # eight = ["J", "X"]
        # ten = ["Q", "Z"]

    # line 13 is the declaration of a function called: word_calc and it will take a str which it will pass      as word
    def word_calc(self, word):

        # This is a variable which has been given the value of 0
        letter_count = 0

        # This next step is a for loop which iterates over the the string passed as word in the function.
        for i in word:
            # for each letter in the word the loop is iterating and evaluating which section it belongs to.
            if i in self.one:
                # line below looks at whether the letter is in array called 'one' and +1 to letter count var if it is.
                letter_count += 1
            elif i in self.two:
                letter_count += 2
            elif i in self.three:
                letter_count += 3
            elif i in self.four:
                letter_count += 4
            elif i in self.five:
                letter_count += 5
            elif i in self.eight:
                letter_count += 8
            elif i in self.ten:
                letter_count += 10

        return letter_count

word = NumbersLetters()
print(word.word_calc('zoooo'))