from tkinter import *
from tkinter.font import Font
# from PIL import image,imageTk
class FBLOGIn:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("600x550+0+0")
        self.root.title("Facebook Login")
        self.root.config(bg="midnight blue")

        title = Label(self.root,text="facebook",font=("timesnewroman 50 bold "),bg="midnight blue",fg="white")
        title.place(x=145,y=60)
        # # Frame
        user_lbl=Label(self.root,font=("timesnewroman 26 bold"),text="Email:",fg="white",bg="midnight blue",).place(x=120,y=185)
        
        user_entry=Entry(self.root,font=("timesnewroman 20 "),bg="white",).place(x=140,y=240)
        
        pass_lbl=Label(self.root,font=("timesnewroman 26 bold"),text="Password:",fg="white",bg="midnight blue",).place(x=115,y=300)
        
        pass_entry=Entry(self.root,font=("timesnewroman 20 "),bg="white",).place(x=140,y=350)

        login_btn = Button(self.root,text="Login",font=("timesnewroman 16 bold"),fg="white",bg="darkgreen",cursor="hand2").place(x=240,y=430,width=100,height=30)
        
        forget_btn = Button(self.root,text="Forget Password?",font=("timesnewroman 11 "),bd=0,fg="white",bg="midnight blue",cursor="hand2").place(x=295,y=394,height=20)
        
        or_txt=Label(self.root,text="OR",font="timesnewroman 10",fg="white",bg="midnight blue").place(x=275,y=475,height=10)

        create_btn = Button(self.root,text="Create an account",font=("timesnewroman 14 "),fg="white",bg="darkgreen",cursor="hand2", command=self.create_wind).place(x=203,y=500,height=30)

    def create_wind(self):
        self.root.destroy()  
        from create import FBCREATE  
        

root=Tk()
obj1 = FBLOGIn(root)
root.mainloop()