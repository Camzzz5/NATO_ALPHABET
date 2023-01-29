import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
#data_dict = {key: value for (key, value) in zip(data.letter, data.code)}
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(data_dict)
word = input("ENTER A WORD: \n").upper()
data_list = [data_dict[letter] for letter in word]
print(data_list)

