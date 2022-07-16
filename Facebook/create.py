from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
class FBCREATE:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1200x750+0+0")
        self.root.title("Create an account")
        self.root.config(bg="white")

        Manage_Frame=Frame(self.root,bg="blue4")
        Manage_Frame.place(x=0,y=0,relwidth=1,height=110)

        title = Label(Manage_Frame,text="facebook",font=("timesnewroman 50 bold "),bg="blue4",fg="white")
        title.place(x=0,y=10,relwidth=1,height=100)

        signin_btn = Button(Manage_Frame,text="Already have an account",font=("timesnewroman 11 "),bd=0,fg="white",bg="blue4",cursor="hand2", command = self.log_window).place(x=900,y=50,height=20)
        

        self.img = Image.open("images.png")
        self.resize_image1 = self.img.resize((120,120))
        self.logoimg = ImageTk.PhotoImage( self.resize_image1)
        labelimg = Label(image=self.logoimg)
        labelimg.image = self.logoimg
        labelimg.place(x=530,y=120)

        head = Label(self.root,text="Create an account",font=("timesnewroman 30 bold "),bg="white",fg="black")
        head.place(x=425,y=250)

        self.f_name = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="First Name").place(x=300,y=330)
        self.f_entry = Entry(self.root,bg="gray",font=("timesnewroman 12"),fg="black")
        self.f_entry.place(x=300,y=360,width=250,height=24) 
        
        self.l_name = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Last Name").place(x=650,y=329)
        self.l_entry = Entry(self.root,bg="gray",font=("timesnewroman 12"),fg="black")
        self.l_entry.place(x=650,y=359,width=250,height=24) 

        self.age_lbl = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="D.O.B").place(x=300,y=390)
        self.age_txt = Entry(self.root,bg="gray",font=("timesnewroman 12"),fg="black")
        self.age_txt.place(x=300,y=420,width=250,height=24) 
        
        self.contact_lbl = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Contact No.").place(x=650,y=389)
        self.contact_txt = Entry(self.root,bg="gray",font=("timesnewroman 12"),fg="black")
        self.contact_txt.place(x=650,y=420,width=250,height=24) 


        self.f_security = Label(self.root,text="Security Question",font=("timesnewroman",15),bg="white",fg="black").place(x=300,y=456)
        self.combo_security = ttk.Combobox(self.root,font=("timesnewroman",13),state="readonly",justify=CENTER)
        self.combo_security['values'] = ("Select","You best friend name","Your favourite colour","Your birth place")
        self.combo_security.place(x=300,y=487,width=250)
        self.combo_security.current(0)


        self.answer = Label(self.root,text="Answer",font=("timesnewroman",15),bg="white",fg="black").place(x=651,y=450)
        self.txt_answer = Entry(self.root,font=("timesnewroman",15),bg="gray")
        self.txt_answer.place(x=650,y=482,width=250,height=26)

        self.email = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Email Address").place(x=300,y=523)
        self.email_txt=Entry(self.root,font=("timesnewroman 12"),bg="gray",fg="black")
        self.email_txt.place(x=300,y=555,width=250,height=26)
        
        self.c_email= Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Confirm Email ").place(x=650,y=520)
        self.cemail_txt=Entry(self.root,font=("timesnewroman 12"),bg="gray",fg="black")
        self.cemail_txt.place(x=650,y=553,width=250,height=26)
        
        self.password = Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Password").place(x=300,y=590)
        self.pass_txt=Entry(self.root,font=("timesnewroman 12"),bg="gray",fg="black")
        self.pass_txt.place(x=300,y=620,width=250,height=26)
        
        self.c_pass= Label(self.root,font=("timesnewroman 15"),fg="black",bg="white",text="Confirm Password ").place(x=650,y=589)
        self.cpass_txt=Entry(self.root,font=("timesnewroman 12"),bg="gray",fg="black")
        self.cpass_txt.place(x=650,y=619,width=250,height=26)

        self.create_btn = Button(self.root,text="Create an account",font=("timesnewroman 15 "),fg="white",bg="darkgreen",cursor="hand2", command=self.create).place(x=510,y=670,height=40)

    def log_window(self):
        self.root.destroy()
        from login import FBLOGIn    

    def create(self):

        if self.f_entry.get()==""  or self.l_entry.get()=="" or self.age_txt.get()==""  or self.contact_txt.get()=="" or self.txt_answer.get()==""or self.email_txt.get()==""or self.cemail_txt.get()==""or self.pass_txt.get()=="" or self.cpass_txt.get()=="":
           messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif self.pass_txt.get() != self.cpass_txt.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same ", parent=self.root)
        
        elif self.email_txt.get() != self.cemail_txt.get():
            messagebox.showerror("Error", "Email & Confirm Email should be same ", parent=self.root)
        
        else:    
            messagebox.showinfo("SUCCESS", "Account has been created")
            
root=Tk()
obj2 = FBCREATE(root)
root.mainloop()