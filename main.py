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

# Func to convert Morse Code to text.
def decode(morse_code):
    decode_dict = {value: key for (key, value) in morse_code_dict.items()}
    decoded_text = [decode_dict[char] for char in morse_code if char in decode_dict]
    
    return " ".join(decoded_text)

# Ask user if he want to encode or decode.
choice = input("Do you want to (E)ncode or (D)ecode? ").lower()

if choice:
    # Ask user to enter the text.
    user_input = input("Enter Text: ")
    if choice == "e":
        text_to_print = encode(text=user_input)        
    else:
        text_to_print = decode(morse_code=user_input)

    # Print the result.
    print(f"Morse Code: {text_to_print}")
