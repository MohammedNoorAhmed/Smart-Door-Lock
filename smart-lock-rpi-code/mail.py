import yagmail

def send_mail(username,msg):
    mailId = yagmail.SMTP('smartlocka39@gmail.com')
    to1 = 'noormohd0845@gmail.com'
    to2= 'shoaib733021@gmail.com'
    sub = 'SUSPICIOUS ACTIVITY'
    body =f"ALERT!!!! malicious activity detected from {username},...."+msg
    mailId.send(to1,sub,body)
    mailId.send(to2,sub,body)