#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import filedialog

import mysql.connector
class registration_windows:
    
    def __init__(self,root):
       #####################################Variable###################
        var_fname=StringVar()
        var_lname=StringVar()
        var_contact=StringVar()
        self.var_email=StringVar()
        var_securityQ=StringVar()
        var_securityA=StringVar()
        var_pass=StringVar()
        var_confpass=StringVar()

       
        ###############################function########################
        
        def registration_data():
            if var_fname.get()=="" or self.var_email.get()=="" or var_pass.get()=="":
                msg.showerror("Error","All Field are required",parent=self.root)
            elif var_pass.get()!=var_confpass.get():
                msg.showerror("Error","Password & Confirm Password must be same",parent=self.root)
            elif var_check.get()==0:
                msg.showerror("Error","Pless Agree All Terms & Condition",parent=self.root)
            else:
                try:
                    #msg.showinfo("Success","Welcome In FACE RECOGNITION ATTENDANCE SYSTEM",parent=self.root)
                    conn=mysql.connector.connect(host = 'localhost',
                                                  user=' root',
                                                  password='12345',
                                                  database='face_registration')
                    my_cursor=conn.cursor()
                    query = ("select email from registration where email=%s")
                    value=(self.var_email.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    if row!=None:
                        msg.showerror("Error","User already exist,please try another email",parent=self.root)
                    else:

                        my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                            var_fname.get(),
                            var_lname.get(),
                            var_contact.get(),
                            self.var_email.get(),
                            var_securityQ.get(),
                            var_securityA.get(),
                            var_pass.get()             
                             ))
                        conn.commit()

                        conn.close()

                        msg.showinfo("Success","Registration has Successfully",parent=self.root)
                        self.root.destroy()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    self.root.destroy()
         
        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Registration System")
         # top image
        
        # bg image
        image1 = Image.open(r"image/image51 (2).jpg")
        image1=image1.resize((1380,730), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(image1)
        bg=Label(self.root,image=self.photo1)
        bg.place(x=0,y=0,width=1380,height=730)
        # title
        title=Label(bg,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),fg="white",bg="darkblue")
        title.place(x=0,y=0,width=1380,height=45)
        
        image2= Image.open(r"image/image51 (1).jpg")
        image2=image2.resize((400,500), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(image2)
        bg_1=Label(bg,image=self.photo2)
        bg_1.place(x=100,y=140,width=400,height=500)
        
        frame=Frame(bg,bg="white")
        frame.place(x=500,y=140,width=700,height=500)
        
        login=Label(frame,text="REGISTRATION HERE",font=("times new roman",20,"bold"),bg="red",fg="white")
        login.place(x=20,y=20)
        
        ####row 1
        user_first_name=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        user_first_name.place(x=50,y=100)
        user_first_name=ttk.Entry(frame,textvariable=var_fname,width=20,font=("times new roman",12,"bold"))
        user_first_name.place(x=50,y=130,width=250)
        
        user_last_name=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        user_last_name.place(x=370,y=100)
        user_last_name=ttk.Entry(frame,textvariable=var_lname,width=20,font=("times new roman",12,"bold"))
        user_last_name.place(x=370,y=130,width=250)
        
        ###row2
        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        contact=ttk.Entry(frame,textvariable=var_contact,width=20,font=("times new roman",12,"bold"))
        contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        email=ttk.Entry(frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email.place(x=370,y=200,width=250)
        
         ###row3
        
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        security_Q=ttk.Combobox(frame,textvariable=var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        security_Q["values"]=("Select","Your Birth Place","Your Favorite Book ","Your Pet Name","Your Best Friend Name")
        security_Q.current(0)
        security_Q.place(x=50,y=270,width=250)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)
        security_a=ttk.Entry(frame,textvariable=var_securityA,width=20,font=("times new roman",12,"bold"))
        security_a.place(x=370,y=270,width=250)
        
         ###row4
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        pswd=ttk.Entry(frame,textvariable=var_pass,width=20,font=("times new roman",12,"bold"))
        pswd.place(x=50,y=340,width=250)
        
        con_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        con_pswd.place(x=370,y=310)
        con_pswd=ttk.Entry(frame,textvariable=var_confpass,width=20,font=("times new roman",12,"bold"))
        con_pswd.place(x=370,y=340,width=250)
        
        
        ####checkbutton#########
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree The Terms & Condtion",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        ######Button############
        registration_button=Button(frame,command=registration_data,text="New User Registration",cursor="hand2",font=("times new roman",15,"bold"),borderwidth=0,bg="darkgreen",fg="white",activeforeground="white",activebackground="red")
        registration_button.place(x=50,y=420,width=250,height=40)
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=registration_windows(root)
    root.mainloop()
    

