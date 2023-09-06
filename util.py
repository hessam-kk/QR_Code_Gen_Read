def save_to_file(img):
    _want_save = input('Do you want to save to a file? (y/n) \n>> ')
    while _want_save not in ['y', 'n', 'Y', 'N']:
        print('wrong input, try again!')
        _want_save = input('Do you want to save to a file? (y/n) \n>> ')
    if _want_save in ['y', 'Y']:
        file_name = input('Please enter file name!\n>> ')
        while not file_name:
            print('wrong input, try again!')
            file_name = input('Please enter file name!\n>> ')
        img.save('{}.png'.format(file_name))


def show_image(img):
    _want_show = input('Do you want to open the created qrcode? \n>> ')
    while _want_show not in ['y', 'n', 'Y', 'N']:
        print('Wrong input, try again!')
        _want_show = input('Do you want to open the created qrcode? \n>> ')

    if _want_show in ['y', 'Y']:
        img.show()
