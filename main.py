from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # first image
        img=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\one.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\two.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\three.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # bg image
        img3=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\bg.png")
        img3=img3.resize((1510,648),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1510,height=648)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",26,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1510,height=40)
        
        # ==================time====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl, font = ('times new roman',20, 'bold'),background = 'white',foreground = 'black')
        lbl.place(x=8,y=0,width=160,height=40)
        time()
            

        # student button
        img4=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\first.png")
        img4=img4.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=20,y=100,width=100,height=80)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=20,y=180,width=100,height=20)

        
        # Detect face button
        img5=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\second.png")
        img5=img5.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=200,y=100,width=100,height=80)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=180,width=100,height=20)

        # Attendance face button
        img6=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\fourth.png")
        img6=img6.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=200,y=400,width=100,height=80)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=470,width=100,height=20)

        # Help face button
        img7=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\sixth.png")
        img7=img7.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=20,y=400,width=100,height=80)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=20,y=470,width=100,height=20)

        # Train face button
        img8=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\fifth.png")
        img8=img8.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=250,width=100,height=80)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=310,width=100,height=20)

        # Photos face button
        img9=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\third.png")
        img9=img9.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=20,y=250,width=100,height=80)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=20,y=310,width=100,height=20)

        # Developer face button
        img10=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\developer.png")
        img10=img10.resize((100,80),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=1400,y=30,width=100,height=100)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1400,y=125,width=100,height=20)

        # Exit face button
        img11=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\eight.png")
        img11=img11.resize((50,40),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1400,y=550,width=80,height=60)




    def open_img(self):
        os.startfile(r"C:\Users\ASHISH PAL\Desktop\tycsproject68\ashish\project68\data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ========================Function Buttons===========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
     






























if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


