import datetime
import time
# import pandas as pd

def get_log(input):
    if input != '':
        print('')
        print('Log Accepted')
        return input
    else:
        print('Log Failed')
        return False

print('Exit -> 0')
print('Enter Log -> 1')
print('Access Previous Logs -> 2\n')

confirm = int(input())
# prev_data = pd.read_csv('../Journal/log_data.csv')

current_date = datetime.date.today().strftime('%B %d, %Y')
current_time = time.strftime("%H:%M:%S", time.localtime())

c_time = str(current_time) + ' - ' + str(current_date)

print('='*50)
print('Current time =', c_time)
print()
# print(prev_data)

if confirm == 0:
    print('System Exit')
elif confirm == 1:
    print('Confirmed...')
    time.sleep(0.5)
    print('Starting...')
    get_log(input('Enter Log: '))
else:
    log_date_access = input('Enter log date: ')
    print(log_date_access)

