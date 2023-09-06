def create_qr_code(link: str):
    # import & install required libraries
    import importlib.util  # to check if qrcode library is installed
    from os import system  # to auto install qrcode library

    package_name = 'qrcode'
    if importlib.util.find_spec(package_name) is None:  # search for package
        print("{} is not installed".format(package_name))

        # attempt to install
        if system('pip install {}'.format(package_name)) == 0:  # installed successfully
            print("package {} installed succressfully!".format(package_name))

        else:  # error on install
            print('could not install {} package!'.format(package_name))
            return None

    # start the process
    import qrcode

    qr = qrcode.QRCode(
        version=1.,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(
        fill_color="black",
        back_color="white")

    show_in_terminal(qr)
    return img


def show_in_terminal(qr):
    import io
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print('{}'.format(f.read()))


def read_qr_code(file_address: str):
    import importlib.util  # to check if qrcode library is installed
    from os import system  # to auto install qrcode library
    package_name = 'opencv-python'
    
    if importlib.util.find_spec('cv2') is None:  # search for package
        print("{} is not installed".format('cv2'))

        # attempt to install
        if system('pip install {}'.format(package_name)) == 0:  # installed successfully
            print("package {} installed succressfully!".format(package_name))

        else:  # error on install
            print('could not install {} package!'.format(package_name))
            return None

    from os.path import exists
    from time import sleep
    if file_address == 'b':
        return
    
    from cv2 import imread, QRCodeDetector
    img = imread(file_address)
    detector = QRCodeDetector()
    link, _, _ = detector.detectAndDecode(img)

    create_qr_code(link) # to show in terminal
    print('your data is: \n\t{}'.format(link))
