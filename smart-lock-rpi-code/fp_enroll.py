import time
import logout_fingerprint
import adafruit_fingerprint
from adafruit_fingerprint import Adafruit_Fingerprint
import serial


uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
uart1 = serial.Serial("/dev/ttyUSB1", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
finger1 = adafruit_fingerprint.Adafruit_Fingerprint(uart1)
#######################
def enroll_finger2(location, char_list):
        
    adafruit_fingerprint.Adafruit_Fingerprint.send_fpdata(self = finger1,data = char_list, slot = 2)
    adafruit_fingerprint.Adafruit_Fingerprint.send_fpdata(self = finger1,data =char_list, slot = 1)
    
    print("Creating model...2", end="")
    i = finger1.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created2")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match2")
        else:
            print("Other error2")
        return False

    print("Storing model #%d...2222" % location, end="")
    i = finger1.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("second finger Stored2")
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location2")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error2")
        else:
            print("Other error2")
        return False

    return True



#######################
def enroll_finger(location):
    """Take a 2 finger images and template it, then store in 'location'"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                print("Image too messy")
            elif i == adafruit_fingerprint.FEATUREFAIL:
                print("Could not identify features")
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while i != adafruit_fingerprint.NOFINGER:
                i = finger.get_image()

    print("Creating model...", end="")
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        enroll_finger(location)

    print("Storing model #%d..." % location, end="")
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("first finger Stored")
        char_list = adafruit_fingerprint.Adafruit_Fingerprint.get_fpdata(self =finger,slot = 1)
        print(char_list)
        enroll_finger2(location, char_list)
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return False
    
    return True
#enroll_finger(1)

##############   DELETING FINGERPRINT OF A USER ########################
def delete_fp(location):
    if finger.delete_model(location) == adafruit_fingerprint.OK:
            if finger1.delete_model(location) == adafruit_fingerprint.OK:
                print('fp successfully deleted')
                return True
            else:
                print("Failed to delete logout fp")
                return False
    else:
        print("Failed to delete login fp")
        return False
# enroll_finger(6)