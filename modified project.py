from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class database:
    def __init__(self,batsman):
        self.connection=sqlite3.connect(batsman)
        self.cursor=self.connection.cursor()
        sql="""
        CREATE TABLE  IF NOT EXISTS Student(
            ADMNNO integer,
            NAME text,
            CLASS,
            CONTACT integer,
            ADDRESS,
            dob,
            MENTOR,
            HEIGHT,
           
            WEIGHT integer,
            CHARACTER integer
        )
        """
        self.cursor.execute(sql)
        self.connection.commit()
 
    def insert(self,ADMNNO,NAME,CLASS,CONTACT,ADDRESS,dob,MENTOR,HEIGHT,WEIGHT,CHARACTER):
        
        self.cursor.execute("insert into Student values(?,?,?,?,?,?,?,?,?,?)",(ADMNNO,NAME,CLASS,CONTACT,ADDRESS,dob,MENTOR,HEIGHT,WEIGHT,CHARACTER))
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * from Student")
        rows=self.cursor.fetchall()
        #print(rows)
        return rows
    def remove(self,ADMNNO):
        self.cursor.execute("delete from Student where ADMNNO=?",(ADMNNO,))
        self.connection.commit()

    def update(self,ADMNNO,NAME,CLASS,CONTACT,ADDRESS,dob,MENTOR,HEIGHT,WEIGHT,CHARACTER):
        self.cursor.execute("update Student set ADMNNO=?,NAME=?,CLASS=?,CONTACT=?,ADDRESS=?,dob=?,MENTOR=?,HEIGHT=?,WEIGHT=?,CHARACTER=? ",(ADMNNO,NAME,CLASS,CONTACT,ADDRESS,dob,MENTOR,HEIGHT,WEIGHT,CHARACTER))
        self.connection.commit()
        
        
       
    



db=database("students.db")





root=Tk()
root.title("Sivalingaiit's school students record")
root.iconbitmap(r'D:/project/icon.ico')

root.geometry("1350x700+0+0")
root.config(bg="TEAL")

ADMNNO=StringVar()
NAME=StringVar()
CLASS=StringVar()
CONTACT=StringVar()
ADDRESS=StringVar()
dob=StringVar()
MENTOR=StringVar()
HEIGHT=StringVar()
WEIGHT=StringVar()
CHARACTER=StringVar()

label=Label(root,text=" MERCY   SCHOOL   STUDENTS   RECORD ",font=("",32,"bold"),fg="black",bg="white")
label.grid(padx=330,pady=20)







frame=Frame(root,bd=10,relief=FLAT,bg="#2c3e50")
frame.place(x=70,y=90,width=450,height=600)
student=Label(frame,text="     STUDENT DETAILS    ",font=("arial",27,"bold"),fg="white",bg="black")
student.grid(row=0,columnspan=2,pady=0)

text1=Label(frame,text=" ADMNNO",font=("arial",15,"bold"),fg="black",bg="white") 
text1.grid(row=1,column=0,pady=15,padx=10,sticky="w")
text2=Entry(frame,textvariable=ADMNNO,font=("times new roman",15,"normal"),bd=3)
text2.grid(row=1,column=1,sticky="w")


text3=Label(frame,text="NAME",font=("arial",15,"bold"),fg="black")
text3.grid(row=2,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text4=Entry(frame,textvariable=NAME,font=("times new roman",15,"normal"),bd=3)
text4.grid(row=2,column=1,sticky="w")

text5=Label(frame,text="CLASS",font=("arial",15,"bold"),fg="black")
text5.grid(row=3,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text6=Entry(frame,textvariable=CLASS,font=("times new roman",15,"normal"),bd=3)
text6.grid(row=3,column=1,sticky="w")

text7=Label(frame,text="CONTACT",font=("arial",15,"bold"),fg="black")
text7.grid(row=4,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text8=Entry(frame,textvariable=CONTACT,font=("times new roman",15,"normal"),bd=3)
text8.grid(row=4,column=1,sticky="w")

text9=Label(frame,text="ADDRESS",font=("arial",15,"bold"),fg="black")
text9.grid(row=5,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text10=Entry(frame,textvariable=ADDRESS,font=("times new roman",15,"normal"),bd=3)
text10.grid(row=5,column=1,sticky="w")

text11=Label(frame,text="D.O.B",font=("arial",15,"bold"),fg="black")
text11.grid(row=6,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text12=Entry(frame,textvariable=dob,font=("times new roman",15,"normal"),bd=3)
text12.grid(row=6,column=1,sticky="w")

text13=Label(frame,text="MENTOR",font=("arial",15,"bold"),fg="black")
text13.grid(row=7,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text14=Entry(frame,textvariable=MENTOR,font=("times new roman",15,"normal"),bd=3)
text14.grid(row=7,column=1,sticky="w")

text15=Label(frame,text="HEIGHT",font=("arial",15,"bold"),fg="black")
text15.grid(row=8,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text16=Entry(frame,textvariable=HEIGHT,font=("times new roman",15,"normal"),bd=3)
text16.grid(row=8,column=1,sticky="w")

text17=Label(frame,text="WEIGHT",font=("arial",15,"bold"),fg="black")
text17.grid(row=9,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text18=Entry(frame,textvariable=WEIGHT,font=("times new roman",15,"normal"),bd=3)
text18.grid(row=9,column=1,sticky="w")

text19=Label(frame,text="CHARACTER",font=("arial",15,"bold"),fg="black")
text19.grid(row=10,column=0,pady=10,padx=10,ipadx=10,sticky="w")
text20=Entry(frame,textvariable=CHARACTER,font=("times new roman",15,"normal"),bd=3)
text20.grid(row=10,column=1,sticky="w")

def get(event):
    #to focus the item  in treeview which  you click

    select=Std_table.focus()
    data=Std_table.item(select)
    global row
    row=data["values"]
    ADMNNO.set(row[0])
    NAME.set(row[1])
    CLASS.set(row[2])
    CONTACT.set(row[3])
    ADDRESS.set(row[4])
    dob.set(row[5])
    MENTOR.set(row[6])
    HEIGHT.set(row[7])
    WEIGHT.set(row[8])
    CHARACTER.set(row[9])







def displayall():
    #this code is for non repition of the rows present in database,children means everything in the treeview
    Std_table.delete(*Std_table.get_children())
    for row in db.fetch():
        Std_table.insert("",END,values=row)
        
    
def adding():
    if text2.get()=="" or text4.get()=="" or text6.get()=="" or text8.get()=="" or text10.get()=="" or text12.get()=="" or text14.get()=="" or text16.get()=="" or text18.get()=="" or text20.get()=="":
        messagebox.showerror(" Sivalingaiit  - ERROR   "," PLEASE FILL ALL THE FIELD ")
        return
    else:
         db.insert(text2.get(),text4.get(),text6.get(),text8.get(),text10.get(),text12.get(),text14.get(),text16.get(),text18.get(),text20.get())
         messagebox.showinfo("Sivalingaiit-CONGRATS","Data added successfully")
         clearall()
         displayall()
    
def updating():

    
    if text2.get()=="" or text4.get()=="" or text6.get()=="" or text8.get()=="" or text10.get()=="" or text12.get()=="" or text14.get()=="" or text16.get()=="" or text18.get()=="" or text20.get()=="":
        messagebox.showerror(" Sivalingaiit  - ERROR   "," PLEASE FILL ALL THE FIELD ")
        return
    else:
        db.update(text2.get(),text4.get(),text6.get(),text8.get(),text10.get(),text12.get(),text14.get(),text16.get(),text18.get(),text20.get())
        messagebox.showinfo("Sivalingaiit-CONGRATS","Data updated successfully")
        clearall()
        displayall()


    
def deleting():
    db.remove(row[0])
    clearall()
    displayall()



   
def clearall():
    ADMNNO.set("")
    NAME.set("")
    CLASS.set("")
    CONTACT.set("")
    ADDRESS.set("")
    dob.set("")
    MENTOR.set("")
    HEIGHT.set("")
    WEIGHT.set("")
    CHARACTER.set("")








   



          
    















button_frame=Frame(root,bd=2,relief=FLAT,bg="teal")
button_frame.place(x=600,y=550,width=730,height=80)

Add_button=Button(button_frame,text="ADD",font=("white",10,"bold"),width=12,command=adding,bg='red',fg='white',bd=0)
Add_button.grid(row=0,column=0,padx=40,pady=28)

Add_button2=Button(button_frame,text="UPDATE",font=("white",10,"bold"),width=12,command=updating,bg='yellow',fg='black')
Add_button2.grid(row=0,column=1,padx=45,pady=28)


Add_button1=Button(button_frame,text="CLEAR",font=("white",10,"bold"),width=12,command=clearall,bg='black',fg='white')
Add_button1.grid(row=0,column=2,padx=45,pady=28)

Add_button3=Button(button_frame,text="DELETE",font=("white",10,"bold"),width=12,command=deleting,bg='green',fg='black')
Add_button3.grid(row=0,column=3,padx=28,pady=28)



    












style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#black",
                rowheight=30,
                fieldbackgrounds="green"
                )
style.map('Treeview',
          background=[('selected','blue')])
def searching():

    try:
        connection=sqlite3.connect("students.db")
        cursor=connection.cursor()
        cursor.execute("select * from Student where ADMNNO="+str(searchbox.get()))
        rows=cursor.fetchall()
        Std_table.delete(*Std_table.get_children())
        if len(rows)!=0:
            for row in rows:
                Std_table.insert("",END,values=row)
        else:
            messagebox.showerror(" Sivalingaiit  - ERROR   ","SEARCH NOT FOUND")
            
        
    except:
        messagebox.showerror(" Sivalingaiit  - ERROR   ","FILL IT ")
            
        
        
def refresh():
    Std_table.delete(*Std_table.get_children())
    
   
    for row in db.fetch():
        Std_table.insert("",END,values=row)
    clearall()
        

        
    
    









search_frame=Frame(root,relief=FLAT,bg="teal")
search_frame.place(x=590,y=100,width=700,height=40)


#search

searchbox=Entry(search_frame,font=("times new roman",20,"bold"),bd=1,width=10)
searchbox.grid(row=0,column=1,ipadx=1,ipady=1,padx=1)

search=Button(search_frame,text="SEARCH ADMNNO",font=("yellow",10,"bold"),command=searching,width=24,bg='orange',fg='black')
search.grid(row=0,column=4,padx=30)

Refresh=Button(search_frame,text="REFRESH",font=("yellow",10,"bold"),command=refresh,width=12,bg='indigo',fg='white')
Refresh.grid(row=0,column=8,padx=30)













frame2=Frame(root,bd=2,relief=FLAT,bg="teal")
frame2.place(x=580,y=150,width=735,height=400)



Table=Frame(frame2,bd=6,bg="teal",relief=FLAT)
Table.place(width=735,height=400)


scroll_x=Scrollbar(Table,orient=HORIZONTAL)
scroll_y=Scrollbar(Table,orient=VERTICAL)

Std_table=ttk.Treeview(Table,columns=(" ADMNNO","NAME","CLASS","CONTACT","ADDRESS","D.O.B","MENTOR","HEIGHT","WEIGHT","CHARACTER"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=Std_table.xview)
scroll_y.config(command=Std_table.yview)

Std_table.heading(" ADMNNO",text=" ADMNNO")
Std_table.heading("NAME",text="NAME")
Std_table.heading("CLASS",text="CLASS")
Std_table.heading("CONTACT",text="CONTACT")
Std_table.heading("ADDRESS",text="ADDRESS",)
Std_table.heading("D.O.B",text="D.O.B")
Std_table.heading("MENTOR",text="MENTOR")
Std_table.heading("HEIGHT",text="HEIGHT")
Std_table.heading("WEIGHT",text="WEIGHT")
Std_table.heading("CHARACTER",text="CHARACTER")

Std_table['show']='headings'

Std_table.column(" ADMNNO",anchor=CENTER,width=150)
Std_table.column("NAME",anchor=CENTER,width=150)
Std_table.column("CLASS",anchor=CENTER,width=150)
Std_table.column("CONTACT",anchor=CENTER,width=150)
Std_table.column("ADDRESS",width=450)
Std_table.column("D.O.B",anchor=CENTER,width=150)
Std_table.column("MENTOR",anchor=CENTER,width=150)
Std_table.column("HEIGHT",anchor=CENTER,width=150)
Std_table.column("WEIGHT",anchor=CENTER,width=150)
Std_table.column("CHARACTER",anchor=CENTER,width=150)
Std_table.bind("<ButtonRelease-1>",get)

Std_table.pack(fill=BOTH,expand=1)







displayall()

root.mainloop()
