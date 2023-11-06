# Func to convert text to Morse Code.
def text_to_morse_code(text):
    morse_code_dict = {
        'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-',
        ' ': ' '
        }

    text = text.upper()
    morse_code = [morse_code_dict[char] for char in text if char in morse_code_dict]
    
    return " ".join(morse_code)


# Ask user to enter the text.
text = input("Enter Text to convert to Morse Code: ")

# Call text_to_morse_code func to convert the text we got from user.
morse_code = text_to_morse_code(text=text)
print(f"Morse Code: {morse_code}")