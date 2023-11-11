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

# Func to convert text to Morse Code.
def encode(text):
    text = text.upper()
    morse_code = [morse_code_dict[char] for char in text if char in morse_code_dict]
    
    return " ".join(morse_code)


# Ask user to enter the text.
user_input = input("Enter Text: ")
text_to_print = encode(text=user_input)  
print(f"Morse Code: {text_to_print}")      
 