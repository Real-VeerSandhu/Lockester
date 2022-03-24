import json

# Key value data (personalized & note shared)
path = './Data/key_val_codes.json'
with open(path) as f:
    key_val = json.load(f)

# Encrypt a string
def encrypt(input_text):
    """Encrypt a string (key-val approach) whilst retaining character data"""

    new_text = ''
    upper_code = ''

    for character in input_text.upper():
        for i in range(len(key_val)):
            if (key_val[i]['Letter'] == character):
                new_text += (key_val[i]['Code']) +'!~!'
    
    for character in input_text:
        upper_code += str(int(character.isupper()))

    return new_text, upper_code

# Decrypt a string
def decrypt(output_text, output_code):
    """Decrypt a string into its original message"""

    output_text = output_text.replace('!~!', ' ')
    text_list = output_text.split()
    
    original_text = ''
    cased_text = ''
    
    for text in text_list:
        for i in range(len(key_val)):
            if (key_val[i]['Code'] == text):
                original_text += (key_val[i]['Letter'])

    out = original_text.lower()
    for i in range(len(out)):
        if output_code[i] == '1':
            cased_text += out[i].upper()
        else:
            cased_text += out[i]
    
    return cased_text