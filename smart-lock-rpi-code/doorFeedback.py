import RPi.GPIO as gpio
import time

def feedback():
    gpio.setmode(gpio.BOARD)#
    gpio.setup(8,gpio.IN)
    gpio.setup(33,gpio.OUT)

    irlist = [1,0,1,0,1]
    Rlist=[]
    x = 1
#     if order == 1:
#         x = 1
#     else:
#         infinite = True
    gpio.output(33,gpio.LOW)
    st = time.time()
    while x < 13 :
        for y in irlist:
            if y == 1:
                gpio.output(33,gpio.HIGH)
                time.sleep(0.1)
                if gpio.input(8)==0:
                    gpio.output(33,gpio.LOW)
                    #print("object detected")
                    time.sleep(0.1)
                    Rlist.append(1)
                else:
                    gpio.output(33,gpio.LOW)
                    Rlist.append(0)
                time.sleep(0.2)   
            else:
                Rlist.append(0)
                #print("no object detected")
                #time.sleep(1)
                #continue
        print(Rlist)
        if Rlist == irlist:
            gpio.cleanup()
            print('if true  ', time.time()-st)
            return True
        Rlist=[]
        x = x + 1
    gpio.cleanup()
    print('if true  ', time.time()-st)
    return False
    
            #time.sleep(0.1)
#feedback() 
#print(feedback())
#gpio.cleanup()