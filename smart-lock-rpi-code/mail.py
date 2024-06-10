import yagmail
import time
from datetime import date


def send_mail(username,msg):
    t = time.localtime()
    mailtime = time.strftime("%I:%M:%S %p", t)
    today = date.today()
    current_date = today.strftime("%d-%b-%Y")
    mailId = yagmail.SMTP('smartlocka39@gmail.com')
    to1 = 'noormohd0845@gmail.com'
    to2= 'shoaib733021@gmail.com'
    to3= 'hussainmohammadmustafa@gmail.com'
    #to = 'shoaib.ahmed011521@gmail.com'
    sub = 'SUSPICIOUS ACTIVITY'
    body =f"ALERT!!!! Malicious activity detected from {username}, {msg} at {current_date}, {mailtime}"
    mailId.send(to1,sub,body)
    mailId.send(to2,sub,body)
    mailId.send(to3,sub,body)
#send_mail('shoaib')
#send_mail("Noor","who did not close the door after using")   