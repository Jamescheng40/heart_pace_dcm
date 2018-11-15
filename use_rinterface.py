from tkinter import *

from tkinter import messagebox

class Window(Frame):

#hahahahahahaha lallaalalalalalalal
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welcome")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        binit = Label(self, text="Please register before you log in")
        binit.place(x=30,y=30)

        def clicked_reg():
            sub1=Toplevel(self)
            frame = Frame(sub1, width=300, height=300)
            frame.pack()
            
            bName = Label(sub1, text="Username:")
            bName.place(x=30,y=30)
        
            bPass = Label(sub1, text="Password:")
            bPass.place(x=30,y=100)
        
            sub1.e1=Entry(sub1)
            sub1.e1.place(x=110,y=30)

            sub1.e2=Entry(sub1)
            sub1.e2.place(x=110,y=100)

            confirm=Button(sub1,text="Confirm",command=clicked_reg1)
            confirm.place(x=50,y=200)

            cancel=Button(sub1,text="Cancel",command=sub1.destroy)
            cancel.place(x=130,y=200)
            
            
        def clicked_log():
            sub2=Toplevel(self)
            frame = Frame(sub2, width=300, height=300)
            frame.pack()
            
            bName = Label(sub2, text="Username:")
            bName.place(x=30,y=30)
        
            bPass = Label(sub2, text="Password:")
            bPass.place(x=30,y=100)
        
            sub2.e1=Entry(sub2)
            sub2.e1.place(x=110,y=30)

            sub2.e2=Entry(sub2)
            sub2.e2.place(x=110,y=100)

            confirm=Button(sub2,text="Confirm",command=clicked_log1)
            confirm.place(x=50,y=200)

            cancel=Button(sub2,text="Cancel",command=sub2.destroy)
            cancel.place(x=130,y=200)
            
        def clicked_reg1( ):
            f=open("D:/banana.txt","a")
            f.write(sub1.e1.get())
            f.write("\t")
            f.write(sub1.e2.get())
            f.write("\n")
            f.close()
            messagebox.showinfo('Message', 'You have registered')

        def clicked_log1( ):
            file=open("D:/banana.txt","r")
            a=0
            for line in file:
                line = line.strip().split("\t")
                if sub2.e1.get() == line[0]:
                    a = 1
                    if sub2.e2.get() == line[1]:
                        messagebox.showinfo('Message','You are logged in')
                        sub=Toplevel(sub1)
                        sub.title("window")
                        sub.geometry("400x400+125+125")
                        variable = StringVar(sub)
                        variable.set("Select") # default value
                        

                        w = OptionMenu(sub, variable, "AAT", "VVT", "AOO","AAI","VOO","VVI","VDD","DOO","DDI","DDD","AOOR","AAIR","VOOR","VVIR","VDDR","DOOR","DDIR","DDDR")
                        w.pack()
                        w.place(x=120,y=20)
                        w1=Label(sub,text="Select mode:")
                        w1.place(x=30,y=20)
                        send_button = Button(sub,text = "Send")
                        send_button.place(x=200,y=20)
                        cancel_button = Button(sub,text = "Cancel")
                        cancel_button.place(x=260,y=20)
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


                    elif sub1.e2.get() != line[1]:
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
