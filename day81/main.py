english_to_morse_dict = {'A': '.-', 'B': '-...',
                         'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-',
                         'L': '.-..', 'M': '--', 'N': '-.',
                         'O': '---', 'P': '.--.', 'Q': '--.-',
                         'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--',
                         'X': '-..-', 'Y': '-.--', 'Z': '--..',
                         '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-',
                         '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    message_list = [letter for letter in message]
    morse_code = []
    for letter in message_list:
        morse_code.append(english_to_morse_dict[letter])
    return ' '.join(morse_code)


def decrypt(message):
    morse_code = message.split(' ')
    text = []
    for code in morse_code:
        for key in english_to_morse_dict:
            if english_to_morse_dict[key] == code:
                text.append(key)
    return ' '.join(text)


def main():
    run = 'C'
    while run == 'C':
        print('***Morse Code Converter***')
        message = input('Please type your message:\n').upper()
        select = input('Please type E to ecrypt or D to decrypt\n').upper()
        if select == 'E':
            print(encrypt(message))
        elif select == 'D':
            print(decrypt(message))
        run = input('Please type C to continue or F to finish\n').upper()
        if run == 'F':
            pass

main()
