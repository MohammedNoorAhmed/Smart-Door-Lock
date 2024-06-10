import faceRecog
import RRead
import time
import lock
import userdb
import find_fingerprint
import exitfp
import lcd_display as lcd
import mqtt
import mail
import doorFeedback

while True:
#    lock.doorlock()
    authorizeduser =''
    authname = ''
    num = 0
    mqtt.connect_admin()
    msg = 'Trying to Access the door without Loging out '
    
    ####################  EXIT FP CODE    #######################
    if num == 0:
        exitempid= exitfp.get_fingerprint()

        if exitempid == None:
            lcd.display_msg('USER NOT FOUND ','   ACCESS DENIED!!  ')
            time.sleep(1.5)
            pass
        elif exitempid == 'none':
            pass
        else :
            st = time.time()
            username=userdb.get_empname(exitempid)
            exit = userdb.logout_entry(username)
            if exit == True:
                lock.doorunlock()
                print(time.time()-st)
                if(doorFeedback.feedback()==True):
                    print("Door is closed....")
            
                    continue
            
                else:
                    while True:
                        print("Door is open...")
                        if(doorFeedback.feedback()==True):
                            print("Door is closed....")
                            break
                
                time.sleep(4)
            else:
                print('unable to open the door')
        num = 1

    ####################    EXIT CODE END     ###################
    
    rfid,rfid_username = RRead.readRfid()
    username = rfid_username
    lcd.display_msg('USE RFID CARD ','  OR  BIOMETRIC   ')
    if rfid_username != 'none' :
        print(rfid_username)
        if userdb.login_check(rfid_username):
                lcd.display_msg('  user already  ','   inside    ')
                mail.send_mail(rfid_username,msg)
                continue
        user_auth = userdb.get_rfid(rfid)
        if user_auth == rfid_username:
            print('please look in the camera')
            lcd.display_msg('PLEASE LOOK IN  ','   THE CAMERA')
            time.sleep(1.5)
            try:
                (authorizeduser,authname) = faceRecog.Face(user_auth)
                print(authname)
                num = 0
            except TypeError:
                num = 0
                continue
        else:
            lcd.display_msg('  INVALID RFID  ','   ACCESS DENIED!!  ')
            time.sleep(1.5)
            #print(authorizeduser)
            num = 0
            
    else:    
        empid= find_fingerprint.get_fingerprint()

        if empid == None:
            lcd.display_msg('USER NOT FOUND ','   ACCESS DENIED!!  ')
            time.sleep(1.5)
            num = 0
            continue
        elif empid == 'none':
            num = 0
            continue
        else :
            
            username=userdb.get_empname(empid)
            if userdb.login_check(username):
                lcd.display_msg('  USER ALREADY  ','   INSIDE    ')
                mail.send_mail(username,msg)
                continue
            print(username)
            num = 0
            if username == None:
                num = 0
                continue
            try:
                lcd.display_msg('PLEASE LOOK IN  ','   THE CAMERA')
                authorizeduser,authname = faceRecog.Face(username)
                print(authname)
                num = 0
            except TypeError:
                num = 0
                continue
            

        
        
    if authorizeduser == False:
            print("Face not match!! Access denied")
            lcd.display_msg('FACE NOT MATCHED ','  ACCESS DENIED!')
            time.sleep(1.5)
            
    
    elif authorizeduser == '':
        print('empty ')
        
    else:    
        print('Access granted')
        lcd.display_msg('FACE MATCHED ',' ACCESS GRANTED! ')
        st = time.time()
        imgUrl=userdb.uploadImage(authname,authname,authorizeduser)
        print(imgUrl)
        userdb.login_entry(authname,imgUrl)
        print('time to upload on db: ', time.time()-st)
        #print("door unlocks...")
        
        lock.doorunlock()
        if(doorFeedback.feedback()==True):
            print("Door is closed....")
            
            continue
            
        else:
            
            while True:
                print("Door is open...")
                mail.send_mail(username,'who did not close the door after using')
                if(doorFeedback.feedback()==True):
                    print("Door is closed....")
                    break
               
                    
                
                    
            
            
            
            #Email..
            #buzzer
            #if(doorFeedback.feedback(2)==True):
           
        

