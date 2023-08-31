from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")
                
                #=================variables=================
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()
                
        
                # first image
                img=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\attendence1.png")
                img=img.resize((800,200))
                self.photoimg=ImageTk.PhotoImage(img)
                
                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=800,height=200)
                
# second         image 
                img1=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\attendence2.png")
                img1=img1.resize((800,200))
                self.photoimg1=ImageTk.PhotoImage(img1)
                
                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=800,y=0,width=800,height=200)
        
                ###bg image####3
        
                img3=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\attendencebg.png")
                img3=img3.resize((500,500))
                self.photoimg3=ImageTk.PhotoImage(img3)
                
                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=240,width=1530,height=500)
        
                title_lbl=Label(bg_img,text="Attendence Management System",font=("times new roman",35,"bold"),bg="white",fg="black")
                title_lbl.place(x=0,y=0,width=1530,height=55)  
  #mian         frame
                main_frame=Frame(bg_img,bd=20)
                main_frame.place(x=5,y=60,width=1500,height=600) 
#left fr        ame
                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
                Left_frame.place(x=5,y=5,width=720,height=580) 
        
                img_left=Image.open(r"C:\Users\ASHISH PAL\Desktop\Face recognition system\all images\student 3.png")
                img_left=img_left.resize((740,130))
                self.photoimg_left=ImageTk.PhotoImage(img_left)
                
                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=740,height=70) 

        
                left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=10,y=100,width=680,height=280)  
        
        
####labe            l and entry #####
        
                attendenceId_label=Label(left_inside_frame,text="Attendence ID:",font=("times new roman",13,"bold"),bg="white")
                attendenceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
                attendenceId_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"),bg="white")
                attendenceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
#roll             
                rollLabel=Label(left_inside_frame,text="Roll :",font=("times new roman",13,"bold"),bg="white")
                rollLabel.grid(row=0,column=2,padx=4,pady=8)
                
                rollLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"),bg="white")
                rollLabel_entry.grid(row=0,column=3,padx=10,pady=8)
        
  #name             
                NameLabel=Label(left_inside_frame,text="Name :",font=("times new roman",13,"bold"),bg="white")
                NameLabel.grid(row=1,column=0,padx=4,pady=16)
                
                NameLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"),bg="white")
                NameLabel_entry.grid(row=1,column=1,padx=10,pady=16)
        
# Depart            ment
                departmentLabel=Label(left_inside_frame,text="Department :",font=("times new roman",13,"bold"),bg="white")
                departmentLabel.grid(row=1,column=2,padx=4,pady=8)
                
                departmentLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"),bg="white")
                departmentLabel_entry.grid(row=1,column=3,padx=10,pady=8)
#time             
                TimeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
                TimeLabel.grid(row=2,column=0,padx=4,pady=8)
                
                TimeLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"),bg="white")
                TimeLabel_entry.grid(row=2,column=1,padx=10,pady=8)
        
####date        
                dateLabel=Label(left_inside_frame,text="Date :",font=("times new roman",13,"bold"),bg="white")
                dateLabel.grid(row=2,column=2,padx=4,pady=8)
                
                dateLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"),bg="white")
                dateLabel_entry.grid(row=2,column=3,padx=10,pady=8)
        
# attednence status
                attendence_label=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",13,"bold"),bg="white")
                attendence_label.grid(row=3,column=0,padx=10,pady=10)
        
                attendence_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=20,state="read only")
                attendence_combo["values"]=("Present","Absent")
                attendence_combo.current(0)
                attendence_combo.grid(row=3,column=1,padx=2,pady=10)
        
 #button         frame
        
                btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=215,width=700,height=40)
        
                save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="white",fg="black")
                save_btn.grid(row=0,column=0)
        
                update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="white",fg="black")
                update_btn.grid(row=0,column=1)
        
                delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="white",fg="black")
                delete_btn.grid(row=0,column=2)
        
                Reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",13,"bold"),bg="white",fg="black")
                Reset_btn.grid(row=0,column=3)
        
#right f        rame
                right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence details",font=("times new roman",13,"bold"),fg="black")
                right_frame.place(x=760,y=5,width=720,height=580) 
        
                table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=5,width=700,height=380)
                
                        #===============scroll bar table=============
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
                self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
        
                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)
        
                self.AttendanceReportTable.heading("id",text="Attendance ID")
                self.AttendanceReportTable.heading("roll",text="Roll")
                self.AttendanceReportTable.heading("name",text="Name")
                self.AttendanceReportTable.heading("department",text="Department")
                self.AttendanceReportTable.heading("time",text="Time")
                self.AttendanceReportTable.heading("date",text="Date")
                self.AttendanceReportTable.heading("attendance",text="Attendance")
        
                self.AttendanceReportTable["show"]="headings"
        
                self.AttendanceReportTable.column("id",width=100)
                self.AttendanceReportTable.column("roll",width=100)
                self.AttendanceReportTable.column("name",width=100)
                self.AttendanceReportTable.column("department",width=100)
                self.AttendanceReportTable.column("time",width=100)
                self.AttendanceReportTable.column("date",width=100)
                self.AttendanceReportTable.column("attendance",width=100)
        
                self.AttendanceReportTable.pack(fill=BOTH,expand=1)
                
                self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        #================fetch data=====================
    
        def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
        # import csv    
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
                
        # export csv
        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Data","No Data found to export",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
            except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
            
        def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
            
        def update_data(self):
            try:
                if self.var_atten_id.get() == "":
                    messagebox.showerror("Error", "Attendence ID must be required.", parent=self.root)
                else:
                    with open(r"C:\Users\ASHISH PAL\Desktop\tycsproject68\College\login_form\ashish.csv", "r", newline="") as file:
                        csv_reader = csv.reader(file)
                        lines = list(csv_reader)

                    updated_row = None
                    for i, line in enumerate(lines):
                        if line[0] == self.var_atten_id.get():
                            updated_row = i
                            break

                    if updated_row is not None:
                        if len(line) == 7:  # Ensure you have 7 columns in your CSV
                            lines[updated_row] = [
                                self.var_atten_id.get(),
                                self.var_atten_roll.get(),
                                self.var_atten_name.get(),
                                self.var_atten_dep.get(),
                                self.var_atten_time.get(),
                                self.var_atten_date.get(),
                                self.var_atten_attendance.get()
                            ]
                                                        
                            with open(r"C:\Users\ASHISH PAL\Desktop\tycsproject68\College\login_form\ashish.csv", "w", newline="") as file:
                                csv_writer = csv.writer(file)
                                csv_writer.writerows(lines)
                                messagebox.showinfo("Success", "Data updated successfully.", parent=self.root)
                            self.fetchData(lines)
                            self.reset_data()
                        else:
                            messagebox.showerror("Error", "Incorrect data format in CSV.", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Attendence ID not found.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        
        


        



    
    
    
if __name__=="__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()