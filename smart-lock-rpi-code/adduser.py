import headshots as hs
import train_model as tm
import fp_enroll as fp
import enrollRFID
import userdb
import lcd_display 
import del_user


def enroll_new_user(uname,empId):
    lcd_display.display_msg('CREATING DATASET',' TAP RFID CARD')
    
    rfidRegistered,rfid= enrollRFID.writeRFID(uname)
    if rfidRegistered == True:
        lcd_display.display_msg('CREATING DATASET','PLACE THE FINGER')
        if fp.enroll_finger(empId):
            lcd_display.display_msg('CREATING DATASET','LOOK IN CAMERA')
            
            if hs.headshots(uname):
                lcd_display.display_msg('    TRAINING    ','   THE MODEL.....')
                if tm.trainmodel(uname):
                    #create a profile in userdb
                    
                    userdb.enroll(uname,empId,rfid)
                    lcd_display.display_msg(f'  {uname}  ','  REGISTERED  ')
                else :
                    print('train error')
                    del_user.delete_dataset(uname,empId)
                    
            else :
                del_user.delete_dataset(uname,empId)
                print('dataset error')
        else :
            del_user.delete_dataset(uname,empId)
            print('fp error')
    else :
        del_user.delete_dataset(uname,empId)  
        print('rfid error')