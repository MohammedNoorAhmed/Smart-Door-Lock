# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import adafruit_fingerprint
from adafruit_fingerprint import Adafruit_Fingerprint
import serial
uart = serial.Serial("/dev/ttyUSB1", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

##################################################





# pylint: disable=too-many-statements
def enroll_finger2(location,temp_list1,temp_list2):
    """Take a 2 finger images and template it, then store in 'location'"""
    Adafruit_Fingerprint.send_fpdata(finger,temp_list1, "char",1)
    Adafruit_Fingerprint.send_fpdata(finger,temp_list2,"char", 2)
    print(Adafruit_Fingerprint.get_fpdata(finger, "char",1))
    print(Adafruit_Fingerprint.get_fpdata(finger,"char", 2))
    print("in fs 2")
    print(temp_list1)
    print(temp_list2)

    print("Creating model...", end="")
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return False

    print("Storing model #%d..." % location, end="")
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("Stored")
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return False

    return True


##################################################


def get_num():
    """Use input() to get a valid number from 1 to 127. Retry till success!"""
    i = 0
    while (i > 127) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-127: "))
        except ValueError:
            pass
    return i






