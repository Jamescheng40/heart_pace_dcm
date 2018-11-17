#import serial
#ser = serial.Serial('/dev/ttyUSB0')
#print(ser.name)
#ser.write(b'hello')
#ser.close()



import serial.tools.list_ports as port_list
import serial
import thread


def init_serial():

    #
    
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ports = list(port_list.comports())
    if not ports:
        print('not logged in')
    else:
        for p in ports: print(p[0])
        ser.port = p[0]
        ser.open()
        if ser.isOpen():
            print('open: ')    
            ser.write(b'adf')
    



#def detect_serial():


init_serial()



#try:
#    while 1:
#        bytes = ser.readline()
#        print('You sent: ' + bytes)
#        break
#except KeyboardInterrupt:
#    print('interrupted')


#ports = list(port_list.comports())
#for p in ports: print(p)
