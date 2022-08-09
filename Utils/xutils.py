import os
import platform
import time


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def wait():
    time.sleep(1.8)



#def join_data_to_dictionary():


