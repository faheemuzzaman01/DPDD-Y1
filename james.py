# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# for o in range(5):
#     for i in range(5):
#         print(f'outer value: {o} inner value: {i}')
#     print('')

import datetime as dt
tries = 3
enter = False
n = dt.datetime.now()
d = n.strftime('%A %d %B %Y')
t = n.strftime('%X')

while tries >= 1: 
    user = input('enter username: ')
    pw = input('enter password: ')

    if user == 'admin' and pw == 'password':
        print(f"\nwelcome, 'admin'")
        while True:
                action = input("\ntype 'date' to see the date and 'exit' to exit: ")
                if action == 'date':
                    print(f'\nthe date is {d} and the time is {t}')
                    break
                elif action == 'exit':
                    print('goodbye')
                    exit()
                else:
                    print('invalid')
                    continue
    else:
        print('\ninvalid\n')
        tries -= 1
        continue

if tries == 0:
    print('all attempts used')
    exit()