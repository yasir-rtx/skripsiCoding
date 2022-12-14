###############################################################################################################################
# Import Library
###############################################################################################################################
# keras & tensorflow
from keras.models import load_model

# File
import json
import pickle

# DIP
from PIL import Image
from PIL.Image import fromarray
import cv2

# numpy
from numpy import asarray
from numpy import expand_dims
from numpy import round
from numpy import linalg

# os
from os import listdir, mkdir
from os.path import exists
from os import system

# date & time
from datetime import datetime
import time

# GUI
from tkinter import *
from tkinter import messagebox

# Take face images and generate signature
def pose(nobp, nama, password):
    # print(f"Nobp : {nobp} | Nama : {nama} | Password : {password}")
    cap = cv2.VideoCapture(2)
    label = nobp + " - " + nama + "\\"
    labelPath = savePath + label
    print(labelPath)
    training.destroy()
    mkdir(labelPath)
    for i in range(1):
        desc = "test"
        messagebox.showinfo(f"Pose {i}", f"Deskripsi Pose {desc}")
        sum = 0
        while 1:
            key = cv2.waitKey(5) & 0xFF
            _, imgVideo = cap.read()
            FaceDetect = HaarCascade.detectMultiScale(imgVideo, 1.3, 5)
            if len(FaceDetect) > 0:
                x1, y1, w, h = FaceDetect[0]
            else :
                x1, y1, w, h = 1,1,10,10
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1+w, y1+h
            img = cv2.cvtColor(imgVideo, cv2.COLOR_BGR2RGB)
            img = fromarray(img)
            img_array = asarray(img)
            face = img_array[y1:y2, x1:x2]
            face = fromarray(face)
            face_save = face.resize((160,160))
            face = asarray(face_save)
            if key == 13:
                fileName = labelPath + nama + "_" + desc + "_" + str(sum) + ".jpg"
                print(f"saving : {fileName}")
                face_save.save(fileName)
                sum+=1
            cv2.rectangle(imgVideo, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.imshow('Rekam Wajah', imgVideo)
            if sum == 10:
                break
            if key == 27:
                break
        cv2.destroyAllWindows()
    
    messagebox.showinfo("Smart Attendance", "Data Wajah Berhasil Direkam")
    cap.release()
    
###############################################################################################################################
# Load Data and Basic Configuration
###############################################################################################################################
system("cls")
x = datetime.now()
date = str(x.day) + "/" + str(x.month) + "/" + str(x.year)

# FaceNet
MyFaceNet = load_model("D:\\College\\Semester 8\\Coding\\Models\\FaceNet\\facenet_keras.h5")

# HaarCascade
HaarCascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'))

# Raw files from faces
savePath = "D:\\College\\Semester 8\\Dataset\\Test\\"
if not exists(savePath):
    mkdir(savePath)
        
def trainingData():
    global training
    training = Toplevel()
    training.title("Training Data")
    training.iconbitmap("D:/Dev/Python/tkinter/img/ok.ico")
    w,h = 400,200
    x,y = int((screenWidth/2) - (w/2)), int((screenHeight/2) - (h/2))
    training.geometry(f"{w}x{h}+{x}+{y-50}")
    
    labelnobp = Label(training, text="NOBP: ")
    nobp = Entry(training, width=40)
    labelnama = Label(training, text="NAMA: ")
    nama = Entry(training, width=40)
    labelpassword = Label(training, text="PASSWORD: ")
    password = Entry(training, width=40)
    btnOk = Button(training, text="OK", width=10, command=lambda: pose(nobp.get(), nama.get(), password.get()))
    btnCancel = Button(training, text="CANCEL", width=10, command=training.destroy)
    
    # Grid Configuration for Training Form
    training.columnconfigure(0, weight=1)
    training.columnconfigure(1, weight=1)
    training.columnconfigure(2, weight=1)
    training.columnconfigure(3, weight=1)
    training.rowconfigure(0, weight=1)
    training.rowconfigure(1, weight=1)
    training.rowconfigure(2, weight=1)
    training.rowconfigure(3, weight=1)
    training.rowconfigure(4, weight=1)
    training.rowconfigure(5, weight=1)
    
    # render form
    labelnobp.grid(row=1, column=1, sticky='E')
    nobp.grid(row=1, column=2, columnspan=3)
    labelnama.grid(row=2, column=1, sticky='E')
    nama.grid(row=2, column=2, columnspan=3)
    labelpassword.grid(row=3, column=1, sticky='E')
    password.grid(row=3, column=2, columnspan=3)
    btnOk.grid(row=4, column=1, columnspan=2)
    btnCancel.grid(row=4, column=2, columnspan=2)        

# Main menu
window = Tk()
window.title("Smart Attendance")
window.iconbitmap("D:/Dev/Python/tkinter/img/ok.ico")

width, height = 800, 500
screenWidth, screenHeight = window.winfo_screenwidth(), window.winfo_screenheight()
x,y = int((screenWidth/2) - (width/2)), int((screenHeight/2) - (height/2))
window.geometry(f"{width}x{height}+{x}+{y-50}")
window.resizable(0,0)           # Disable resize Main Window  

# Setup for Main Grid / Grid on Main Window(window)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
# window.rowconfigure(0, weight=9)
# window.rowconfigure(1, weight=1)

# Main Frame
mainFrame = LabelFrame(window)
mainFrame.grid(row=0, column=0, sticky='WENS')

# Grid Setup for Main Frame
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=6)
mainFrame.rowconfigure(1, weight=4)

# Define title and button frame in Main frame
titleFrame = Frame(mainFrame)
buttonFrame = Frame(mainFrame)
titleFrame.grid(row=0,column=0,sticky='WENS')
buttonFrame.grid(row=1,column=0,sticky='WENS')

# Title Frame Grid Configuration
titleFrame.rowconfigure(0, weight=1)
titleFrame.rowconfigure(1, weight=1)
titleFrame.rowconfigure(2, weight=1)
titleFrame.columnconfigure(0, weight=1)
titleFrame.columnconfigure(1, weight=1)
titleFrame.columnconfigure(2, weight=1)
titleFrame.columnconfigure(3, weight=1)
titleFrame.columnconfigure(4, weight=1)

# Button Frame Grid Configuration
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)
buttonFrame.columnconfigure(4, weight=1)
buttonFrame.columnconfigure(5, weight=1)
buttonFrame.columnconfigure(6, weight=1)

# Title Frame
mainTitle = Label(titleFrame, text="APLIKASI SMART ATTENDANCE", font=('Times New Roman',30,'bold'))
mainTitle.grid(row=2, column=2)

# Button Frame
button1 = Button(buttonFrame, text="TRAINING WAJAH", padx=50, pady=25, command=trainingData)
button2 = Button(buttonFrame, text="AMBIL ABSENSI", padx=50, pady=25, state=DISABLED)
button3 = Button(buttonFrame, text="REKAP ABSENSI", padx=50, pady=25, state=DISABLED)
button1.grid(row=0, column=2)
button2.grid(row=0, column=3)
button3.grid(row=0, column=4)


# Footer / Copyright
copyright = u"\u00A9"
copyright = Label(window, text="Muhammad Yasir " + copyright + " 2022")
# copyright = Label(window, text="Muhammad Yasir " + copyright + " 2022\n Contact : yasir112358@gmail.com")
copyright.grid()

window.mainloop()