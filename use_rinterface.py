from tkinter import *

from tkinter import messagebox
import serial
import _thread


class Window(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.b = 0
        self.tempname=""
        self.name="D:/filename.txt"
        self.init_window()



    

        
    #Creation of init_window12345678990
        
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welcome")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        binit = Label(self, text="Please register before you log in")
        binit.place(x=30,y=30)


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
                    



        def save():
             
            if int(self.sub2.sub.e1.get())>100:
                messagebox.showinfo('Message','Invalid input for amplitude')
                return
            if int(self.sub2.sub.e2.get())>100:
                messagebox.showinfo('Message','Invalid input for pulse width')
                return
            if int(self.sub2.sub.e3.get())>100:
                messagebox.showinfo('Message','Invalid input for upper rate limit')
                return
            if int(self.sub2.sub.e4.get())>100:
                messagebox.showinfo('Message','Invalid input for lower rate limit')
                return
            
            outname=self.name.replace("filename",self.tempname)
            f=open(outname,"w")
            f.write(self.sub2.sub.e1.get())
            f.write("\t")
            f.write(self.sub2.sub.e2.get())
            f.write("\t")
            f.write(self.sub2.sub.e3.get())
            f.write("\t")
            f.write(self.sub2.sub.e4.get())
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


                        variable = StringVar(self.sub2.sub)
                        variable.set("Select") # default value
                        w = OptionMenu(self.sub2.sub, variable, "AAT", "VVT", "AOO","AAI","VOO","VVI","VDD","DOO","DDI","DDD","AOOR","AAIR","VOOR","VVIR","VDDR","DOOR","DDIR","DDDR")
                        w.pack()
                        
                        w.place(x=120,y=50)
                        w1=Label(self.sub2.sub,text="Select mode:")
                        w1.place(x=30,y=50)
                        
                        send_button = Button(self.sub2.sub,text = "Send", command=init_serial)
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

                        if (variable.get()=="AOO"):
                            self.sub2.sub.e1.config(state='disabled')
                            self.sub2.sub.e2.config(state='disabled')
                            self.sub2.sub.e7.config(state='disabled')
                            self.sub2.sub.e8.config(state='disabled')
                            self.sub2.sub.e9.config(state='disabled')
                            self.sub2.sub.e10.config(state='disabled')
                            self.sub2.sub.e11.config(state='disabled')
                            self.sub2.sub.e12.config(state='disabled')
                            self.sub2.sub.e13.config(state='disabled')
                        if (variable.get()=="AAI"):
                            self.sub2.sub.e1.config(state='disabled')
                            self.sub2.sub.e2.config(state='disabled')
                            self.sub2.sub.e8.config(state='disabled')
                            self.sub2.sub.e9.config(state='disabled')
                        if (variable.get()=="VOO"):
                            self.sub2.sub.e5.config(state='disabled')
                            self.sub2.sub.e6.config(state='disabled')
                            self.sub2.sub.e7.config(state='disabled')
                            self.sub2.sub.e8.config(state='disabled')
                            self.sub2.sub.e9.config(state='disabled')
                            self.sub2.sub.e10.config(state='disabled')
                            self.sub2.sub.e11.config(state='disabled')
                            self.sub2.sub.e12.config(state='disabled')
                            self.sub2.sub.e13.config(state='disabled')
                        if (variable.get()=="VVI"):
                            self.sub2.sub.e5.config(state='disabled')
                            self.sub2.sub.e6.config(state='disabled')
                            self.sub2.sub.e8.config(state='disabled')
                            self.sub2.sub.e10.config(state='disabled')
                            self.sub2.sub.e11.config(state='disabled')
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
        
   
          

root = Tk()

#size of the window
root.geometry("300x300")

app = Window(root)
root.mainloop()  
