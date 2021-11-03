from tkinter import *
# from PIL import image
from tkinter import ttk


window=Tk()


window.geometry('1350x700+0+0')
window.config(background='powder blue')
lbl1=Label(window,text="SHANGLA PUBLIC SCHOOL & COLAGE BESHAM",font=("time new roman",30,"bold"),bg='powder blue',fg="blue")
lbl1.place(x=270,y=30)
#-------- frame1-------------
StdID=StringVar()
Name=StringVar()
fatherN=StringVar()
Cls=StringVar()
gender=StringVar()
Adrs=StringVar()

frame1=Frame(window,bd=3,bg='powder blue',relief=RIDGE)
frame1.place(x=10,y=80,width=750,height=620,)
lbl2=Label(frame1,text="Student Details",font=("time new roman",20,"bold"),bg='powder blue',fg="blue")
lbl2.place(x=300,y=20)

lbl3=Label(frame1,text="Student ID",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl3.place(x=20,y=60)
StdntID=Entry(frame1,font=("time new roman",15,"bold"),bg='light gray',fg="red",textvariable=StdID)
StdntID.place(x=180,y=60)

lbl4=Label(frame1,text="Student Name",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl4.place(x=20,y=100)
StdntNm=Entry(frame1,font=("time new roman",15,"bold"),bg='light gray',fg="red",textvariable=Name)
StdntNm.place(x=180,y=100)

lbl5=Label(frame1,text="Father Name",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl5.place(x=20,y=140)
Text5fn=Entry(frame1,font=("time new roman",15,"bold"),bg='light gray',fg="red",textvariable=fatherN)
Text5fn.place(x=180,y=140)

lbl6=Label(frame1,text="Class",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl6.place(x=20,y=180)
Text6cls=Entry(frame1,font=("time new roman",15,"bold"),bg='light gray',fg="red",textvariable=Cls)
Text6cls.place(x=180,y=180)

lbl7=Label(frame1,text="Gender",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl7.place(x=20,y=220)
clscombo=ttk.Combobox(frame1,values=("Female","Male"))
clscombo.place(x=180,y=220,width=220,height=30)

lbl8=Label(frame1,text="Adress",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl8.place(x=20,y=260)
Text8adrs=Entry(frame1,font=("time new roman",15,"bold"),bg='light gray',fg="red",textvariable=Adrs)
Text8adrs.place(x=180,y=260)


#================Functions=================
def Reciept():
    New_sample = f'''\t SPS\n\t Adress: Besham
    -------------------------------------------
    Student ID\t\t:{StdID.get()}
    Name\t\t:{Name.get()}
    Father Name\t\t:{fatherN.get()}
    Class\t\t:{Cls.get()}
    Date\t\t:MM-YYYY
    Generted on\t\t:
    -------------------------------------------
    Tution Fee\t\t:Rs----
    Admission Fee\t\t:Rs----
    Exam Fee\t\t:Rs----
    Books & uniform\t\t:
    other\t\t:
    Total Payment\t\t:
    ------------------------------------------
    This is computer generted slip not required any signature 
    '''
    fee_reciept.delete('1.0',END)
    fee_reciept.insert(END,New_sample)
def Clr():
    StdID.set("")
    Name.set("")
    fatherN.set("")
    Cls.set("")
    gender.set("")
    Adrs.set("")


btn1update=Button(frame1,text="Update",font=("time new roman",15,"bold"),bg='light gray',fg="red")
btn1update.place(x=100,y=500,width=100,height=50)

btn1search=Button(frame1,text="Search",font=("time new roman",15,"bold"),bg='light gray',fg="red")
btn1search.place(x=210,y=500,width=100,height=50)

btn1Print=Button(frame1,text="Print",font=("time new roman",15,"bold"),bg='light gray',fg="red")
btn1Print.place(x=310,y=500,width=100,height=50)

btn1clr=Button(frame1,text="Clear",font=("time new roman",15,"bold"),bg='light gray',fg="red",command=Clr)
btn1clr.place(x=410,y=500,width=100,height=50)

btn1dlt=Button(frame1,text="Delete",font=("time new roman",15,"bold"),bg='light gray',fg="red")
btn1dlt.place(x=520,y=500,width=100,height=50)

btn1rcpt=Button(frame1,text="Reciept",font=("time new roman",15,"bold"),bg='light gray',fg="red",command=Reciept)
btn1rcpt.place(x=620,y=500,width=100,height=50)

#---------frame2---------
frame2=Frame(window,bd=3,bg='powder blue',relief=RIDGE)
frame2.place(x=770,y=80,width=570,height=300)
lbl9=Label(frame2,text="FEE details",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl9.place(x=250,y=0)

lbl10=Label(frame2,text="Month",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl10.place(x=10,y=40)

text10tf=Entry(frame2,font=("time new roman",15,"bold"),bg='light gray',fg="red")
text10tf.place(x=140,y=40,width=80)

lbl11=Label(frame2,text="Year",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl11.place(x=230,y=40,width=80)
text11yr=Entry(frame2,font=("time new roman",15,"bold"),bg='light gray',fg="red")
text11yr.place(x=300,y=40,width=80)

lbl11=Label(frame2,text="Admission Fee",font=("time new roman",15,"bold"),bg='powder blue',fg="red")
lbl11.place(x=10,y=100)

text11Month=Entry(frame2,font=("time new roman",15,"bold"),bg='light gray',fg="red")
text11Month.place(x=160,y=100)

#--------fram3_-----------------
frame3=Frame(window,bd=5,bg='white',relief=RIDGE)
frame3.place(x=770,y=390,width=570,height=310)

lbl12=Label(frame3,text="---- Fee Reciept ----",font=("time new roman",15,"bold"),bg='white',fg="red")
lbl12.place(x=200,y=0)
FeeRecipt=Frame(frame3,bd=5,bg='white',relief=RIDGE)
FeeRecipt.place(x=0,y=40,width=570,height=265)
scroll_y=Scrollbar(FeeRecipt,orient=VERTICAL)
scroll_y.pack(fill=Y,side=RIGHT)
fee_reciept=Text(FeeRecipt,font=("time new roman",10,"bold"),bg='white',fg="red",yscrollcommand=scroll_y.set)
fee_reciept.pack()
scroll_y.config(command=fee_reciept)
sample=f'''\t SPS\n\t Adress: Besham
-------------------------------------------
Student ID\t\t:
Name\t\t:
Father Name\t\t:
Class\t\t:
Date\t\t:MM-YYYY
Generted on\t\t:
-------------------------------------------
Tution Fee\t\t:Rs----
Admission Fee\t\t:Rs----
Exam Fee\t\t:Rs----
Books & uniform\t\t:
other\t\t:
Total Payment\t\t:
------------------------------------------
This is computer generted slip not required any signature 
'''
fee_reciept.insert(END,sample)
def check_con():
    pass










window.mainloop()
