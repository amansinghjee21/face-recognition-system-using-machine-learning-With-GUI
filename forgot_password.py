#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import filedialog
import mysql.connector



import os

class forgot_password_window:
   
        
    def __init__(self,root):
       
        var_email=StringVar()
        var_securityQ=StringVar()
        var_securityA=StringVar()
        var_for_pass=StringVar()
        
        def forgot_password():
            if var_email.get()=="" or var_securityQ.get()=="" or var_securityA.get()=="" or var_for_pass.get()=="":
                msg.showerror("Error","All Field are required",parent=self.root)
            else:
                conn=mysql.connector.connect(host = 'localhost',
                                                      user=' root',
                                                      password='',
                                                      database='face_registration')
                my_cursor=conn.cursor()
                query = ("select * from registration where email=%s")
                value=(var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                print(row)
                if row==None:
                    msg.showerror("Error","Pless enter the valid email id",parent=self.root)
                else:
                    query = ("select * from registration where email=%s and securityQ=%s and securityA=%s")
                    value=(var_email.get(),var_securityQ.get(),var_securityA.get())
                    my_cursor.execute(query,value)
                    data=my_cursor.fetchone()
                    if data==None:
                        msg.showerror("Error","Inavalid Security Questions & Security Answer",parent=self.root)
                    else:
                        query = ("update registration set password=%s where email=%s")
                        value=(var_for_pass.get(),var_email.get(),)
                        my_cursor.execute(query,value)
                        conn.commit()                
                        conn.close()
                        msg.showinfo("Success","Your password has been reset,pless login new password",parent=self.root)
                        self.root.destroy()
                
                
        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Login System")
        image3 = Image.open(r"image/image99.jpg")
        image3=image3.resize((1380,730), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=0,width=1380,height=730)
        # title
        title=Label(bg,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.place(x=0,y=0,width=1380,height=45)
        
        frame=Frame(bg,bg="black")
        frame.place(x=220,y=150,width=400,height=500)
        
        login=Label(frame,text="Forgot Password",font=("times new roman",25,"bold"),bg="black",fg="red")
        login.place(x=75,y=10)
        
        user_email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        user_email.place(x=80,y=80)

        user_email=ttk.Entry(frame,textvariable=var_email,width=12,font=("times new roman",12,"bold"))
        user_email.place(x=50,y=110,width=300,height=35)
        
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.place(x=80,y=150)
        security_Q=ttk.Combobox(frame,textvariable=var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        security_Q["values"]=("Select","Your Birth Place","Your Favorite Book ","Your Pet Name","Your Best Friend Name")
        security_Q.place(x=50,y=180,width=300,height=35)
        security_Q.current(0)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_a.place(x=80,y=230)
        security_a=ttk.Entry(frame,textvariable=var_securityA,width=20,font=("times new roman",12,"bold"))
        security_a.place(x=50,y=260,width=300,height=35)
        
        user_password=Label(frame,text="New Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        user_password.place(x=80,y=310)

        user_password=ttk.Entry(frame,textvariable=var_for_pass,width=20,font=("times new roman",12,"bold"))
        user_password.place(x=50,y=340,height=35,width=300)
        
        reset_button=Button(frame,text="Reset",command=forgot_password,cursor="hand2",font=("times new roman",15,"bold"),borderwidth=0,bg="darkgreen",fg="white",activeforeground="white",activebackground="red")
        reset_button.place(x=130,y=400,width=120,height=40)
        
        
if __name__=="__main__":
    root=Tk()
    obj=forgot_password_window(root)
    root.mainloop()


# In[ ]:




