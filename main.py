from qr import create_qr_code, read_qr_code
from util import save_to_file, show_image
from menu import get_data, menu_selector, get_file_address, press_any_key

if __name__ == '__main__':
    while True:
        _choice = menu_selector()
        
        # create
        while _choice == 'c':
            link = get_data()
            
            if link.lower() == 'b':
                _choice = None
                break
            
            img = create_qr_code(link=link)
            if img:
                save_to_file(img)
                show_image(img)
                press_any_key()
                _choice = None
        
        # read
        while _choice == 'r':
            address = get_file_address()
            if address.lower() == 'b':
                _choice = None
                break
            read_qr_code(address)
            press_any_key()
            _choice = None
            
        # exit
        if _choice == 'e':
            break
        