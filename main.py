import pandas


class NATOPhoneticAlphabet:
    """Class which performs prompts and converts a string to the NATO Phonetic Alphabet."""
    def __init__(self):
        self.db = {
            "data_file_name": "./nato_phonetic_alphabet.csv",
            "nato_phonetic_alphabet": {},
            "word_to_convert": "",
        }

        self.import_data()
        self.get_user_input()
        self.convert_string()

    def import_data(self):
        """Imports phonetic alphabet data from CSV file."""
        pass

    def get_user_input(self):
        """Prompts user for a word to convert."""
        self.db["word_to_convert"] = input("Enter a word to convert: ")

    def convert_string(self):
        """Accepts a string and returns a string containing the phonetic version."""
        print(self.db["word_to_convert"])


if __name__ == "__main__":
    app = NATOPhoneticAlphabet()
