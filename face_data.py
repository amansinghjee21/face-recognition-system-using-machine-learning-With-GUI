#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
from tkinter import *

from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
################################### importing scripts

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

class face_recognation:
    def __init__(self,root):
        
       
        def add_excel(ids,roll,name,department,sem,course):
            now=datetime.now()
            d1=now.strftime("%d/%m/%y")
            dtString=now.strftime("%H:%M:%S")


            if sem == "1":
                path='data/Attendance_xlsx/first_year_1.xlsx'
                d=pd.read_excel(path)
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel( path)

            elif sem == "2":
                path='data/Attendance_xlsx/first_year_2.xlsx'
                d=pd.read_excel(path)
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel( path)   

            elif sem == "3":
                path='data/Attendance_xlsx/second_year_3.xlsx'
                d=pd.read_excel(path)        
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel ( path)              

            elif sem == "4":
                path='data/Attendance_xlsx/second_year_4.xlsx'
                d=pd.read_excel(path)        
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel ( path)          
            elif sem == "5":
                path='data/Attendance_xlsx/third_year_5.xlsx'
                d=pd.read_excel(path)         
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel ( path)          
            elif sem == "6":

                path='data/Attendance_xlsx/third_year_6.xlsx'
                d=pd.read_excel(path)            
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel ( path)         
            elif sem == "7":
                path='data/Attendance_xlsx/forth_year_7.xlsx'
                d=pd.read_excel(path)
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel ( path)         
            elif sem == "8":
                path='data/Attendance_xlsx/forth_year_8.xlsx'
                d=pd.read_excel(path)           
                df={"Id":ids,"Name":name,"Roll No":roll,"Department":department,"Course":course,"Semester":sem,"Date":d1,"Time":dtString}
                d=d.concat(df,ignore_index=True)
                d.drop(columns=d.columns[0],axis=1,inplace=True)
                d.to_excel( path)

        def add_data(ids,roll,name,department,semester,course):
            now=datetime.now()
            d1=now.strftime("%d/%m/%y")
            dtString=now.strftime("%H:%M:%S")
            def add_database():
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                conn=mysql.connector.connect(host = 'localhost',
                                      user=' root',
                                      password='12345',
                                      database='face_registration')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_attendance values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                ids,
                roll,
                name,
                department,
                course,
                semester,
                d1,
                dtString
                 ))
                conn.commit()
                conn.close()

            conn=mysql.connector.connect(host = 'localhost',
                                      user=' root',
                                      password='12345',
                                      database='face_registration')
            my_cursor=conn.cursor()

            query = "select date from student_attendance where id={}".format(ids)
            my_cursor.execute(query)
            data=my_cursor.fetchall()
            l=len(data)
            data_date=[]
            if data==[]:
                data_date=[]
            else:
                for i in range(0,l):
                    data_date.append(data[i][0])
            conn.commit()
            conn.close()
            if (d1 not in data_date):
                add_database()
                add_excel(ids,roll,name,department,semester,course)
            elif data_date==[]:
                add_database()
                add_excel(ids,roll,name,department,semester,course)







        def face_recog():
            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                for (x,y,w,h) in features:

                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    stu_id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn=mysql.connector.connect(host = 'localhost',
                                                  user=' root',
                                                  password='12345',
                                                  database='face_registration')
                    my_cursor=conn.cursor()
                    my_cursor.execute("select name from student where id="+str(stu_id))
                    n=my_cursor.fetchone()
                    if n:
                        n = n[0]
                    else:
                        n = ""

                    my_cursor=conn.cursor()
                    my_cursor.execute("select roll from student where id="+str(stu_id))
                    r=my_cursor.fetchone()
                    if r:
                        r = r[0]
                    else:
                        r = ""
            

                    my_cursor=conn.cursor()
                    my_cursor.execute("select dep from student where id="+str(stu_id))
                    d=my_cursor.fetchone()
                    if d:
                        d = d[0]
                    else:
                        d = ""

                    my_cursor=conn.cursor()
                    my_cursor.execute("select course from student where id="+str(stu_id))
                    c=my_cursor.fetchone()
                    if c:
                        c = c[0]
                    else:
                        c = ""

                    my_cursor=conn.cursor()
                    my_cursor.execute("select sem from student where id="+str(stu_id))
                    s=my_cursor.fetchone()
                    if s:
                        s = s[0]
                    else:
                        s = ""

                    my_cursor=conn.cursor()
                    my_cursor.execute("select id from student where id="+str(stu_id))
                    i=my_cursor.fetchone()
                    if i:
                        i = i[0]
                    else:
                        i = ""


                    if confidence>80:
                        cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,50,50),3)
                        cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,50,50),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,50,50),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,50,50),3)
                        add_data(i,r,n,d,s,c)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    coord=[x,y,w,y]
                return coord


            def recognize(img,clf,faceCascade):

                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("trainer/classifier.xml")

            video_cap=cv2.VideoCapture(0)
            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()
           

        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Fce Rcognation System")
        title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.place(x=0,y=0,width=1380,height=55)

        image_top= Image.open(r"image/image29.jpg")
        image_top=image_top.resize((685,660), Image.LANCZOS)
        self.photo_top = ImageTk.PhotoImage(image_top)
        f1=Label(self.root,image=self.photo_top)
        f1.place(x=0,y=55,width=685,height=660)

        image_bottom= Image.open(r"image/image30.jpg")
        image_bottom=image_bottom.resize((685,660), Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(image_bottom)
        f1=Label(self.root,image=self.photo_bottom)
        f1.place(x=685,y=55,width=685,height=660)

        bt_img=Button(f1,text="Face Recognition",command=face_recog,cursor="hand2",width=11,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        bt_img.place(x=240,y=585,width=200,height=40)

if __name__=="__main__":
    root=Tk()
    obj=face_recognation(root)
    root.mainloop()


# In[ ]:




