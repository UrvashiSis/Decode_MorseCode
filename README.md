# Decode_MorseCode
- Import the re module for regular expressions. 
-The decodeBits function takes the input bits (a string containing 0s and 1s) and removes any leading and dragging zeros.
-Using regular expressions, we finds all sequences of consecutive 0s and 1s and calculates the minimum length among them, 
 which gives the transmission rate of the message.
-Define a dictionary morse_to_char used to convert Morse code characters to readable characters 
- Replace the sequences of 0s and 1s with spaces or dashes or dots.
- we join the Morse code characters to form a human-readable Morse code string.
- In the decodeMorse function, we create a new dictionary char_to_morse that is the reverse of the morse_to_char dictionary. This dictionary 
 maps human-readable characters to their corresponding Morse code characters. It is used to convert Morse code words to a human-readable string.
- we split the input morseCode into Morse code words by using three spaces as the separator. The strip() method is used to remove any leading and
 trailing spaces before splitting.
- Now, we convert each Morse code word to a human-readable character by using the char_to_morse dictionary and join them with spaces to form a
 human-readable string.
