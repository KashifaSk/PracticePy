from time import sleep

def is_windows():
    sleep(5)
    print('Windows')
    return True

def get_op_sys():
    return 'Windows' if is_windows()==True else 'Linux'


