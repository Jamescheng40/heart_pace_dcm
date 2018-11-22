from tkinter import *

from tkinter import messagebox
import serial.tools.list_ports as port_list
import serial
import _thread
import threading
import queue
import time, threading
import locale

class Window(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.b = 0
        self.tempname=""
        self.name="Z:/filename.txt"
        self.init_window()
        self.variable = ""
        self.p_state = 0
        self.pro_array = []
        self.mode_state = 0
        self.ser = serial.Serial()

## wasted testing garbage
        #self.queue1 = queue.Queue()
       # ThreadedTask(self.queue1).start()
       # self.master.after(100, self.process_queue)
        #messagebox.showinfo('Message','Invalid input for amplitude')
       # try:
       #     r = 1
        #    _thread.start_new_thread(self.thread_serial_auto,(r,))
       # except:
        #    print("asdfsadf")
        
##
##    def process_queue(self):
##        try:
##            msg = self.queue1.get(0)
##
##        except queue.Empty:
##            self.master.after(100, self.process_queue)
##        


    #Creation of init_window12345678990
        
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welcome")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        binit = Label(self, text="Please register before you log in")
        binit.place(x=30,y=30)

        

       
##         old 
##        #initializing serial communication
##        def init_serial():
##
##            global ser
##            ser = serial.Serial()
##            ser.baudrate = 9600
##            ports = list(port_list.comports())
##            if not ports:
##                print('no device plugged in')
##            else:
##                for p in ports: print(p[0])
##                ser.port = p[0]
##                ser.open()
##                if ser.isOpen():
##                    print('open: ')    
##                    ser.write(b'adf')



        def save():
            
            outname=self.name.replace("filename",self.tempname)
            f=open(outname,"w")
                
            if (self.variable.get()=="AOO"):
                if locale.atof(self.sub2.sub.e3.get())>175 or locale.atof(self.sub2.sub.e3.get())<50:
                    messagebox.showinfo('Message','Invalid input for upper rate limit\nshould be in the range 50-175ppm')
                    return
                if locale.atof(self.sub2.sub.e4.get())>175 or locale.atof(self.sub2.sub.e4.get())<30:
                    messagebox.showinfo('Message','Invalid input for lower rate limit\nshould be in the rannge 30-175ppm')
                    return
                if locale.atof(self.sub2.sub.e5.get())>3.2 or locale.atof(self.sub2.sub.e5.get())<0.5:
                    messagebox.showinfo('Message','Invalid input for atrial amplitude\nshould be in the range 0.5-3.2V ')
                    return
                if locale.atof(self.sub2.sub.e6.get()) !=0.05:
                    messagebox.showinfo('Message','Invalid input for atrial pulse width\n should be 0.05ms')
                    return
                
                f.write("0\t0\t")
                f.write(self.sub2.sub.e3.get())
                f.write("\t")
                f.write(self.sub2.sub.e4.get())
                f.write("\t")
                f.write(self.sub2.sub.e5.get())
                f.write("\t")
                f.write(self.sub2.sub.e6.get())
                f.write("\t")
                f.write("0\t0\t0\t0\t0\t0\t0")
                f.close()
                messagebox.showinfo('Message','Settings saved')
                
            if (self.variable.get()=="AAI"):
                if locale.atof(self.sub2.sub.e3.get())>175 or locale.atof(self.sub2.sub.e3.get())<50:
                    messagebox.showinfo('Message','Invalid input for upper rate limit\nshould be in the range 50-175ppm')
                    return
                if locale.atof(self.sub2.sub.e4.get())>175 or locale.atof(self.sub2.sub.e4.get())<30:
                    messagebox.showinfo('Message','Invalid input for lower rate limit\nshould be in the rannge 30-175ppm')
                    return
                if locale.atof(self.sub2.sub.e5.get())>3.2 or locale.atof(self.sub2.sub.e5.get())<0.5:
                    messagebox.showinfo('Message','Invalid input for atrial amplitude\nshould be in the range 0.5-3.2V ')
                    return
                if locale.atof(self.sub2.sub.e6.get()) !=0.05:
                    messagebox.showinfo('Message','Invalid input for atrial pulse width\n should be 0.05ms')
                    return
                if locale.atof(self.sub2.sub.e7.get())>10 or locale.atof(self.sub2.sub.e7.get())<1:
                    messagebox.showinfo('Message','Invalid input for ventricular sensitivity\nshould be in the rage 1.0-10.0mV')
                    return
                if locale.atof(self.sub2.sub.e10.get())>500 or locale.atof(self.sub2.sub.e10.get())<150:
                    messagebox.showinfo('Message','Invalid input for ARP\nshould be in range 150-500ms')
                    return
                if locale.atof(self.sub2.sub.e11.get())>500 or locale.atof(self.sub2.sub.e11.get())<150:
                    messagebox.showinfo('Message','Invalid input for PVARP\nshould be in range 150-500ms')
                    return
                if locale.atof(self.sub2.sub.e12.get())!=locale.atof(self.sub2.sub.e4.get()):
                    messagebox.showinfo('Message','Invalid input for hysteresis\nshould be the same with lower rate limit')
                    return
                entry13=locale.atof(self.sub2.sub,e13.get())
                if entry13!=0 and entry13!=3 and entry13!=6 and entry13!=9 and entry13!=12 and entry13!=15 and entry13!=18 and entry13!=21:
                    messagebox.showinfo('Message','Invalid input for rate smoothing\nshould be one number of 0,3,6,9,12,15,18,21')
                    return
                f.write("0\t0\t")
                f.write(self.sub2.sub.e3.get())
                f.write("\t")
                f.write(self.sub2.sub.e4.get())
                f.write("\t")
                f.write(self.sub2.sub.e5.get())
                f.write("\t")
                f.write(self.sub2.sub.e6.get())
                f.write("\t")
                f.write(self.sub2.sub.e7.get())
                f.write("\t")
                f.write(self.sub2.sub.e10.get())
                f.write("\t")
                f.write(self.sub2.sub.e11.get())
                f.write("\t")
                f.write(self.sub2.sub.e12.get())
                f.write("\t")
                f.write(self.sub2.sub.e13.get())
                f.close()
                messagebox.showinfo('Message','Settings saved')
                
            if (self.variable.get()=="VOO"):
                if locale.atof(self.sub2.sub.e1.get())>7 or locale.atof(self.sub2.sub.e1.get())<3.5:
                    messagebox.showinfo('Message','Invalid input for ventricular amplitude\nshould be in the range 3.5-7.0V')
                    return
                if locale.atof(self.sub2.sub.e2.get())>1.9 or locale.atof(self.sub2.sub.e2.get())<0.1:
                    messagebox.showinfo('Message','Invalid input for ventricular pulse width\nshould be in the range 0.1-1.9ms')
                    return
                if locale.atof(self.sub2.sub.e3.get())>175 or locale.atof(self.sub2.sub.e3.get())<50:
                    messagebox.showinfo('Message','Invalid input for upper rate limit\nshould be in the range 50-175ppm')
                    return
                if locale.atof(self.sub2.sub.e4.get())>175 or locale.atof(self.sub2.sub.e4.get())<30:
                    messagebox.showinfo('Message','Invalid input for lower rate limit\nshould be in the rannge 30-175ppm')
                    return
                f.write(self.sub2.sub.e1.get())
                f.write("\t")
                f.write(self.sub2.sub.e2.get())
                f.write("\t")
                f.write(self.sub2.sub.e3.get())
                f.write("\t")
                f.write(self.sub2.sub.e4.get())
                f.write("\t")
                f.write("0\t0\t0\t0\t0\t0\t0\t0\t0")
                f.close()
                messagebox.showinfo('Message','Settings saved')

            if (self.variable.get()=="VVI"):
  
                if locale.atof(self.sub2.sub.e1.get())>7 or locale.atof(self.sub2.sub.e1.get())<3.5:
                    messagebox.showinfo('Message','Invalid input for ventricular amplitude\nshould be in the range 3.5-7.0V')
                    return
                if locale.atof(self.sub2.sub.e2.get())>1.9 or locale.atof(self.sub2.sub.e2.get())<0.1:
                    messagebox.showinfo('Message','Invalid input for ventricular pulse width\nshould be in the range 0.1-1.9ms')
                    return
                if locale.atof(self.sub2.sub.e3.get())>175 or locale.atof(self.sub2.sub.e3.get())<50:
                    messagebox.showinfo('Message','Invalid input for upper rate limit\nshould be in the range 50-175ppm')
                    return
                if locale.atof(self.sub2.sub.e4.get())>175 or locale.atof(self.sub2.sub.e4.get())<30:
                    messagebox.showinfo('Message','Invalid input for lower rate limit\nshould be in the rannge 30-175ppm')
                    return
                if locale.atof(self.sub2.sub.e7.get())>10 or locale.atof(self.sub2.sub.e7.get())<1:
                    messagebox.showinfo('Message','Invalid input for ventricular sensitivity\nshould be in the rage 1.0-10.0mV')
                    return
                if locale.atof(self.sub2.sub.e9.get())>500 or locale.atof(self.sub2.sub.e9.get())<150:
                    messagebox.showinfo('Message','Invalid input for VRP\nshould be in range 150-500ms')
                    return
                if locale.atof(self.sub2.sub.e12.get())!=locale.atof(self.sub2.sub.e4.get()):
                    messagebox.showinfo('Message','Invalid input for hysteresis\nshould be the same with lower rate limit')
                    return
                entry13=locale.atof(self.sub2.sub,e13.get())
                if entry13!=0 and entry13!=3 and entry13!=6 and entry13!=9 and entry13!=12 and entry13!=15 and entry13!=18 and entry13!=21:
                    messagebox.showinfo('Message','Invalid input for rate smoothing\nshould be one number of 0,3,6,9,12,15,18,21')
                    return
                f.write(self.sub2.sub.e1.get())
                f.write("\t")
                f.write(self.sub2.sub.e2.get())
                f.write("\t")
                f.write(self.sub2.sub.e3.get())
                f.write("\t")
                f.write(self.sub2.sub.e4.get())
                f.write("\t")
                f.write("0\t0")
                f.write(self.sub2.sub.e7.get())
                f.write("\t0\t")
                f.write(self.sub2.sub.e9.get())
                f.write("\t0\t0\t")
                f.write(self.sub2.sub.e12.get())
                f.write(self.sub2.sub.e13.get())
                f.close()
                messagebox.showinfo('Message','Settings saved')
                         
            
        def load():
            outname=self.name.replace("filename",self.tempname)
            f=open(outname,"r")
            for line in f:
                line = line.strip().split("\t")
            temp1=line[0]
            temp2=line[1]
            temp3=line[2]
            temp4=line[3]
            self.sub2.sub.e1.insert(0,temp1)
            self.sub2.sub.e2.insert(0,temp2)
            self.sub2.sub.e3.insert(0,temp3)
            self.sub2.sub.e4.insert(0,temp4)
            messagebox.showinfo('Message','Settings loaded')



   #     def process_array():
  
##            
##        def clicked_reg():
##            self.sub1=Toplevel(self)
##            frame = Frame(self.sub1, width=300, height=300)
##            frame.pack()
##            
##            bName = Label(self.sub1, text="Username:")
##            bName.place(x=30,y=30)
##        
##            bPass = Label(self.sub1, text="Password:")
##            bPass.place(x=30,y=100)
##        
##            self.sub1.e1=Entry(self.sub1);
##            self.sub1.e1.place(x=110,y=30)
##            
##
##            self.sub1.e2=Entry(self.sub1)
##            self.sub1.e2.config(show="*")
##            self.sub1.e2.place(x=110,y=100)
##
##            confirm=Button(self.sub1,text="Confirm",command=clicked_reg1)
##            confirm.place(x=50,y=200)
##
##            cancel=Button(self.sub1,text="Cancel",command=self.sub1.destroy)
##            cancel.place(x=130,y=200)
##            

        def clicked_reg():
            self.sub1=Toplevel(self)
            frame = Frame(self.sub1, width=500, height=300)
            frame.pack()
            
            bName = Label(self.sub1, text="Username:")
            bName.place(x=60,y=30)
        
            bPass = Label(self.sub1, text="Password:")
            bPass.place(x=60,y=100)

            bPass = Label(self.sub1, text="Check Password:")
            bPass.place(x=10,y=150)
        
            self.sub1.e1=Entry(self.sub1);
            self.sub1.e1.place(x=200,y=30)
            

            self.sub1.e2=Entry(self.sub1)
            self.sub1.e2.config(show="*")
            self.sub1.e2.place(x=200,y=100)

            self.sub1.e3=Entry(self.sub1)
            self.sub1.e3.config(show="*")
            self.sub1.e3.place(x=200,y=150)

            confirm=Button(self.sub1,text="Confirm",command=clicked_reg1)
            confirm.place(x=50,y=200)

            cancel=Button(self.sub1,text="Cancel",command=self.sub1.destroy)
            cancel.place(x=130,y=200)
            
            
        def clicked_log():
            self.sub2=Toplevel(self)
            frame = Frame(self.sub2, width=300, height=300)
            frame.pack()
            
            bName = Label(self.sub2, text="Username:")
            bName.place(x=30,y=30)
        
            bPass = Label(self.sub2, text="Password:")
            bPass.place(x=30,y=100)
        
            self.sub2.e1=Entry(self.sub2)
            self.sub2.e1.place(x=110,y=30)
            

            self.sub2.e2=Entry(self.sub2)
            self.sub2.e2.config(show="*")
            self.sub2.e2.place(x=110,y=100)

            confirm=Button(self.sub2,text="Confirm",command=clicked_log1)
            confirm.place(x=50,y=200)

            cancel=Button(self.sub2,text="Cancel",command=self.sub2.destroy)
            cancel.place(x=130,y=200)
            
##        def clicked_reg1( ):
##            f=open("Z:/testcount.txt","r")
##            for line in f:
##                self.b=self.b+1
##            if self.b<=9:
##                f=open("Z:/testcount.txt","a")
##                f.write(self.sub1.e1.get())
##                f.write("\t")
##                f.write(self.sub1.e2.get())
##                f.write("\n")
##                f.close()
##                messagebox.showinfo('Message', 'You have registered')
##                self.sub1.destroy
##            elif self.b>9:
##                messagebox.showinfo('Message','Amount of user reaches maximum')
##                self.sub1.destroy
##

        def clicked_reg1( ):
            if self.sub1.e2.get()!=self.sub1.e3.get():
                messagebox.showinfo('Message','Password does not matched!')
            else:
                count=0
                f=open("Z:/testcount.txt","r")
                for line in f:
                    if count < 9:
                        count += 1
                    else:
                        messagebox.showinfo('Message','Amount of user reaches maximum')
                        f.close()
                        return
                f=open("Z:/testcount.txt","r")
                for line in f:
                    line = line.strip().split("\t")
                    if self.sub1.e1.get() == line[0]:
                        messagebox.showinfo('Message','User name has been used')
                        f.close()
                        return
                f=open("Z:/testcount.txt","a")
                f.write(self.sub1.e1.get())
                f.write("\t")
                f.write(self.sub1.e2.get())
                f.write("\n")
                f.close()
                messagebox.showinfo('Message', 'You have registered')
            

        #testing serial communication as well as added periodic action
        def init_serial():
            

            ports = list(port_list.comports())
            if not ports:
                if self.p_state == 0:
                    try:
                        ser.close()
                    except:
                        pass
                    messagebox.showinfo('Message','Device plugged out')
                    self.p_state = 1
            else:
                if self.p_state == 1:
                    
                    self.ser = serial.Serial()
                    self.ser.baudrate = 115200
                    for p in ports: print(p[0])
                    self.ser.port = p[0]
                    self.ser.open()
                   # x = b"\x16\x16\x16\x16\x16"
                    #x = len(array)
                    #print(x[0])
                    if self.ser.isOpen():
                        messagebox.showinfo('Message','Device plugged in ')    
                       # ser.write(b"\x16\x16\x16\x16\x16")
                    self.p_state = 0
                    thread_data_receiving()
            

            threading.Timer(1, init_serial).start()  

       #function callback when the selection is changed      
        def callback(*args):

            self.mode_state = 0
            print("variable changed")
            if (self.variable.get()=="AOO"):
                
                self.sub2.sub.e1.config(state='disabled')
                self.sub2.sub.e2.config(state='disabled')
                self.sub2.sub.e3.config(state='normal')
                self.sub2.sub.e4.config(state='normal')
                self.sub2.sub.e5.config(state='normal')
                self.sub2.sub.e6.config(state='normal')
                self.sub2.sub.e7.config(state='disabled')
                self.sub2.sub.e8.config(state='disabled')
                self.sub2.sub.e9.config(state='disabled')
                self.sub2.sub.e10.config(state='disabled')
                self.sub2.sub.e11.config(state='disabled')
                self.sub2.sub.e12.config(state='disabled')
                self.sub2.sub.e13.config(state='disabled')
              
            if (self.variable.get()=="AAI"):
                
                self.sub2.sub.e1.config(state='disabled')
                self.sub2.sub.e2.config(state='disabled')
                self.sub2.sub.e3.config(state='normal')
                self.sub2.sub.e4.config(state='normal')
                self.sub2.sub.e5.config(state='normal')
                self.sub2.sub.e6.config(state='normal')
                self.sub2.sub.e7.config(state='normal')
                self.sub2.sub.e8.config(state='disabled')
                self.sub2.sub.e9.config(state='disabled')
                self.sub2.sub.e10.config(state='normal')
                self.sub2.sub.e11.config(state='normal')
                self.sub2.sub.e12.config(state='normal')
                self.sub2.sub.e13.config(state='normal')
              
            if (self.variable.get()=="VOO"):
                
                self.sub2.sub.e1.config(state='normal')
                self.sub2.sub.e2.config(state='normal')
                self.sub2.sub.e3.config(state='normal')
                self.sub2.sub.e4.config(state='normal')
                self.sub2.sub.e5.config(state='disabled')
                self.sub2.sub.e6.config(state='disabled')
                self.sub2.sub.e7.config(state='disabled')
                self.sub2.sub.e8.config(state='disabled')
                self.sub2.sub.e9.config(state='disabled')
                self.sub2.sub.e10.config(state='disabled')
                self.sub2.sub.e11.config(state='disabled')
                self.sub2.sub.e12.config(state='disabled')
                self.sub2.sub.e13.config(state='disabled')
              
            if (self.variable.get()=="VVI"):
                
                self.sub2.sub.e1.config(state='normal')
                self.sub2.sub.e2.config(state='normal')
                self.sub2.sub.e3.config(state='normal')
                self.sub2.sub.e4.config(state='normal')
                self.sub2.sub.e5.config(state='disabled')
                self.sub2.sub.e6.config(state='disabled')
                self.sub2.sub.e7.config(state='normal')
                self.sub2.sub.e8.config(state='disabled')
                self.sub2.sub.e9.config(state='normal')
                self.sub2.sub.e10.config(state='disabled')
                self.sub2.sub.e11.config(state='disabled')
                self.sub2.sub.e12.config(state='normal')
                self.sub2.sub.e13.config(state='normal')
                
        def thread_data_receiving():
            try:       
                s = self.ser.read(2)
                print("message received from simulink")
                print(s[1])
            except:
                pass
            if self.p_state == 0:
                threading.Timer(0.1, thread_data_receiving).start()  



            
        def send_bytearray(array):
            if self.p_state == 1:
                messagebox.showinfo('Message','devoce not plugged in check your connection')
            else:
               # ser = serial.Serial()
                #ser.baudrate = 115200
                print(array)
                ports = list(port_list.comports())
                if not ports:
                   
                    messagebox.showinfo('Message','message not been able to send due to noise')
                        
                else:
                    print(ports)
                    for p in ports: print(p[0])
                    #ser.port = p[0]
                    #ser.open()
                    sent_arr = bytearray(array)
                    #x = len(array)
                    print(sent_arr[0])
                    if self.ser.isOpen():
                        self.ser.write(sent_arr)
                        messagebox.showinfo('Message','message sent ')
                        
                #ser.close()


        def set_para(atr_pace, ventri_pace, atr_sensing, vent_sensing, vrp_l,vrp_h, arp_l, arp_h, pvarp_l,pvarp_h, hystersis, ven_cmp_pwm, art_cmp):
            self.pro_array[1] = atr_pace
            self.pro_array[2] = ventri_pace
            self.pro_array[3] = atr_sensing
            self.pro_array[4] = vent_sensing
            self.pro_array[5] = vrp_l
            self.pro_array[6] = vrp_h
            self.pro_array[7] = arp_l
            self.pro_array[8] = arp_h
            self.pro_array[9] = pvarp_l
            self.pro_array[10] = pvarp_h
            self.pro_array[11] = hystersis
            self.pro_array[12] = ven_cmp_pwm
            self.pro_array[13] = art_cmp
            
            
        def unpacking(numb,pos):
            low_bit = numb % 256
            high_bit = numb // 256
            self.pro_array[pos] = low_bit
            self.pro_array[pos] = high_bit

        
                
        def process_array():
            #thread_data_receiving()


            if (self.mode_state == 0):            
                self.pro_array = [0x16,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]
                print(self.sub2.sub.e1.get())
                if (self.variable.get()=="VOO"):
                    set_para(0, 1, 0, 0, 94, 1,250,0, 250,0, 0, 50, 15)
                if (self.variable.get()=="AOO"):
                    set_para(1,0,0,0,94,1,250,0,250,0,0,50,15)
                if (self.variable.get()=="AAI"):
                    set_para(1,0,1,0,94,1,250,0,250,0,1,50,15)
                if (self.variable.get()=="VVI"):
                    set_para(0,1,0,1,94,1,250,0,250,0,0,50,15)

                self.mode_state == 1
            else:            
                
                if self.sub2.sub.e1.get() != "":
                    try:
                        #pro_array[1] = (int(self.sub2.sub.e1.get()))
                        pass
                    except:
                        pass

                if self.sub2.sub.e2.get() != "":
                    try:
                        #pro_array[2] = (int(self.sub2.sub.e2.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e3.get() != "":
                    try:
                        #pro_array[3] = (int(self.sub2.sub.e3.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e4.get() != "":
                    try:
                        #pro_array[4] = (int(self.sub2.sub.e4.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e5.get() != "":
                    try:
                        #pro_array[5] = (int(self.sub2.sub.e5.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e6.get() != "":
                    try:
                        #pro_array[6] = (int(self.sub2.sub.e6.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e7.get() != "":
                    try:
                        #pro_array[7] = (int(self.sub2.sub.e7.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e8.get() != "":
                    try:
                        #pro_array[8] = (int(self.sub2.sub.e8.get()))
                        pass
                    except:
                        pass
                if self.sub2.sub.e9.get() != "":
                    try:
                        #pro_array[9] = (int(self.sub2.sub.e9.get()))
                        unpacking((int(self.sub2.sub.e9.get())),4)
                    except:
                        pass
                if self.sub2.sub.e10.get() != "":
                    try:
                        #pro_array[10] = (int(self.sub2.sub.e10.get()))
                        unpacking((int(self.sub2.sub.e10.get())),6)
                    except:
                        pass
                if self.sub2.sub.e11.get() != "":
                    try:
                        #pro_array[11] = (int(self.sub2.sub.e11.get()))
                        unpacking((int(self.sub2.sub.e11.get())),8)
                        pass
                    except:
                        pass

                if self.sub2.sub.e12.get() != "":
                    try:
                        #pro_array[12] = (int(self.sub2.sub.e12.get()))
                        pass
                    except:
                        pass

                if self.sub2.sub.e13.get() != "":
                    try:
                        #pro_array[13] = (int(self.sub2.sub.e13.get()))
                        pass
                    except:
                        pass
                
            send_bytearray(self.pro_array)
        #added  
        def clicked_log1( ):
            file=open("Z:/testcount.txt","r")
            a=0
            for line in file:
                line = line.strip().split("\t")
                if self.sub2.e1.get() == line[0]:
                    a = 1
                    if self.sub2.e2.get() == line[1]:
                        messagebox.showinfo('Message','You are logged in')
                        self.sub2.sub=Toplevel(self.sub2)
                        self.sub2.sub.title("window")
                        self.sub2.sub.geometry("600x600+125+125")
                        self.master.after(100, init_serial)


                        ##serial auto detection thread starts


                        #init_serial()
                        

                        self.variable = StringVar(self.sub2.sub)
                        self.variable.set("Select") # default value
                        self.variable.trace("w", callback)
                        w = OptionMenu(self.sub2.sub, self.variable, "AAT", "VVT", "AOO","AAI","VOO","VVI","VDD","DOO","DDI","DDD","AOOR","AAIR","VOOR","VVIR","VDDR","DOOR","DDIR","DDDR")
                        w.pack()
                        
                        w.place(x=120,y=50)
                        w1=Label(self.sub2.sub,text="Select mode:")
                        w1.place(x=30,y=50)
                        
                        send_button = Button(self.sub2.sub,text = "Send", command=process_array)
                        send_button.place(x=100,y=370)
                        cancel_button = Button(self.sub2.sub,text = "Cancel",command=self.sub2.sub.destroy)
                        cancel_button.place(x=160,y=370)
                        saveButton=Button(self.sub2.sub,text="Save current setting",command=save)
                        saveButton.place(x=220,y=370)

                        ##Parameter Label
                        voo=Label(self.sub2.sub, text="Ventricular Amplitude:")
                        voo.place(x=30,y=100)
                        voo1=Label(self.sub2.sub,text="Ventricular Pulse Width:")
                        voo1.place(x=30,y=120)
                        voo2=Label(self.sub2.sub,text="Upper Rate Limit:")
                        voo2.place(x=30,y=140)
                        voo3=Label(self.sub2.sub,text="Lower Rate Limit:")
                        voo3.place(x=30,y=160)
                        voo4=Label(self.sub2.sub, text="Atrial Amplitude:")
                        voo4.place(x=30,y=180)
                        voo5=Label(self.sub2.sub, text="Atrial Pulse Width:")
                        voo5.place(x=30,y=200)
                        voo6=Label(self.sub2.sub, text="Ventricular Sensitivity:")
                        voo6.place(x=30,y=220)
                        voo7=Label(self.sub2.sub, text="Atrial Sensitivity:")
                        voo7.place(x=30,y=240)
                        voo8=Label(self.sub2.sub, text="VRP:")
                        voo8.place(x=30,y=260)
                        voo9=Label(self.sub2.sub, text="ARP:")
                        voo9.place(x=30,y=280)
                        voo10=Label(self.sub2.sub, text="PVARP:")
                        voo10.place(x=30,y=300)
                        voo11=Label(self.sub2.sub, text="Hysteresis:")
                        voo11.place(x=30,y=320)
                        voo12=Label(self.sub2.sub, text="Rate Smoothing:")
                        voo12.place(x=30,y=340)
                        
                        self.tempname=self.sub2.e1.get()
                        
                        ##Parameter entries
                        self.sub2.sub.e1=Entry(self.sub2.sub)
                        self.sub2.sub.e1.place(x=180,y=100)
                        self.sub2.sub.e2=Entry(self.sub2.sub)
                        self.sub2.sub.e2.place(x=180,y=120)
                        self.sub2.sub.e3=Entry(self.sub2.sub)
                        self.sub2.sub.e3.place(x=180,y=140)
                        self.sub2.sub.e4=Entry(self.sub2.sub)
                        self.sub2.sub.e4.place(x=180,y=160)
                        self.sub2.sub.e5=Entry(self.sub2.sub)
                        self.sub2.sub.e5.place(x=180,y=180)
                        self.sub2.sub.e6=Entry(self.sub2.sub)
                        self.sub2.sub.e6.place(x=180,y=200)
                        self.sub2.sub.e7=Entry(self.sub2.sub)
                        self.sub2.sub.e7.place(x=180,y=220)
                        self.sub2.sub.e8=Entry(self.sub2.sub)
                        self.sub2.sub.e8.place(x=180,y=240)
                        self.sub2.sub.e9=Entry(self.sub2.sub)
                        self.sub2.sub.e9.place(x=180,y=260)
                        self.sub2.sub.e10=Entry(self.sub2.sub)
                        self.sub2.sub.e10.place(x=180,y=280)
                        self.sub2.sub.e11=Entry(self.sub2.sub)
                        self.sub2.sub.e11.place(x=180,y=300)
                        self.sub2.sub.e12=Entry(self.sub2.sub)
                        self.sub2.sub.e12.place(x=180,y=320)
                        self.sub2.sub.e13=Entry(self.sub2.sub)
                        self.sub2.sub.e13.place(x=180,y=340)

                        print(self.variable.get())
                        

                        load()

                    elif self.sub2.e2.get() != line[1]:
                        messagebox.showinfo('Message','Password is not correct')
            if a==0:
                messagebox.showinfo('Message','You are not registered')
            file.close()
                        
                

        # creating a button instance
        regButton = Button(self, text="Register",command=clicked_reg)
        regButton.place(x=30, y=200)

        
        logButton = Button(self, text="Log in",command=clicked_log)
        logButton.place(x=150, y=200)
        
   
## wasted testing garbage       
##class ThreadedTask(threading.Thread):
##    def __init__(self,queue):
##        threading.Thread.__init__(self)
##        self.queue = queue
##        
##    def run(self):
##        self.thread_serial_auto()
##        self.queue.put("task finished")
##     #multithread to detect the status of the serial communication
##            
##    def thread_serial_auto(self):
##        p = []
##        a = ""
##        serial_state = 0
##        ports = list(port_list.comports())
##        for p in ports: print(p[0])
##        try:
##            a = p[0]
##        except:
##            pass
##        
##        while 1:
##            if(serial_state == 0):
##                a = ""
##               # print("a")
##            ports = list(port_list.comports())
##            #print(ports)
##            for p in ports: pass
##            try:
##                a = p[0]
##            except:
##                pass
##            
##            if(ports != []):
##                
##                if(serial_state == 1):
##                    self.init_serial()
##                    serial_state = 0
##                
##            else:
##          
##                if(serial_state == 0):
##                    #do sth
##                    
##                    print("normal state")
##                    serial_state = 1
##            
##        print("hello")






root = Tk()

#size of the window
root.geometry("300x300")

app = Window(root)

root.mainloop()  


