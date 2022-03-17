import datetime
import time
import pandas as pd
from read_message import encrypt, decrypt

log_storage = pd.read_csv('./Notes/stored_logs.csv')

current_date = datetime.date.today().strftime('%B %d, %Y')
current_time = time.strftime("%H:%M:%S", time.localtime())
c_time = str(current_time) + ' - ' + str(current_date)

def get_new_log(input):
    if input != '':
        encryption = encrypt(input)
        log_storage.append({'Date': str(current_date), 'Time': str(current_time), 'Content': encryption[0], 'Code': encryption[1]}, ignore_index=True).to_csv('./Notes/stored_logs.csv', index=False)
        
        print(f'\n*Log Accepted*\n{encryption}')
        return encryption
    else:
        return '\n*Log Failed*'

def read_old_logs(date):
    if len(log_storage[log_storage['Date'] == date]) == 0:
        print('\n*No Such Logs*')
    else:
        print('\n*Log(s) Accessed*\n')
        for i in range(len(log_storage[log_storage['Date'] == date])):
            original_text = decrypt(log_storage[log_storage['Date'] == date]['Content'].iloc[i], str(log_storage[log_storage['Date'] == date]['Code'].iloc[i]))
            print(f'#{i+1} {original_text}')
    return True

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
else:
    access_date = input('(Enter) Log Date -> ')
    read_old_logs(access_date)