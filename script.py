import time

confirm = int(input())

if confirm == 1:
    print('Confirmed...')
    time.sleep(0.1)
    print('Starting...')
else:
    print('System exit')

