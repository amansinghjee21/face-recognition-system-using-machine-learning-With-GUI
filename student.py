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

class student:
    def __init__(self,root):


        self.root=root
        self.root.geometry("1380x730+0+0")
        self.root.title("Student Details System")
                ##############Variables###############



        var_dep=StringVar()
        var_course=StringVar()
        var_year=StringVar()
        var_sem=StringVar()
        var_id=StringVar()
        var_name=StringVar()
        var_en=StringVar()
        var_roll=StringVar()
        var_gender=StringVar()
        var_dob=StringVar()
        var_email=StringVar()
        var_phone=StringVar()
        var_data=StringVar()
        var_search=StringVar()

        def add_data():

            if var_dep.get()=="Select Department" or var_name.get()=="" or var_id.get()=="":
                msg.showerror("Error","All Field are required",parent=self.root)
            else:


                try:

                    conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                     var_id.get(),
                     var_dep.get(),
                     var_course.get(),
                     var_year.get(),
                     var_sem.get(),
                     var_name.get(),
                     var_en.get(),
                     var_roll.get(),
                     var_gender.get(),
                     var_dob.get(),
                     var_email.get(),
                     var_phone.get() ,
                     var_radio1.get()                     
                     ))
                    conn.commit()
                    fetch_data()
                    conn.close()

                    msg.showinfo("Success","Student details has been added Successfully",parent=self.root)
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        # ======================fetch_data==========================

        def fetch_data():
            conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            if len(data)!=0:
                student_table.delete(*student_table.get_children())
                for i in data:
                    student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        def get_cursor(event=""):
            cursor_focus=student_table.focus()
            content=student_table.item(cursor_focus)
            data=content["values"]
            
            var_id.set(data[0]),
            var_dep.set(data[1]),
            var_course.set(data[2]),
            var_year.set(data[3]),
            var_sem.set(data[4]),
            
            var_name.set(data[5]),
            var_en.set(data[6]),
            var_roll.set(data[7]),
            var_gender.set(data[8]),
            var_dob.set(data[9]),
            var_email.set(data[10]),
            var_phone.set(data[11]) ,
            var_radio1.set(data[12])

        def update_data():
            if var_dep.get()=="Select Department" or var_name.get()=="" or var_id.get()=="":       
                msg.showerror("Error","All Field are required",parent=self.root)
            else:
                try:
                    Update=msg.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,en=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,photo=%s where id=%s",(
                        var_dep.get(),
                        var_course.get(),
                        var_year.get(),
                        var_sem.get(),

                        var_name.get(),
                        var_en.get(),
                        var_roll.get(),
                        var_gender.get(),
                        var_dob.get(),
                        var_email.get(),
                        var_phone.get() ,
                        var_radio1.get(),
                        var_id.get(),
                        
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
                    delete=msg.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                        my_cursor=conn.cursor()
                        s=var_id.get()                       
                        query = "delete from student where id={}".format(s)                       
                        my_cursor.execute(query)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    fetch_data()
                    conn.close()
                    msg.showinfo("Delete","Successfully deleted select student details",parent=self.root)
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        def reset_data():
            var_dep.set("Select Department"),
            var_course.set("Select Course"),
            var_year.set("Select Year"),
            var_sem.set("Select Semester "),
            var_id.set(""),
            var_name.set(""),
            var_en.set(""),
            var_roll.set(""),
            var_gender.set("Select Gender"),
            var_dob.set(""),
            var_email.set(""),
            var_phone.set("") ,
            var_radio1.set("")

    #=================Generate data set or Take photo sample================

        def generate_dataset():
            if var_dep.get()=="Select Department" or var_name.get()=="" or var_id.get()=="":       
                msg.showerror("Error","All Field are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    stu_id=var_id.get()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,en=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,photo=%s where id=%s",(
                        var_dep.get(),
                        var_course.get(),
                        var_year.get(),
                        var_sem.get(),
                        var_name.get(),
                        var_en.get(),
                        var_roll.get(),
                        var_gender.get(),
                        var_dob.get(),
                        var_email.get(),
                        var_phone.get() ,
                        var_radio1.get(),
                        var_id.get()
                                    ))
                    conn.commit()
                    fetch_data()
                    reset_data()
                    conn.close()
                    harcascadePath = "haarcascade_frontalface_default.xml"
                    detector = cv2.CascadeClassifier(harcascadePath)

                    cam = cv2.VideoCapture(0)

                    sampleNum = 0
                    while (True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = detector.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                            # incrementing sample number
                            sampleNum = sampleNum + 1
                            # saving the captured face in the dataset folder TrainingImage
                            cv2.imwrite("dataset/TrainingImage/user."+str(stu_id)+"."+str(sampleNum)+".jpg",
                                        gray[y:y + h, x:x + w])
                            cv2.putText(img,f"NO OF IMAGE:{sampleNum}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,50,50),3)
                            # display the frame
                            cv2.imshow("Crooped Face",img)
                        # wait for 100 miliseconds
                        if cv2.waitKey(100) & 0xFF == ord('q'):
                            break
                        # break if the sample number is morethan 100
                        elif sampleNum > 100:
                            break
                    cam.release()
                    cv2.destroyAllWindows()
                except Exception as es:

                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        def search_data():
            conn=mysql.connector.connect(host = 'localhost',
                                              user=' root',
                                              password='12345',
                                              database='face_registration')
            my_cursor=conn.cursor()
            if var_search.get()=="Roll No":
                try:
                    s=var_data.get()
                    query = "select * from student where roll={}".format(s)
                    my_cursor.execute(query)
                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        student_table.delete(*student_table.get_children())
                        for i in data:
                            student_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            elif var_search.get()=="Enrolment No":
                try:
                    s=var_data.get()
                    query = "select * from student where en={}".format(s)
                    my_cursor.execute(query)


                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        student_table.delete(*student_table.get_children())
                        for i in data:
                            student_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            elif var_search.get()=="Semester":
                try:

                    s=var_data.get()
                    query = "select * from student where sem={}".format(s)
                    my_cursor.execute(query)


                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        student_table.delete(*student_table.get_children())
                        for i in data:
                            student_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        # top image
        image = Image.open(r"image/image23.jpg")
        image=image.resize((450,130), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        f1=Label(self.root,image=self.photo)
        f1.place(x=0,y=0,width=450,height=130)

        image1 = Image.open(r"image/image22.jpg")
        image1=image1.resize((450,130), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(image1)
        f1=Label(self.root,image=self.photo1)
        f1.place(x=450,y=0,width=450,height=130)

        image2 = Image.open(r"image/image23.jpg")
        image2=image2.resize((500,130), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(image2)
        f1=Label(self.root,image=self.photo2)
        f1.place(x=900,y=0,width=500,height=130)
        # bg image
        image3 = Image.open(r"image/image24.jpg")
        image3=image3.resize((1380,600), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=130,width=1380,height=600)
        # title
        title=Label(bg,text="STUDENT REGISTRATION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=0,width=1380,height=45)

        main_frame=Frame(bg,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1360,height=530)
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=670,height=515)
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
        dep_combo["values"]=("Select Department","CS","Chemistry","History","Physics","Commerce")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,stick=W)

        # current course

        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,stick=W)

        course_combo=ttk.Combobox(current_course,textvariable=var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BCA","MCA","BCom","MBA","B.A","B.Sc","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,stick=W)

        # year

        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,stick=W)

        year_combo=ttk.Combobox(current_course,textvariable=var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,stick=W)

        # Semester

        sem_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,stick=W)

        sem_combo=ttk.Combobox(current_course,textvariable=var_sem,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,stick=W)

        # Class student information
        class_student=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=250,width=660,height=240)

        #id
        id_label=Label(class_student,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        id=ttk.Entry(class_student,textvariable=var_id,width=20,font=("times new roman",12,"bold"))
        id.grid(row=0,column=1,padx=10,pady=5,stick=W)
        #name
        name_label=Label(class_student,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,stick=W)

        name=ttk.Entry(class_student,textvariable=var_name,width=20,font=("times new roman",12,"bold"))
        name.grid(row=0,column=3,padx=10,pady=5,stick=W)
        #enrolment no
        en_label=Label(class_student,text="Enrollment NO:",font=("times new roman",12,"bold"),bg="white")
        en_label.grid(row=1,column=0,padx=10,pady=5,stick=W)

        en=ttk.Entry(class_student,textvariable=var_en,width=20,font=("times new roman",12,"bold"))
        en.grid(row=1,column=1,padx=10,pady=5,stick=W)
        #Rollno
        roll_label=Label(class_student,text="Roll NO:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,stick=W)

        roll=ttk.Entry(class_student,textvariable=var_roll,width=20,font=("times new roman",12,"bold"))
        roll.grid(row=1,column=3,padx=10,pady=5,stick=W)
        #gender
        gender_label=Label(class_student,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,stick=W)

        gender_combo=ttk.Combobox(class_student,textvariable=var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Femal")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,stick=W)

        #Dob
        dob_label=Label(class_student,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,stick=W)

        dob=ttk.Entry(class_student,textvariable=var_dob,width=20,font=("times new roman",12,"bold"))
        dob.grid(row=2,column=3,padx=10,pady=5,stick=W)
        #email
        email_label=Label(class_student,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,stick=W)

        email=ttk.Entry(class_student,textvariable=var_email,width=20,font=("times new roman",12,"bold"))
        email.grid(row=3,column=1,padx=10,pady=5,stick=W)
        #phone no
        phone_label=Label(class_student,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,stick=W)

        phone=ttk.Entry(class_student,textvariable=var_phone,width=20,font=("times new roman",12,"bold"))
        phone.grid(row=3,column=3,padx=10,pady=5,stick=W)
        # radio button
        global var_radio1
        var_radio1=StringVar()
        button1=ttk.Radiobutton(class_student,variable=var_radio1,text="Take Photo Sample",value="Yes")
        button1.grid(row=4,column=0)


        button2=ttk.Radiobutton(class_student,variable=var_radio1,text="No Photo Sample",value="No")
        button2.grid(row=4,column=1)

        # button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=655,height=35)

        save=Button(btn_frame,text="Save",command=add_data,cursor="hand2",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save.grid(row=0,column=0)

        update=Button(btn_frame,text="Update",command=update_data,cursor="hand2",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1)

        delete=Button(btn_frame,text="Delete",command=delete_data,cursor="hand2",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=2)

        reset=Button(btn_frame,text="Reset",command=reset_data,cursor="hand2",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3)


        btn_frame1=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=190,width=655,height=28)

        take_photo=Button(btn_frame1,text="Take Photo Sample",command=generate_dataset,cursor="hand2",width=72,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo.grid(row=0,column=2)




                     ######################Right label frame##########
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=660,height=515)

        image_right= Image.open(r"image/image2.jpg")
        image_right=image_left.resize((660,130), Image.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(image_right)
        f1=Label(right_frame,image=self.photo_left)
        f1.place(x=5,y=0,width=660,height=130)

                         ################Search System#################

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)

        search_label=Label(search_frame,text="Search Bar:",font=("times new roman",15,"bold"),fg="white",bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        search_combo=ttk.Combobox(search_frame,textvariable=var_search,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No","Enrolment No","Semester")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,stick=W)

        search=ttk.Entry(search_frame,textvariable=var_data,width=15,font=("times new roman",12,"bold"))
        search.grid(row=0,column=2,padx=3,pady=5,stick=W)

        search=Button(search_frame,text="Search",command=search_data,cursor="hand2",width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search.grid(row=0,column=3,padx=3)

        showall=Button(search_frame,text="Show All",command=fetch_data,cursor="hand2",width=11,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall.grid(row=0,column=4,padx=3)

                   ###########################TABLE FRAME############

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=280)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(table_frame,column=("id","dep","course","year","sem","name","en","roll","gender","dob",
                                                       "email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        
        student_table.heading("id",text="StudentID") 
        student_table.heading("dep",text="Department")
        student_table.heading("course",text="Course")  
        student_table.heading("year",text="Year") 
        student_table.heading("sem",text="Semester") 
        
        student_table.heading("name",text="Name") 
        student_table.heading("en",text="Enrolment NO") 
        student_table.heading("roll",text="Roll")
        student_table.heading("gender",text="Gender") 
        student_table.heading("dob",text="DOB") 
        student_table.heading("email",text="Email") 
        student_table.heading("phone",text="Phone No") 
        student_table.heading("photo",text="PhotoSampleStatus") 
        student_table["show"]="headings"
        
        student_table.column("id",width=100) 
        student_table.column("dep",width=100)
        student_table.column("course",width=100)  
        student_table.column("year",width=100) 
        student_table.column("sem",width=100) 
        student_table.column("name",width=100) 
        student_table.column("en",width=100) 
        student_table.column("roll",width=100)
        student_table.column("gender",width=100) 
        student_table.column("dob",width=100) 
        student_table.column("email",width=100) 
        student_table.column("phone",width=100) 
        student_table.column("photo",width=150) 



        student_table.pack(fill=BOTH,expand=1)
        fetch_data()
        # ===================Set Cursor for update================= 
        student_table.bind("<ButtonRelease>",get_cursor)
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
