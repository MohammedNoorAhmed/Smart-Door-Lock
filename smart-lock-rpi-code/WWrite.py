#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import userdb
reader = SimpleMFRC522()

def writeRFID(uname):
    
    try:
            print("Now place your tag to write")
            id,text = reader.read()
#             if rfid_exists(config.db,id):
            print('first', id, text)
            reader.write(uname)
            print("Written")
            return True, id
#             else :
#                 return False
#             id,text = reader.read()
#             print('id :', id)
#             print('text:', text)
    finally:
            GPIO.cleanup()
            
def delRFID():
    
    try:
            print("Now place your tag to write")
#             id,text = reader.read()
# #             if rfid_exists(config.db,id):
#             print('first', id, text)
            reader.write("")
            print("Rfid unregistered")
            return True
    finally:
            GPIO.cleanup()


#writeRFID("mustafa")
