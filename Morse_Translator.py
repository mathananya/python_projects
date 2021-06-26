
morse_letters = {
    "A": "·-",
    "B": "-···",
    "C": "-·-·",
    "D": "-··",
    "E": "·",
    "F": "··-·",
    "G": "--·",
    "H": "····",
    "I": "··",
    "J": "·---",
    "K": "-·-",
    "L": "·-··",
    "M": "--",
    "N": "-·",
    "O": "---",
    "P": "·--·",
    "Q": "--·-",
    "R": "·-·",
    "S": "···",
    "T": "-",
    "U": "··-",
    "V": "···-",
    "W": "·--",
    "X": "-··-",
    "Y": "-·--",
    "Z": "--··",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ",":"--..--",
    ".":".-.-.-",
    "?":"..--..",
    "/":"-..-.",
    "-":"-....-",
    "(":"-.--.",
    ")":"-.--.-"
    }

print("\n~ MORSE CODE TRANSLATOR ~")

sentence = input("\nPlease type the sentence you wish to translate:\n")
sentence = sentence.upper()

word_list = sentence.split()

def encrypt(this_letter):
    m_trans = morse_letters[this_letter]
    return m_trans
    

for word in word_list:
    for letter in word:
        print(encrypt(letter)+"   ", end='')
    print("      ", end = '')





