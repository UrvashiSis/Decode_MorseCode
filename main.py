import re

def decodeBits(bits):
    # Remove leading and trailing zeros
    bits = bits.strip('0')

    # Find the transmission rate (time unit)
    time_unit = min(map(len, re.findall(r'0+|1+', bits)))

    # Define the mapping for Morse code characters
    morse_to_char = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                     '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                     '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                     '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0',
                     '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                     '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
                     '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
                     '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
                     '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS', '': ' '}

    # Replace sequences of 0s and 1s with 0 or 1
    bits = bits.replace('0' * 7 * time_unit, '   ')
    bits = bits.replace('0' * 3 * time_unit, ' ')
    bits = bits.replace('1' * 3 * time_unit, '-')
    bits = bits.replace('1' * time_unit, '.')

    # Convert binary Morse code to Morse code characters and then to a human-readable string
    morse_code_string = ''.join(morse_to_char[char] for char in bits.split() if char in morse_to_char)

    return morse_code_string

def decodeMorse(morseCode):
    # Define the mapping for human-readable characters to Morse code
    char_to_morse = {v: k for k, v in morse_to_char.items()}
    
    # Convert the Morse code string to Morse code words
    morse_code_words = morseCode.strip().split('   ')

    # Convert Morse code words to a human-readable string
    human_readable_string = ' '.join(''.join(char_to_morse[char] for char in word.split()) for word in morse_code_words)

    return human_readable_string
    
morseCode = '.... . -.--   .--- ..- -.. .'
bits = decodeBits(morseCode)
human_readable_string = decodeMorse(bits)
print(human_readable_string)

