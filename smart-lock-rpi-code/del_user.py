import os
import shutil
import fp_enroll
import userdb
import time
import lcd_display
import WWrite
import train_model

def delete_db(fpDeleted,username,empId):
    if fpDeleted:
        lcd_display.display_msg('    FINGERPRINT  ',' DELETED ')
        time.sleep(0.5)
        userdb.delete_entry(empId)
        lcd_display.display_msg(f'ALL DATA OF ',f'{username} DELETED')
        time.sleep(0.5)

# deleting a user photos dataset
def delete_dataset(username,empId):
    time.sleep(2)
    parentdir = "/home/pi/facial-recognition-main/dataset/"
    path = os.path.join(parentdir,username)
#     try:
    shutil.rmtree(path)
    lcd_display.display_msg(f'PHOTOSET OF ',f'{username} DELETED')
    time.sleep(0.5)
    print("% s removed successfully" % path)
    train_model.delmodel(username)
    time.sleep(0.5)
    lcd_display.display_msg('  PLACE YOUR    ','  RFID CARD  ')
    WWrite.delRFID()
    lcd_display.display_msg('   RFID   ','  UNREGISTERED  ')
    fpDeleted = fp_enroll.delete_fp(empId)
    delete_db(fpDeleted,username,empId)
      
#     except OSError as error:
#         print(error)
#         print("File path can not be removed")
        
#delete_dataset('modi',6)