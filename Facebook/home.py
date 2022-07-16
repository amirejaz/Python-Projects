from tkinter import *
from PIL import Image, ImageTk





class Home:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title("Facebook")

        self.image1 = Image.open("home2.jpg")
        self.resize_image1 = self.image1.resize((1300,700))
        img1 = ImageTk.PhotoImage(self.resize_image1)
        label1 = Label(image=img1)
        label1.image = img1
        label1.place(x=0,y=0,relwidth=1,relheight=1)

        login_btn = Button(self.root,text="Login",font=("timesnewroman 18 bold"),fg="white",bg="darkgreen",cursor="hand2", command = self.login_window).place(x=850,y=500,width=100,height=50)

        create_btn = Button(self.root,text="Create an account",font=("timesnewroman 15 "),fg="white",bg="darkgreen",cursor="hand2", command = self.create_window).place(x=810,y=570,height=40)

    def login_window(self):
        self.root.destroy()
        from login import FBLOGIn
        

    def create_window(self):
        self.root.destroy()  
        from create import FBCREATE  

root=Tk()
obj = Home(root)
root.mainloop()        