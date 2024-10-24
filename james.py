# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# for o in range(5):
#     for i in range(5):
#         print(f'outer value: {o} inner value: {i}')
#     print('')

# import datetime as dt
# tries = 3
# enter = False
# n = dt.datetime.now()
# d = n.strftime('%A %d %B %Y')
# t = n.strftime('%X')

# while tries >= 1: 
#     user = input('enter username: ')
#     pw = input('enter password: ')

#     if user == 'admin' and pw == 'password':
#         print(f"\nwelcome, 'admin'")
#         while True:
#                 action = input("\ntype 'date' to see the date and 'exit' to exit: ")
#                 if action == 'date':
#                     print(f'\nthe date is {d} and the time is {t}')
#                     break
#                 elif action == 'exit':
#                     print('goodbye')
#                     exit()
#                 else:
#                     print('invalid')
#                     continue
#     else:
#         print('\ninvalid\n')
#         tries -= 1
#         continue

# if tries == 0:
#     print('all attempts used')
#     exit()

def menu():
    global f
    global r
    global enter
    fname = input('enter file name: ')
    fname = fname + '.txt'
    menudecr = '''
    01 - Create a file
    02 - Read a file
    03 - Write to a file
    04 - Append a file
    05 - Exit
    '''
    print(menudecr)
    while True:
        try:
            x = int(input('enter a number: '))
        except ValueError:
            print('invalid')
            continue
        
        if x == 1:
            try:
                f = open(fname, 'a')
                print('file created successfully')
            except FileExistsError:
                print('file already exists')

        elif x == 2:
            try:
                with open(fname, 'r') as f:
                    r = f.read()
            except FileNotFoundError:
                print('file does not exist')
            if r == '':
                print('file is empty')
            else:
                print(r)
        
        elif x == 3:
            enter = input('type something: ')
            with open(fname, 'w') as f:
                f.write(enter)
            print('file overwritten successfully')
        
        elif x == 4:
            enter = input('type something: ')
            with open(fname, 'a') as f:
                f.write(enter)
            print('file appended successfully')
        
        elif x == 5:
            print('goodbye')
            exit()
        
        else:
            print('please enter a valid integer')
            continue
menu()
