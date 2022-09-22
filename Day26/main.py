

import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter:row.code for (index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Please enter your name?: ").upper()
result = [phonetic[alphabet] for alphabet in [*name]]
print(result)