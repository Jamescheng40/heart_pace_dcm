from tkinter import *

from tkinter import messagebox

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        #hahahahahahahahah

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welcome")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        
        

        bName = Label(self, text="Username:")
        bName.place(x=30,y=30)
        
        bPass = Label(self, text="Password:")
        bPass.place(x=30,y=100)
        
        self.e1=Entry(self)
        self.e1.place(x=110,y=30)

        self.e2=Entry(self)
        self.e2.place(x=110,y=100)

        
        def clicked_reg( ):
            f=open("/Users/pc/Desktop/kill.txt","r")
            for line in f:
                line = line.strip().split("\t")
                if self.e1.get() == line[0]:
                    if self.e2.get() == line[1]:
                        messagebox.showinfo('Message','You have registered')
                        f.close()
                        return
                    elif self.e2.get() != line[1]:
                        messagebox.showinfo('Message','User name has been registered')
                        f.close()
                        return
            f=open("/Users/pc/Desktop/kill.txt","a")
            f.write(self.e1.get())
            f.write("\t")
            f.write(self.e2.get())
            f.write("\n")
            f.close()
            messagebox.showinfo('Message', 'You have registered')

        def clicked_log( ):
            file=open("/Users/pc/Desktop/kill.txt","r")
            a=0
            for line in file:
                line = line.strip().split("\t")
                if self.e1.get() == line[0]:
                    a = 1
                    if self.e2.get() == line[1]:
                        messagebox.showinfo('Message','You are logged in')
                        sub=Toplevel(self)
                        sub.title("window")
                        sub.geometry("400x400+125+125")
                        variable = StringVar(sub)
                        variable.set("Select") # default value
                        w = OptionMenu(sub, variable, "AAT", "VVT", "AOO","AAI","VOO","VVI","VDD","DOO","DDI","DDD","AOOR","AAIR","VOOR","VVIR","VDDR","DOOR","DDIR","DDDR")
                        w.pack()
                        w.place(x=120,y=20)
                        w1=Label(sub,text="Select mode:")
                        w1.place(x=30,y=20)
                        voo=Label(sub, text="Ventricular Amplitude:")
                        voo.place(x=30,y=100)
                        voo1=Label(sub,text="Ventricular Pulse Width:")
                        voo1.place(x=30,y=150)
                        voo2=Label(sub,text="Upper Rate Limit:")
                        voo2.place(x=30,y=200)
                        voo3=Label(sub,text="Lower Rate Limit:")
                        voo3.place(x=30,y=250)
                        sub.e1=Entry(sub)
                        sub.e1.place(x=180,y=100)
                        sub.e2=Entry(sub)
                        sub.e2.place(x=180,y=150)
                        sub.e3=Entry(sub)
                        sub.e3.place(x=180,y=200)
                        sub.e4=Entry(sub)
                        sub.e4.place(x=180,y=250)


                    elif self.e2.get() != line[1]:
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
