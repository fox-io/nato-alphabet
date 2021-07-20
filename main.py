import csv


class NATOPhoneticAlphabet:
    """Class which performs prompts and converts a string to the NATO Phonetic Alphabet."""
    def __init__(self):
        self.file_name = "./nato_phonetic_alphabet.csv"
        self.nato_alphabet = {}
        self.user_input = ""

    def import_data(self):
        """Imports phonetic alphabet data from CSV file."""
        with open(self.file_name) as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                if row[0] != "letter":
                    self.nato_alphabet[row[0]] = row[1]

    def get_user_input(self):
        """Prompts user for a word to convert."""
        self.user_input = input("Enter a word to convert: ")
        pass

    def convert_string(self):
        """Accepts a string and returns a string containing the phonetic version."""
        letters_in_word = list(self.user_input)
        converted_letters = []
        for each_letter in letters_in_word:
            converted_letters.append(self.nato_alphabet[each_letter.upper()])
        print(converted_letters)
        pass


if __name__ == "__main__":
    app = NATOPhoneticAlphabet()
    app.import_data()
    app.get_user_input()
    app.convert_string()
