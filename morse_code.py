from playsound import playsound
from time import sleep

# Dictionary representing the international morse code
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
                   '0': '-----', ' ': ' '}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode(message):
    cipher = ''
    for letter in message:
        if letter.isalnum():
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/ '
    return cipher


def decode(message):
    symbols = message.split()
    decipher = [REVERSE_MORSE_CODE_DICT[s] if (
        s != '/') else ' ' for s in symbols]
    return ''.join(decipher)


def play_morse_code(message):
    for character in encode(message.upper()):
        if character == '.':
            playsound('dit.wav')
            sleep(0.2)
        if character == '-':
            playsound('dah.wav')
            sleep(0.2)
        if character == ' ' or character == '/':
            sleep(0.32)
