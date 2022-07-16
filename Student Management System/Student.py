from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql.cursors import Cursor
class Student():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #=====All Variables=====
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Age_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_No_var=StringVar()
        self.DOB_var=StringVar()
        self.Search_By = StringVar()
        self.search_txt = StringVar()
        
        

    #===Manage Frame=====
    
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",fg="white",bg="green",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
      
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_age=Label(Manage_Frame,text="Age",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_age.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_age=Entry(Manage_Frame,textvariable=self.Age_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_age.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_Gender['values']=("male","female","other")
        combo_Gender.grid(row=4,column=1,pady=10,padx=20)


        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_DOB=Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_cont=Label(Manage_Frame,text="Contact No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_cont.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        
        txt_cont=Entry(Manage_Frame,textvariable=self.Contact_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cont.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_add=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        
        self.txt_Address=Text(Manage_Frame,width=30,height=3,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

    #===Button Frame=====

        btn_Frame=Frame(Manage_Frame,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=518,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=11,pady=11)        
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.Update_data)
        Updatebtn.grid(row=0,column=1,padx=11,pady=11)        
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data)
        Deletebtn.grid(row=0,column=2,padx=11,pady=11)        
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear)
        Clearbtn.grid(row=0,column=3,padx=11,pady=11)        

    #===Detail Frame=====

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=580)
        
        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
     
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.Search_By,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll No.","Name","Age")
        combo_search.grid(row=0,column=1,pady=10,padx=20)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=6,pady=10)        
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data)
        showallbtn.grid(row=0,column=4,padx=6,pady=10)        

    #========Table Frame=====

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame,columns=("Roll No.",'Name','Age','Gender','Contact','D.O.B','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Roll No.",text="Roll No.")
        self.Student_Table.heading("Name",text="Name")
        self.Student_Table.heading("Age",text="Age")
        self.Student_Table.heading("Gender",text="Gender")
        self.Student_Table.heading("Contact",text="Contact")
        self.Student_Table.heading("D.O.B",text="D.O.B")
        self.Student_Table.heading("Address",text="Address")   
        self.Student_Table['show']='headings'
        self.Student_Table.column('Roll No.',width=80)
        self.Student_Table.column('Name',width=140)
        self.Student_Table.column('Age',width=100)
        self.Student_Table.column('Contact',width=140)
        self.Student_Table.column('D.O.B',width=100)
        self.Student_Table.column('Address',width=150)    
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor )

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All fields are required !!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.Name_var.get(),self.Age_var.get(),self.Gender_var.get(),self.DOB_var.get(),self.Contact_No_var.get(),self.txt_Address.get('1.0',END) ))
            con.commit()
            self.clear()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")  
        self.Name_var.set("")  
        self.Age_var.set("")  
        self.Gender_var.set("") 
        self.DOB_var.set("")  
        self.Contact_No_var.set("")  
        self.txt_Address.delete("1.0",END)    

    def get_cursor(self,ev):
        cursor_row=self.Student_Table.focus()
        contents=self.Student_Table.item(cursor_row)
        row=contents['values']
        self.Roll_No_va.set(row[0])  
        self.Name_var.set(row[1])  
        self.Age_var.set(row[2])  
        self.Gender_var.set(row[3]) 
        self.DOB_var.set(row[4])  
        self.Contact_No_var.set(row[5])  
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
        
    def Update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("Update student set Name=%s,Age=%s,Gender=%s,DOB=%s,Contact_No=%s,Address=%s,where Roll No=%s",(self.Name_var.get(),self.Age_var.get(),self.Gender_var.get(),self.DOB_var.get(),self.Contact_No_var.get(),self.txt_Address.get('1.0',END),self.Roll_No_var.get() ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from student where Roll No =%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
              
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("Select * from student where"+str (self.Search_By.get())+ " LIKE '% " +str(self.search_txt.get()+"%'"))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            con.commit()
        con.close()

        
root = Tk()
obj = Student(root)
root.mainloop()        