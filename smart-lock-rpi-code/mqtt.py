import paho.mqtt.client as mqtt
import time
import json
import adduser
import os
import del_user
import lock
import userdb
import mail
import doorFeedback


def userexists(username):
    parentdir = r'/home/pi/facial-recognition-main/dataset'
    path = os.path.join(parentdir, username)
    return os.path.exists(path)
def on_log(client, userdata, level, buf):
    print("log: ",+buf)
    
def on_message(client, userdata,msg):
    m_decode = str(msg.payload.decode("utf-8","ignore"))
    m_json = json.loads(m_decode)
    print(m_json)
    
    op = m_json['operation']
    #time.sleep(2)
    
    if op =='adduser':
        username  = m_json['name']
        empId = m_json['empId']
        if userexists(username):
            #no enrollment
            print('user already exists')
        else :
            #enrollment
            adduser.enroll_new_user(username,empId)
            
    elif op == 'deluser':
        username  = m_json['name']
        empId = m_json['empId']
        #delete a user
        if userexists(username):
            del_user.delete_dataset(username,empId)
        
        
    elif op == 'doorOpen':
        print('Door operation')
        
        username  = m_json['name']
        optime = m_json['ctime']/1000
        doortime = time.time()
        if(optime +5 > doortime):
            print("Opening the door")
            lock.doorunlock()
            userdb.admin_entry(username)
            while True:
                print("Door is open...")
                mail.send_mail(username,'who did not close the door after using')
                if(doorFeedback.feedback()==True):
                    print("Door is closed....")
                    break
        else:
            print('time over')
        
        
        
        #print(time.time())
#         lock.doorunlock()
#         userdb.admin_entry(username)
    else:
        print('no operation')
        
        
         
     
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK rc = ",str(rc)," flags = ",str(flags))
        
    else:
        print("Bad connection returned code : ",rc)
        
def on_disconnect(client, userdata, flags, rc=0):
    print("disconnected result code:" +str(rc))
    

def connect_admin():
    
    broker_address='172.20.10.4'
    client = mqtt.Client('lkjui',transport='websockets') #create new instance
    client.on_connect = on_connect
    #client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.on_message = on_message

    print("connecting to broker ",broker_address)
    client.username_pw_set("mna","mna0845")
    client.connect(broker_address,1901,150)#connect to broker
    client.loop_start()
    client.subscribe("admin",1,True)
    time.sleep(0.1)
    client.loop_stop()
    client.disconnect()
#connect_admin()
