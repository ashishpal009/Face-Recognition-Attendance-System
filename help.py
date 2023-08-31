from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)  

        img_top=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\helpdesk.png")
        img_top=img_top.resize((1530,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=700) 
        

        dev_label=Label(f_lbl,text="ashu584584@gmail.com",font=("times new roman",25,"bold"),bg="lightgrey")
        dev_label.place(x=850,y=380)

    
    
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
