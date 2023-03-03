import pandas

alphabet = "nato_phonetic_alphabet.csv"

csv = pandas.read_csv(alphabet)

alphabet_dict = {value.letter:value.code for (key, value) in csv.iterrows()}
print(alphabet_dict)



def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        coded_words = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(coded_words)
generate_phonetic()