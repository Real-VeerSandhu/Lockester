# Imports
import datetime
import time
import json
from read_message import encrypt, decrypt

# Set up storage & time
path = './Notes/stored_logs.json'
with open(path) as f:
    stored_logs = json.load(f)

current_date = datetime.date.today().strftime('%B %d, %Y')
current_time = time.strftime("%H:%M:%S", time.localtime())
c_time = str(current_time) + ' - ' + str(current_date)

# Input a new log
def get_new_log(input):
    if input != '':
        encryption = encrypt(input) # read_message.py encryption function
        write_json({'Date': str(current_date), 'Time': str(current_time), 'Log': encryption[0], 'Code': encryption[1]})
        
        print(f'\n*Log Accepted*\n{encryption}')
        return encryption
    else:
        return '\n*Log Failed*'

# Read an old log 
def read_old_logs(date):
    counter = 0
    texts = []
    for i in range(len(stored_logs)):
        if (stored_logs[i]['Date'] == date):
            counter += 1
            texts.append(decrypt(stored_logs[i]['Log'], stored_logs[i]['Code'])) # read_message.py decryption function
    if counter != 0:
        print('\n*Log(s) Accessed*\n')
        for i in range(len(texts)):
            print(f'#{i+1} {texts[i]}')
        return True
    else:
        print('\n*No Such Logs*')

# Add log to storage
def write_json(new_data, file_name='./Notes/stored_logs.json'):
    with open(file_name,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

# User interface
print('Exit -> 0')
print('Enter Log -> 1')
print('Access Previous Logs -> 2\n')

confirm = int(input())

print('='*50)
print('Current time:', c_time)
print()

if confirm == 0:
    print('Confirmed...\n')
    print('*System Exit*')
elif confirm == 1:
    print('Confirmed...\n')
    get_new_log(input('(Enter) New Log -> '))
elif confirm == 2:
    print('Confirmed...\n')
    access_date = input('(Enter) Log Date -> ')
    read_old_logs(access_date)
else:
    print('Invalid Input...\n')