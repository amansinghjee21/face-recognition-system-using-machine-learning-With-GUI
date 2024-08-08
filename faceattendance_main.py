#!/usr/bin/env python
# coding: utf-8

# In[15]:



import tkinter as tk
from tkinter import *

from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
################################### importing scripts###########################
from train import train
from student import student
from face_data import face_recognation
from attendance import attendance
################################### lib to perform CRUD operations in csv/excel
from PIL import Image, ImageTk
from openpyxl import *
import pandas as pd
import numpy as np
import cv2,os
from cv2 import cvtColor
import csv
################################### other dependencies
import datetime
from time import strftime
from datetime import datetime
import os
class face_recognition_system:
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
    def face_dection(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognation(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
    
    
    
    
    
    def __init__(self,root):
        
        def open_img():
            os.startfile(r"C:/Users/aman singh/Desktop/Automated-Attendance-System/dataset/TrainingImage")
        def iExit():
            iExit=msg.askyesno("Face Recognition","Are you sure exit this app",parent=self.root)
            if iExit>0:
                root.destroy()
            else:
                return
        self.root=root
        
        self.root.geometry("1380x730+0+0")
        self.root.title("Home")

        # top image
        image = Image.open(r"image/image19.jpg")
        image=image.resize((450,130), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        f1=Label(self.root,image=self.photo)
        f1.place(x=0,y=0,width=450,height=130)

        image1 = Image.open(r"image/image50.jpg")
        image1=image1.resize((450,130), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(image1)
        f1=Label(self.root,image=self.photo1)
        f1.place(x=450,y=0,width=450,height=130)

        image2 = Image.open(r"image/image21.jpg")
        image2=image2.resize((500,130), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(image2)
        f1=Label(self.root,image=self.photo2)
        f1.place(x=900,y=0,width=500,height=130)
        # bg image
        image3 = Image.open(r"image/image45.jpg")
        image3=image3.resize((1380,600), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=130,width=1380,height=600)
        # title
        title=Label(bg,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=0,width=1380,height=45)


        # student button
        image4 = Image.open(r"image/image9.jpg")
        image4=image4.resize((200,200), Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(image4)

        b1=Button(bg,image=self.photo4,cursor="hand2",command=self.student_details)
        b1.place(x=100,y=50,width=200,height=200)
        b1_1=Button(bg,text="Student Registration",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=230,width=200,height=40)
        # Face Detector
        image5 = Image.open(r"image/image10.jpg")
        image5=image5.resize((200,200), Image.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(image5)

        b1=Button(bg,image=self.photo5,cursor="hand2",command=self.face_dection)
        b1.place(x=400,y=50,width=200,height=200)

        b1_1=Button(bg,text="Face Detector",cursor="hand2",command=self.face_dection,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=230,width=200,height=40)
        # Attendance
        image6 = Image.open(r"image/image13.jpg")
        image6=image6.resize((200,200), Image.LANCZOS)
        self.photo6= ImageTk.PhotoImage(image6)

        b1=Button(bg,image=self.photo6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=50,width=200,height=200)

        b1_1=Button(bg,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=230,width=200,height=40)
        # Train Data
        image7 = Image.open(r"image/image11.jpg")
        image7=image7.resize((200,200), Image.LANCZOS)
        self.photo7= ImageTk.PhotoImage(image7)

        b1=Button(bg,image=self.photo7,cursor="hand2",command=self.train_data)
        b1.place(x=1000,y=50,width=200,height=200)

        b1_1=Button(bg,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=230,width=200,height=40)
        # Photos
        image8 = Image.open(r"image/image14.jpg")
        image8=image8.resize((200,200), Image.LANCZOS)
        self.photo8= ImageTk.PhotoImage(image8)

        b1=Button(bg,image=self.photo8,command=open_img,cursor="hand2")
        b1.place(x=100,y=300,width=200,height=200)

        b1_1=Button(bg,text="Photos",cursor="hand2",command=open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=480,width=200,height=40)
        # Update
        image9 = Image.open(r"image/image15.jpg")
        image9=image9.resize((200,200), Image.LANCZOS)
        self.photo9= ImageTk.PhotoImage(image9)

        b1=Button(bg,image=self.photo9,cursor="hand2",command=self.student_details)
        b1.place(x=400,y=300,width=200,height=200)

        b1_1=Button(bg,text="Update",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=480,width=200,height=40)
        
        # Exit Desk
        image11 = Image.open(r"image/image16.jpg")
        image11=image11.resize((200,200), Image.LANCZOS)
        self.photo11= ImageTk.PhotoImage(image11)

        b1=Button(bg,image=self.photo11,cursor="hand2",command=iExit)
        b1.place(x=700,y=300,width=200,height=200)

        b1_1=Button(bg,text="Exit",cursor="hand2",command=iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=480,width=200,height=40)
    


if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()

# In[ ]:




