
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names_list = names_file.read().split("\n")

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    starting_letter = letter_file.read()

for name in names_list:
    letter_with_name = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode="w") as new_letter:
        new_letter.write(letter_with_name)

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp