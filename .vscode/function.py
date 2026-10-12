from time import sleep

def welcome_message(title):
    style = "*" * (len(title) + 8)
    print(style)
    print(f'*** {title} ***')
    print(style)

def exit_message():
    print('Program akan dihentikan...')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program dihentikan. Terima kasih!')