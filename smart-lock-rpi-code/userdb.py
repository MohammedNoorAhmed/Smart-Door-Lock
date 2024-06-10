import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
from datetime import date
from firebase_admin import storage
from firebase_admin.firestore import SERVER_TIMESTAMP

path = '/home/pi/facial-recognition-main/db/user-login-register-firebase.json'

if not firebase_admin._apps:
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred, {'storageBucket': 'user-login-register-d16ab.appspot.com'})
    db = firestore.client()

def enroll(name,empId,rfid):
    
    data = {'name':name,'empId':empId,'rfid':rfid}
    db.collection(u'Profiles').add(data)
    bucket = storage.bucket(name)

def delete_entry(empId):
    docs = db.collection(u'Profiles').where(u'empId',u'==',empId).get()
    for doc in docs:
        if doc.exists:
            docid= doc.id
            print(docid)
            db.collection(u'Profiles').document(docid).delete()
        else:
            print('not exists')
def delete_admin_entry():
    name = 'ADMIN shoaib'
    docs = db.collection(u'user-login-details').where(u'name',u'==',name).get()
    for doc in docs:
        if doc.exists:
            docid= doc.id
            print(docid)
            db.collection(u'user-login-details').document(docid).delete()
            print('deleted')
        else:
            print('not exists')
def user_exists(empId):
    count = db.collection(u'Profiles').where(u'empId', '==' ,empId ).count()
    if count :
        return True
    else:
        return False 
        
def get_empname(empId):
    docs= db.collection(u'Profiles').where(u'empId',u'==',empId).get()#returns list of dictionaries
    for doc in docs:
        if doc.exists:
            result=doc.to_dict()
            return  result['name']

def get_rfid(rfid):
    docs=db.collection(u'Profiles').where(u'rfid',u'==',rfid).get()
    for doc in docs:
        if doc.exists:
            result=doc.to_dict()
            print("from db :" , result['name'])
            return  result['name']
        else:
            return False
def rfid_exists(rfid):
    docs=db.collection(u'Profiles').where(u'rfid',u'==',rfid).get()
    for doc in docs:
        if doc.exists:
            return True
        else:
            return False  
        
def readdb():
    docs = db.collection('Profiles').stream()
    for doc in docs:
        print(doc.to_dict())

# def initializeDB(path):
#     if not firebase_admin._apps:
#         cred = credentials.Certificate(path)
#         firebase_admin.initialize_app(cred, {'storageBucket': 'user-login-register-d16ab.appspot.com'})
#         db = firestore.client()
#         return db

def login_entry(name,image_url):
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", t)
    current_date = today.strftime("%d-%b-%Y")
    data={
        u'name':name,
        u'login_time':current_time,
        u'date':current_date,
        u'image':image_url,
        u'logout_time': '',
        u'filter_date': SERVER_TIMESTAMP
    }
    db.collection(u'user-login-details').document().set(data)
def admin_entry(name):
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", t)
    current_date = today.strftime("%d-%b-%Y")
    data={
        u'name':'ADMIN '+name,
        u'login_time':current_time,
        u'date':current_date,
        #u'image':image_url,
        #u'logout_time': '',
        u'filter_date': SERVER_TIMESTAMP
    }
    db.collection(u'user-login-details').document().set(data)

def logout_entry(username):
    docs = db.collection('user-login-details').where(u'name', '==', username).where(u'logout_time','==', '').get()
    for doc in docs:
        if doc.exists:
            t = time.localtime()
            current_time = time.strftime("%I:%M:%S %p", t)
            db.collection('user-login-details').document(doc.id).update({u'logout_time':current_time})
            return True
        else:
            return False

def login_check(username):
    docs = db.collection('user-login-details').where(u'name', '==', username).where(u'logout_time','==', '').get()
    for doc in docs:
        if doc.exists:
            return True
        else:
            return False
        

def uploadImage(folder,cloudFilename,imgbuf):
    cloudFilename = cloudFilename + str(time.time())
    bucket = storage.bucket()
    blob = bucket.blob(folder+'/'+cloudFilename+'.png')
    blob.upload_from_string(imgbuf,content_type='image/png')
    blob.make_public()
    url = blob._get_download_url(None)
    # print(url)
    return url
#admin_entry('shoaib')
#delete_admin_entry()
