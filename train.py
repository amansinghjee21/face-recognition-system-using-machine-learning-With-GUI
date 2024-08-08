import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1380x730+0+0")
        self.root.title("Train")

        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path) if not f.startswith('.') and not f.startswith('_')]
            faces = []
            Ids = []

            for imagePath in imagePaths:
                try:
                    pilImage = Image.open(imagePath).convert('L')
                    imageNp = np.array(pilImage, 'uint8')
                    ID = int(os.path.split(imagePath)[-1].split(".")[1])
                    faces.append(imageNp)
                    Ids.append(ID)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1) == 13
                except Exception as e:
                    print(f"Skipping file {imagePath} due to error: {e}")

            Ids = np.array(Ids)
            return faces, Ids

        def TrainImages():
            clf = cv2.face.LBPHFaceRecognizer_create()
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            faces, ID = getImagesAndLabels(r"C:/Users/aman singh/Desktop/Automated-Attendance-System/dataset/TrainingImage")
            
            try:
                clf.train(faces, ID)
            except Exception as e:
                msg.showerror("Error", f"Training failed: {e}", parent=self.root)
                return

            clf.write("trainer/classifier.xml")
            cv2.destroyAllWindows()
            msg.showinfo("Result", "Training dataset completed!!!", parent=self.root)

        title = Label(self.root, text="Train Dataset", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title.place(x=0, y=0, width=1380, height=55)

        image_top = Image.open(r"image/image28.jpg")
        image_top = image_top.resize((1370, 300), Image.LANCZOS)
        self.photo_top = ImageTk.PhotoImage(image_top)
        f1 = Label(self.root, image=self.photo_top)
        f1.place(x=0, y=55, width=1370, height=300)

        bt_img = Button(self.root, text="TRAIN DATA", command=TrainImages, cursor="hand2", width=11, font=("times new roman", 30, "bold"), bg="red", fg="white")
        bt_img.place(x=0, y=356, width=1370, height=60)

        image_bottom = Image.open(r"image/image34.png")
        image_bottom = image_bottom.resize((1370, 300), Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(image_bottom)
        f1 = Label(self.root, image=self.photo_bottom)
        f1.place(x=0, y=415, width=1370, height=300)

if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()
