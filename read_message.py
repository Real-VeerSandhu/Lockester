import pandas as pd

# Key value data (personalized & note shared)
key_val = pd.read_csv('./Data/encryption.csv')

# Encrypt a string
def encrypt(input_text):
    """Encrypt a string (key-val approach) whilst retaining character data"""

    new_text = ''
    upper_code = ''

    for character in input_text.upper():
        new_text += key_val[key_val['Letter'] == character]['Code'].iloc[0] + '!~!'
    
    for character in input_text:
        upper_code += str(int(character.isupper()))

    return new_text, upper_code

# Decrypt a string
def decrypt(output_text, output_code):
    """Decrypt a string into its original message"""

    output_text = output_text.replace('!~!', ' ')
    text_list = output_text.split()
    
    original_text = ''
    final_text = ''
    
    for text in text_list:
        original_text += key_val[key_val['Code'] == text]['Letter'].iloc[0]

    out = original_text.lower()
    for i in range(len(out)):
        if output_code[i] == '1':
            final_text += out[i].upper()
        else:
            final_text += out[i]
    
    return final_text