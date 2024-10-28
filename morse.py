MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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
    encrypted = ''
    for letter in message:
        if letter != ' ':
            encrypted += MORSE_CODE_DICT[letter] + ' '
        else:
            encrypted += ' '
    return encrypted

def decrypt(message):
    message += " "
    decrypted = ''
    morse_letter = ''
    i=0
    for letter in message:
        if (letter != ' '):
            i = 0
            morse_letter += letter
        else:
            i += 1
            if i == 2:
                decrypted += ' '
            else:
                decrypted += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_letter)]
                morse_letter = ''
    return decrypted

still_playing = True
while (still_playing):
    option = input("Enter 1 if you want to Convert TO Morse\nEnter 2 if you want to Convert from Morse\nEnter X to stop\n")
    if option == "1":
        text = input("Input TEXT message\n")
        encrypted_msg = encrypt(text.upper())
        print(encrypted_msg)
        choice = input("Do you want to decrypt the previous message?Y for yes, N for No\n")
        if choice =="Y" or choice =="y":
            print(decrypt(encrypted_msg))
    if option == "2":
        text2 = input("Input MORSE message\n")
        decrypted_msg = decrypt(text2.upper())
        print(decrypted_msg)
        choice2 = input("Do you want to encrypt the previous message?Y for yes, N for No\n")
        if choice2 =="Y" or choice2 =="y":
            print(encrypt(decrypted_msg))
    if option =="X" or option=="x":
        break
