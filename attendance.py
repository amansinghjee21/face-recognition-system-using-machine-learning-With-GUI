#!/usr/bin/env python
# coding: utf-8

# In[14]:


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
class attendance:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Attendance System")


        var_dep=StringVar()
        var_sem=StringVar()
        var_course=StringVar()
        var_id=StringVar()
        var_name=StringVar()

        var_roll=StringVar()
        var_time=StringVar()
        var_date=StringVar()
        var_search=StringVar()
        var_data=StringVar()

        def fetch_data():
            conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student_attendance")
            data=my_cursor.fetchall()
            if len(data)!=0:
                Attendance_table.delete(*Attendance_table.get_children())
                for i in data:
                    Attendance_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        def get_cursor(event=""):
            cursor_focus=Attendance_table.focus()
            content=Attendance_table.item(cursor_focus)
            data=content["values"]

            var_id.set(data[0]),
            var_roll.set(data[1]),
            var_name.set(data[2]),
            var_dep.set(data[3]),
            var_course.set(data[4]),
            var_sem.set(data[5]),

            var_date.set(data[6]),
            var_time.set(data[7]),

        def update_data():
            if var_dep.get()=="Select Department" or var_name.get()=="" or var_id.get()=="":       
                msg.showerror("Error","All Field are required",parent=self.root)
            else:
                try:
                    Update=msg.askyesno("Update","Do you want to update this student details",parent=self.root,)
                    if Update>0:
                        conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student_attendance set dep=%s,course=%s,sem=%s,name=%s,roll=%s,date=%s,time=%s where id=%s",(
                        var_dep.get(),
                        var_course.get(),
                        var_sem.get(),
                        var_name.get(),
                        var_roll.get(),
                        var_date.get(),
                        var_time.get(),
                        var_id.get()


                                    ))
                    else:
                        if not Update:
                            return
                    msg.showinfo("Success","Student details successfully update completed",parent=self.root)


                    conn.commit()
                    fetch_data()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        def delete_data():
            if var_id.get()=="":
                msg.showerror("Error","Student id must be required",parent=self.root)
            else:
                try:
                    delete=msg.askyesno("Student Delete Page","Do you want to delete this student attendance",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                        s=var_id.get()

                        my_cursor=conn.cursor()
                        query = "delete from student_attendance where id={}".format(s)
                        my_cursor.execute(query)

                        fetch_data()


                    else:
                        if not delete:
                            return



                    conn.commit()
                    conn.close()

                    msg.showinfo("Delete","Successfully deleted select student details",parent=self.root)
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        def reset_data():
            var_id.set(""),
            var_roll.set(""),
            var_name.set(""),
            var_dep.set("Select Department"),
            var_course.set("Select Course"),
            var_sem.set("Select Semester "),
            var_date.set(""),
            var_time.set("")
        def search_data():
            conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')


            my_cursor=conn.cursor()
            if var_search.get()=="Roll No":
                try:
                    s=var_data.get()
                    query = "select * from student_attendance where roll={}".format(s)
                    my_cursor.execute(query)


                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        Attendance_table.delete(*Attendance_table.get_children())
                        for i in data:
                            Attendance_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            elif var_search.get()=="Id":
                try:
                    s=var_data.get()
                    query = "select * from student_attendance where id={}".format(s)
                    my_cursor.execute(query)


                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        Attendance_table.delete(*Attendance_table.get_children())
                        for i in data:
                            Attendance_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            elif var_search.get()=="Date":
                try:

                    s=var_data.get()
                    query = "select * from student_attendance where date={}".format(s)
                    my_cursor.execute(query)


                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        Attendance_table.delete(*Attendance_table.get_children())
                        for i in data:
                            Attendance_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)





        image_top= Image.open(r"image/image29.jpg")
        image_top=image_top.resize((690,130), Image.LANCZOS)
        self.photo_top = ImageTk.PhotoImage(image_top)
        f1=Label(self.root,image=self.photo_top)
        f1.place(x=0,y=0,width=690,height=130)




        image_bottom= Image.open(r"image/image30.jpg")
        image_bottom=image_bottom.resize((690,130), Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(image_bottom)
        f1=Label(self.root,image=self.photo_bottom)
        f1.place(x=690,y=0,width=690,height=130)

        image3 = Image.open(r"image/image15.jpg")
        image3=image3.resize((1380,530), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=130,width=1380,height=600)

        title=Label(bg,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=0,width=1380,height=45)

        main_frame=Frame(bg,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1380,height=530)
        #right label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=670,height=518)

        image_left= Image.open(r"image/image2.jpg")
        image_left=image_left.resize((660,130), Image.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(image_left)
        f1=Label(left_frame,image=self.photo_left)
        f1.place(x=5,y=0,width=660,height=130)


        # current course
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=135,width=660,height=115)
        #department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,stick=W)

        dep_combo=ttk.Combobox(current_course,textvariable=var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CS","IT","BCOM","B.A")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,stick=W)

        # current course

        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,stick=W)

        course_combo=ttk.Combobox(current_course,textvariable=var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CS","IT","BCOM","B.A")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,stick=W)



        # Semester

        sem_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,stick=W)

        sem_combo=ttk.Combobox(current_course,textvariable=var_sem,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,stick=W)
        # Class student information
        inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        inside_frame.place(x=5,y=250,width=660,height=240)

        #id
        idlabel=Label(inside_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        idlabel.grid(row=0,column=0,padx=10,pady=5,stick=W)

        atten_id=ttk.Entry(inside_frame,textvariable=var_id,width=20,font=("times new roman",12,"bold"))
        atten_id.grid(row=0,column=1,padx=10,pady=5,stick=W)
        #name
        namelabel=Label(inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        namelabel.grid(row=0,column=2,padx=10,pady=5,stick=W)

        atten_name=ttk.Entry(inside_frame,textvariable=var_name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=0,column=3,padx=10,pady=5,stick=W)
        #Rollno
        rolllabel=Label(inside_frame,text="Roll NO:",font=("times new roman",12,"bold"),bg="white")
        rolllabel.grid(row=1,column=0,padx=10,pady=5,stick=W)

        atten_roll=ttk.Entry(inside_frame,textvariable=var_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=1,column=1,padx=10,pady=5,stick=W)



        #date
        courselabel=Label(inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        courselabel.grid(row=1,column=2,padx=10,pady=5,stick=W)

        atten_course=ttk.Entry(inside_frame,textvariable=var_date,width=20,font=("times new roman",12,"bold"))
        atten_course.grid(row=1,column=3,padx=10,pady=5,stick=W)

        #time
        semlabel=Label(inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        semlabel.grid(row=2,column=0,padx=10,pady=5,stick=W)

        atten_sem=ttk.Entry(inside_frame,textvariable=var_time,width=20,font=("times new roman",12,"bold"))
        atten_sem.grid(row=2,column=1,padx=10,pady=5,stick=W)

         # button frame
        btn_frame=Frame(inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=655,height=35)

        update=Button(btn_frame,text="Update",command=update_data,cursor="hand2",width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=0)

        delete=Button(btn_frame,text="Delete",command=delete_data,cursor="hand2",width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=1)



        reset=Button(btn_frame,text="Reset",command=reset_data,cursor="hand2",width=22,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=2)




        #left label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=660,height=518)


        image_right= Image.open(r"image/image2.jpg")
        image_right=image_left.resize((660,130), Image.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(image_right)
        f1=Label(right_frame,image=self.photo_left)
        f1.place(x=5,y=0,width=660,height=130)

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)

        search_label=Label(search_frame,text="Search Bar:",font=("times new roman",15,"bold"),fg="white",bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        search_combo=ttk.Combobox(search_frame,textvariable=var_search,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Id","Roll No","Date")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,stick=W)

        search=ttk.Entry(search_frame,textvariable=var_data,width=15,font=("times new roman",12,"bold"))
        search.grid(row=0,column=2,padx=3,pady=5,stick=W)

        search=Button(search_frame,text="Search",command=search_data,cursor="hand2",width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search.grid(row=0,column=3,padx=3)

        showall=Button(search_frame,text="Show All",command=fetch_data,cursor="hand2",width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall.grid(row=0,column=4,padx=3)

        ######################scroll bar table###########################
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=280)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        global Attendance_table
        Attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","dep","course","sem","date","time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X),
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Attendance_table.xview)
        scroll_y.config(command=Attendance_table.yview)

        Attendance_table.heading("id",text="StudentID")
        Attendance_table.heading("roll",text="Roll")
        Attendance_table.heading("name",text="Name")
        Attendance_table.heading("dep",text="Department")
        Attendance_table.heading("course",text="Course")   
        Attendance_table.heading("sem",text="Semester") 
        Attendance_table.heading("date",text="Date") 
        Attendance_table.heading("time",text="Time")

        Attendance_table["show"]="headings"

        Attendance_table.column("id",width=100)
        Attendance_table.column("roll",width=100)
        Attendance_table.column("name",width=100)
        Attendance_table.column("dep",width=100)
        Attendance_table.column("course",width=100)  
        Attendance_table.column("sem",width=100) 
        Attendance_table.column("date",width=100) 
        Attendance_table.column("time",width=100) 

        Attendance_table.pack(fill=BOTH,expand=1)
        fetch_data()
        #######################fetch data############################
        Attendance_table.bind("<ButtonRelease>",get_cursor)
    
if __name__=="__main__":    
    root=Tk()

    obj=attendance(root)
    root.mainloop()


# In[ ]:




