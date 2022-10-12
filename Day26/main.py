

import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter:row.code for (index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

run_status = True

while run_status:
    try:
        name = input("Please enter your name?: ").upper()
        result = [phonetic[alphabet] for alphabet in [*name]]
    except KeyError:
        print("Sorry, only letters in the alphabet are accepted")
    else:
        run_status = False

print(result)