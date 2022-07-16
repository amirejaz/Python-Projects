from tkinter import *

from PIL import Image,ImageTk
from tkinter import messagebox

class login():
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+50+50")
        self.root.resizable(False,False)

        # BG Image
        self.image = Image.open("1.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.img_Label = Label(self.root,image=self.photo).place(x=0,y=0,relwidth=1,relheight=1)
        
        # Login Frame 
        Framelogin = Frame(self.root,bg="white")
        Framelogin.place(x=330,y=150,height=320,width=500)
        
        title = Label(Framelogin,text="Login Here",bg="white",font=("Impact 35 bold"),fg="VioletRed3").place(x=130,y=20)

        
        desc = Label(Framelogin,text="Employee Accountant Login Area",bg="white",font=("BaoliSC 15 bold"),fg="VioletRed4").place(x=90,y=80)

        lbl_user = Label(Framelogin,text="Username",font=("Goudyoldstyle 15 bold"),bg="white",fg="gray").place(x=60,y=117)

        self.txt_user = Entry(Framelogin,font=("timesnewroman 15"),bg="lightgray")
        self.txt_user.place(x=70,y=150,width=350,height=35) 

        
        lbl_pass = Label(Framelogin,text="Password",font=("Goudyoldstyle 15 bold"),bg="white",fg="gray").place(x=60,y=190)

        self.txt_pass = Entry(Framelogin,font=("timesnewroman 15"),bg="lightgray")
        self.txt_pass.place(x=70,y=220,width=350,height=35) 

        forget_btn = Button(Framelogin,text="Forget Password?",cursor="hand2",bg="white",fg="VioletRed4",font=("timesnewroman 12 ")).place(x=75 ,y=264,height=26  )

        
        login_btn = Button(self.root,command=self.login_function,cursor="hand2",text="Login",bg="VioletRed3",fg="white",font=("timesnewroman 20 ")).place(x=510 ,y=450,width=130,height=50  )

    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent = self.root)

        elif self.txt_user.get()!="Amir" or self.txt_pass.get()!="123456":
            messagebox.showerror("Error","Invalid Username/Password ",parent = self.root)

        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}")       

root = Tk()
obj = login(root)
root.mainloop()
    
