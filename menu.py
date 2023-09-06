def get_data():
    text = 'Please enter the data to create qrcode! (b for back)'.title()
    
    draw_box(text=text)
    data = input('>> ')
    
    while not data:
        wrong_input()
        draw_box(text=text)
        data = input('>> ')
    return data


def draw_box(text: str):
    from os import system
    
    seperator = '=' * (len(text) + 36 )
    seperator_beg = '||'
    text = '||' + (' ' * 16) + text + (' ' * 16) + '||'
    
    system('cls')
    print(seperator)
    print(text)
    print(seperator)

def wrong_input(text='Wrong input, try again!'.title()):
    from os import system
    from time import sleep
    
    system('cls')
    draw_box(text.title())
    sleep(2)
    system('cls')
    
    
def menu_selector():
    text = 'Read or Create or Exit?! (r/c/e)'
    
    draw_box(text=text)
    _ans = input('>> ')
    
    while _ans not in ['r', 'R', 'c', 'C', 'e', 'E']:
        wrong_input()
        draw_box(text=text)
        _ans = input('>> ')
    return _ans.lower()
    
    
def get_file_address():
    from os.path import exists
    text = 'Please enter the address to read qrcode! (b for back)'.title()
    
    draw_box(text=text)
    address = input('>> ')
    
    while not exists(address):
        wrong_input('File not found!')
        draw_box(text=text)
        address = input('>> ')
    return address

def press_any_key():
    text = 'Press any key to continue...'
    from time import sleep
    sleep(2)
    input(text)