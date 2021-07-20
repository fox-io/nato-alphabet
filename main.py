import pandas


class NATOPhoneticAlphabet:
    """Class which performs prompts and converts a string to the NATO Phonetic Alphabet."""
    def __init__(self):
        self.db = {
            "data_file_name": "./nato_phonetic_alphabet.csv",
            "nato_phonetic_alphabet": pandas.DataFrame(),
            "word_to_convert": "",
        }

    def import_data(self):
        """Imports phonetic alphabet data from CSV file."""
        self.db["nato_phonetic_alphabet"] = pandas.read_csv(self.db["data_file_name"])

    def get_user_input(self):
        """Prompts user for a word to convert."""
        self.db["word_to_convert"] = input("Enter a word to convert: ")

    def convert_string(self):
        """Accepts a string and returns a string containing the phonetic version."""
        letters_in_word = list(self.db["word_to_convert"])
        converted_letters = []
        for each_letter in letters_in_word:
            result = self.db["nato_phonetic_alphabet"].query(f'letter == "{each_letter.upper()}"')
            converted_letters.append(result.values[0][1])
        print(converted_letters)


if __name__ == "__main__":
    app = NATOPhoneticAlphabet()
    app.import_data()
    app.get_user_input()
    app.convert_string()
