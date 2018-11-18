#import serial
#ser = serial.Serial('/dev/ttyUSB0')
#print(ser.name)
#ser.write(b'hello')
#ser.close()



import serial.tools.list_ports as port_list
import serial
import _thread


#multithread to detect the status of the serial communication
def thread_serial_auto(a):
    p = []
    a = ""
    serial_state = 0
    ports = list(port_list.comports())
    for p in ports: print(p[0])
    try:
        a = p[0]
    except:
        pass
    
    while 1:
        if(serial_state == 0):
            a = ""
           # print("a")
        ports = list(port_list.comports())
        #print(ports)
        for p in ports: pass
        try:
            a = p[0]
        except:
            pass
        
        if(ports != []):
            
            if(serial_state == 1):
                init_serial()
                serial_state = 0
            
        else:
      
            if(serial_state == 0):
                #do sth
                
                print("normal state")
                serial_state = 1
        
    print("hello")


#testing serial communication as well as
def init_serial():
    
    global ser
    ser = serial.Serial()
    ser.baudrate = 115200
    ports = list(port_list.comports())
    if not ports:
        print('no device plugged in')
    else:
        for p in ports: print(p[0])
        ser.port = p[0]
        ser.open()
        x = b"\x16\x16\x16\x16\x16"
        #x = len(array)
        print(x[0])
        if ser.isOpen():
            print('open: ')    
            ser.write(b"\x16\x16\x16\x16\x16")
    ser.close()
            


#def detect_serial():

try:
    a = 1
    b = 2
    _thread.start_new_thread(thread_serial_auto,(a,))
except:
    print("asdfsadf")


while 1:
    pass
    



#try:
#    while 1:
#        bytes = ser.readline()
#        print('You sent: ' + bytes)
#        break
#except KeyboardInterrupt:
#    print('interrupted')


#ports = list(port_list.comports())
#for p in ports: print(p)
