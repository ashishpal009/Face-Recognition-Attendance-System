from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
     

        img=Image.open(r"C:\Users\ASHISH PAL\Desktop\login\image\loginbg.png")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open(r"C:\Users\ASHISH PAL\Desktop\login\image\img1.png")
        img1=img1.resize((100,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        ##############label user name #################3333
        usernamee=lbl=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        usernamee.place(x=40,y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=215)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
###### login button ############

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)

##################register button ###########33
        registerbtn=Button(frame,text=" New User Register",borderwidth=0,command=self.register_window,font=("times new roman",10,"bold"),fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)
        
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,borderwidth=0,font=("times new roman",10,"bold"),fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=16,y=380,width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Eroor","all field required")
        elif self.txtuser.get()=="ashu" and self.txtpass.get()=="068":
             messagebox.showinfo("Success","Welcome to Face Recognition Attendence System ")  
        else:
            conn=mysql.connector.connect(host="localhost",port="3305",user="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query = "SELECT * FROM register WHERE email = %s AND password = %s"
            my_cursor.execute(query, (self.txtuser.get(), self.txtpass.get()))
                     
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
            if open_main>0:
                new_window = Toplevel(self.root)  # Create a new Toplevel instance
                app = Face_Recognition_System(new_window)
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()

        ################## reset passowrd #################
    def reset_pass(self):
        if self.combo_security_Q.get() == "select":
            messagebox.showerror("Error", "Select the security Question")
        elif self.security_A_entry.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            conn = mysql.connector.connect(host="localhost", port="3305", user="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.security_A_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct Answer")
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
    
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with the new password")

##################################forot passsowrd #################3

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password ")
        else:
            conn=mysql.connector.connect(host="localhost",port="3305",user="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter The Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_Q.place(x=50,y=80)
          
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
          
                 
                security_A=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_A.place(x=50,y=150)
          
                self.security_A_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_A_entry.place(x=50,y=180,width=250)



                new_password_A=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_password_A.place(x=50,y=220)
                                     
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=150)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="black",bg="white")
                btn.place(x=50,y=280,width=150)



class Register:
    def __init__(self,root):
      self.root=root
      self.root.title("Register")
      self.root.geometry("1200x700+0+0")
      
      ######################### variables ############3333
      self.var_fname=StringVar()
      self.var_lname=StringVar()
      self.var_contact=StringVar()
      self.var_email=StringVar()
      self.var_securityQ=StringVar(value="Select")
      self.var_securityA=StringVar()
      self.var_pass=StringVar()
      self.var_confpass=StringVar()



      ###################background image #################
      img=Image.open(r"C:\Users\ASHISH PAL\Desktop\login\image\registerbg.png")
      img=img.resize((1550,800))
      self.photoimg=ImageTk.PhotoImage(img)
        
      bg_lbl=Label(self.root,image=self.photoimg)
      bg_lbl.place(x=0,y=0,width=1550,height=800)
 #####################333frame#############

      frame=Frame(self.root,bg="white")
      frame.place(x=730,y=180,width=800,height=550)

      register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="black",bg="white")
      register_lbl.place(x=20,y=20)
   
    ####lables#################### and entry ##########33

      fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
      fname.place(x=50,y=100)

      fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
      fname_entry.place(x=50,y=130,width=250)

      lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
      lname.place(x=370,y=100)

      lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
      lname_entry.place(x=370,y=130,width=250)

      contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
      contact.place(x=50,y=170)

      fname_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
      fname_entry.place(x=50,y=200,width=250)

      email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
      email.place(x=370,y=170)

      email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
      email_entry.place(x=370,y=200,width=250)

      security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
      security_Q.place(x=50,y=240)

      self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
      self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name")
      self.combo_security_Q.place(x=50,y=270,width=250)
      self.combo_security_Q.current(0)

       
      security_A=Label(frame,text="Security answer",font=("times new roman",15,"bold"),fg="black",bg="white")
      security_A.place(x=370,y=240)

      security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
      security_A_entry.place(x=370,y=270,width=250)
    
      pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
      pswd.place(x=50,y=310)

      pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
      pswd_entry.place(x=50,y=340,width=250)

      confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
      confirm_pswd.place(x=370,y=310)

      confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
      confirm_pswd_entry.place(x=370,y=340,width=250)
      

    
      #########################check button #################
      self.var_check=IntVar()
      self.Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="white")
      self.Checkbtn.place(x=50,y=400)




#####################buttons###################
      img=Image.open(r"C:\Users\ASHISH PAL\Desktop\login\image\registernow.png")
      img=img.resize((280,50))
      self.photoimage=ImageTk.PhotoImage(img)

      b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
      b1.place(x=10,y=450,width=280)

      img1=Image.open(r"C:\Users\ASHISH PAL\Desktop\login\image\loginnow.png")
      img1=img1.resize((280,50))
      self.photoimage1=ImageTk.PhotoImage(img1)

      b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2")
      b1.place(x=330,y=450,width=280)


      ###############3333function declaration################3
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() =="Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please Agree to all terms and conditions")
        else:
            messagebox.showinfo("Success", "Welcome")
            

            conn=mysql.connector.connect(host="localhost",port="3305",user="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully")
    

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
    main()






