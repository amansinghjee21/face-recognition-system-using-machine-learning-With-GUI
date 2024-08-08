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
from registration import registration_windows
from faceattendance_main import face_recognition_system
from forgot_password import forgot_password_window

import os
import time
class login_windows:
    def registr_window(self):
        self.new_window=Toplevel(self.root)    
        self.app=registration_windows(self.new_window)
        
    def forgot_pass_window(self):
        self.new_window=Toplevel(self.root)    
        self.app=forgot_password_window(self.new_window)
        
        
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Login System")
        global var_email,var_pass
        var_email=StringVar()
        var_pass=StringVar()
        
        
        def user_login():
            if var_email.get()=="" or var_pass.get()=="":
                msg.showerror("Error","All field required",parent=self.root)
            else:
                conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from registration where email=%s and password=%s",(
                    var_email.get(),
                    var_pass.get()
                                  ))
                row=my_cursor.fetchone()
                if row==None:
                    msg.showerror("Error","Inavalid Email & Password",parent=self.root)
                else:
                    open_main=msg.askyesno("YesNo","Access Only Admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=face_recognition_system(self.new_window)
                       
                       
                       
                    else:
                        if not open_main:
                            return
                conn.commit()
               
                conn.close()
            

        # bg image
        image3 = Image.open(r"image/image99.jpg")
        image3=image3.resize((1380,730), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=0,width=1380,height=730)
        # title
        title=Label(bg,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.place(x=0,y=0,width=1380,height=45)
        
        frame=Frame(bg,bg="black")
        frame.place(x=220,y=150,width=400,height=450)
        
        login=Label(frame,text="Log In",font=("times new roman",25,"bold"),bg="black",fg="red")
        login.place(x=150,y=10)
        
        user_email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        user_email.place(x=80,y=80)

        user_email=ttk.Entry(frame,textvariable=var_email,width=12,font=("times new roman",12,"bold"))
        user_email.place(x=50,y=110,width=300,height=35)
        
        
        user_password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        user_password.place(x=80,y=150)

        user_password=ttk.Entry(frame,textvariable=var_pass,width=12,font=("times new roman",12,"bold"))
        user_password.place(x=50,y=180,width=300,height=35)
        
        login_button=Button(frame,command=user_login,text="Login",cursor="hand2",font=("times new roman",15,"bold"),borderwidth=0,bg="darkgreen",fg="white",activeforeground="white",activebackground="red")
        login_button.place(x=130,y=250,width=120,height=40)
        
        registration_button=Button(frame,text="New User Registration",command=self.registr_window,cursor="hand2",font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="red")
        registration_button.place(x=20,y=310,width=150,height=40)
        
        forget_button=Button(frame,text="Forget Password",command=self.forgot_pass_window,cursor="hand2",font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="red")
        forget_button.place(x=20,y=350,width=120,height=40)
        

        
        
if __name__=="__main__":
    
    root=Tk()
    obj=login_windows(root)
    root.mainloop()
    


# In[ ]:
