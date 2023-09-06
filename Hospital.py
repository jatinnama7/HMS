from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import pymysql

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Mamnagement System")
        self.root.geometry("1540x800+0+0")
        self.root.config(bg="#F5D7DB")


        self.NameofTablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.storage=StringVar()
        self.nhsnumber=StringVar()
        self.pname=StringVar()
        self.dob=StringVar()
        self.address=StringVar()
        self.sideeffect=StringVar()
        self.hospname=StringVar()
        self.mustavoid=StringVar()
        self.Dname=StringVar()



        lbtitle = Label(self.root,bd= 20,relief = RIDGE,text="+ HOSPITAL MANAGEMENT SYSYTEM +",fg="red",bg ='white',font= ("Helvetica",50,'bold')) 
        lbtitle.pack(side=TOP,fill =X)

# --------------------------Data Frame-------------------------------
        Dataframe = Frame(self.root,bd=20,relief=RIDGE,bg="#F5D7DB")
        Dataframe.place(x=0,y=130,width=1530,height=400)
        

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Helvetica",12,'bold'),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Helvetica",12,'bold'),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

# ------------------------ Button frame -------------------------------------

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

# ------------------------- Details Frame ------------------------------------

        Detailframe = Frame(self.root,bd=20,relief=RIDGE,bg="#F5D7DB")
        Detailframe.place(x=0,y=600,width=1530,height=190)

# ------------------------- Data FrameLeft -----------------------------------

        lblNameTablet=Label (DataframeLeft, font=("helvetica", 12, "bold"), text="Name Of Tablets", padx=2, pady=6) 
        lblNameTablet.grid(row=0, column=0, sticky=W)
        
        comNameTablet=ttk.Combobox (DataframeLeft,textvariable= self.NameofTablets,state="readonly",font=("helvetica", 12, "bold"), width=33)
        comNameTablet['value']=("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)
        
        lblref=Label(DataframeLeft, font=("helvetica", 12, "bold"), text="Reference No: ",padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        
        txtref=Entry (DataframeLeft, font=("helvetica", 13, "bold"),width=35,textvariable= self.ref)
        txtref.grid(row=1, column=1)
        
        lblDose=Label(DataframeLeft, font=("helvetica", 12, "bold"), text="Dose: ", padx=2, pady=4)
        lblDose.grid(row=2, column=0,sticky=W) 
        txtDose=Entry (DataframeLeft, font=("helvetica", 13, "bold"),width=35,textvariable= self.Dose)
        txtDose.grid(row=2, column=1)
        
        lblNoOftablets=Label(DataframeLeft, font=("helvetica", 12, "bold"),text="No Of Tablets:",padx=2,pady=6) 
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35, textvariable= self.NoofTablets)
        txtNoOftablets.grid(row=3, column=1)
        
        lblLot=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Lot: ", padx=2, pady=6) 
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35, textvariable= self.lot)
        txtLot.grid(row=4, column=1)

        lblIssueDate=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Issue Date: ", padx=2, pady=6) 
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35, textvariable= self.issuedate)
        txtIssueDate.grid(row=5, column=1)

        lblExpiryDate=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Expiry Date: ", padx=2, pady=6) 
        lblExpiryDate.grid(row=6, column=0, sticky=W)
        txlExpiryDate=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.expdate)
        txlExpiryDate.grid(row=6, column=1)

        lblDaillydose=Label(DataframeLeft, font=("helvetica",12,"bold") ,text="Daily Dose: ", padx=2, pady=6) 
        lblDaillydose.grid(row=7, column=0, sticky=W)
        txlDaillydose=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.dailydose)
        txlDaillydose.grid(row=7, column=1)


        lblSideEffect=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Side Effect: ", padx=2, pady=6) 
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.sideeffect)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInformation=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Must Avoid: ", padx=2, pady=6) 
        lblFurtherInformation.grid(row=0, column=2, sticky=W)
        txtFurtherInformation=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.mustavoid)
        txtFurtherInformation.grid(row=0, column=3)
        

        lblBloodPressure=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Blood Pressure: ", padx=2, pady=6) 
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Hospital Name: ", padx=2, pady=6) 
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.hospname)
        txtStorage.grid(row=2, column=3)

        lblMedicine=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Medication: ", padx=2, pady=6) 
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35)
        txtMedicine.grid(row=3, column=3,sticky= W)

        lblpatientId=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Doctor Name: ", padx=2, pady=6) 
        lblpatientId.grid(row=4, column=2, sticky=W)
        txtpatientId=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.Dname)
        txtpatientId.grid(row=4, column=3)

        lblpatietname=Label(DataframeLeft, font=("helvetica",12,"bold"), text="Patient Name: ", padx=2, pady=6) 
        lblpatietname.grid(row=5, column=2, sticky=W)
        txtpatietname=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.pname)
        txtpatietname.grid(row=5, column=3)

        lblDOB=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Date of Birth: ", padx=2, pady=6) 
        lblDOB.grid(row=6, column=2, sticky=W)
        txtDOB=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35, textvariable= self.dob)
        txtDOB.grid(row=6, column=3)

        lblpataddress=Label(DataframeLeft, font=("helvetica",12,"bold"),text="Patient Address: ", padx=2, pady=6) 
        lblpataddress.grid(row=7, column=2, sticky=W)
        txtpataddress=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.address)
        txtpataddress.grid(row=7, column=3)

        lblNHS=Label(DataframeLeft, font=("helvetica",12,"bold"),text="NHS Number: ", padx=2, pady=6) 
        lblNHS.grid(row=8, column=2, sticky=W)
        txtNHS=Entry (DataframeLeft, font=("helvetica", 13, "bold"), width=35,textvariable= self.nhsnumber)
        txtNHS.grid(row=8, column=3)
        # ---------------------------------------------------------------------
        self.txtPrescription=Text (DataframeRight, font=("arial",12,"bold"),width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

# --------------------------------- Button ---------------------------------------

        btnPrescription=Button(Buttonframe, text="Presciption", bg="green", fg="white", font=("arial",12,"bold"),width=23, padx=2,pady=6,command=self.iPrectioption)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData=Button(Buttonframe, text="Add Data", bg="green", fg="white", font=("arial",12,"bold"),width=23, padx=2,pady=6,command=self.add_funn)
        btnPrescriptionData.grid(row=0, column=1)


        btnUpdate=Button (Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),width=23, padx=2,pady=6,command=self.update_funn)
        btnUpdate.grid(row=0, column=2)

        btnDelete=Button (Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),width=23, padx=2,pady=6,command =self.delete_funn)
        btnDelete.grid(row=0, column=3)

        btnClear=Button (Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),width=23, padx=2,pady= 6,command=self.clear_fun)
        btnClear.grid(row=0, column=4)

        btnExit=Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=6,command=self.exit) 
        btnExit.grid(row=0, column=5)
        

# ---------------------------------- Table ------------------------------------
# ---------------------------------- Scrollbar -------------------------------- 

        scroll_x=ttk.Scrollbar(Detailframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailframe, column=("nameoftable", "ref", "dose", "nooftablets", "lot","issuedate","expdate", "dailydose", "storage", "nhsnumber","pname", "dob", "address"), 
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)     
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x= ttk.Scrollbar (command=self.hospital_table.xview) 
        scroll_y= ttk.Scrollbar (command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name OF Tablets")
        self.hospital_table.heading("ref",text="Reference no.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="Number OF Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp. Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Hospital")
        self.hospital_table.heading("nhsnumber",text="NHS number")
        self.hospital_table.heading("pname",text="Person Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data() 
# -------------------------------- MySQL ---------------------------
    def fetch_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="hms1")
        curr=conn.cursor()
        curr.execute("SELECT*FROM data")
        rows=curr.fetchall()
        if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                     self.hospital_table.insert("",END,values=row)
                conn.commit()
        conn.close()

    def add_funn(self):
        if self.NameofTablets.get()==""or self.ref.get() == "" or self.Dose.get() == "" or  self.NoofTablets.get() == "" or self.lot.get() == "" or self.issuedate.get() == "" or self.expdate.get() == "" or self.dailydose.get() == ""  or self.storage.get() == ""or self.nhsnumber.get() == ""or self.pname.get() == ""or self.dob.get() == "" or self.address.get() == "":
         messagebox.showerror("Error!!", "Please fill all the details")
        else:
         conn = pymysql.connect(host="localhost", user="root", password="", database="hms1")
         curr = conn.cursor()
         curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.NameofTablets.get(), self.ref.get(), self.Dose.get(),  self.NoofTablets.get(), self.lot.get(), self.issuedate.get(), self.expdate.get(), self.dailydose.get() , self.storage.get(), self.nhsnumber.get(), self.pname.get(), self.dob.get(), self.address.get()))
         conn.commit()
         self.fetch_data()    
         conn.close()
         messagebox.showinfo("Success!","The record was added successfully.")

    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row = content['values']
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NoofTablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storage.set(row[8])
        self.nhsnumber.set(row[9])
        self.pname.set(row[10])
        self.dob.set(row[11])
        self.address.set(row[12])

    def clear_fun(self):
        self.NameofTablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NoofTablets.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.storage.set("")
        self.nhsnumber.set("")
        self.pname.set("")
        self.dob.set("")
        self.address.set("")
        self.iPrectioption("")

    def update_funn(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="hms1")
        curr = conn.cursor()
        curr.execute("UPDATE data set Nameoft=%s, Dose =%s, Nooftablets=%s, Lot= %s, Issuedate=%s, Expdate=%s,Dailydose=%s,Storage=%s,nhsnumber=%s,patientname=%s,DOB=%s, Address=%s WHERE referenceno =%s",
                     (self.NameofTablets.get(), self.Dose.get(),  self.NoofTablets.get(), self.lot.get(), self.issuedate.get(), self.expdate.get(), self.dailydose.get() , self.storage.get(), self.nhsnumber.get(), self.pname.get(), self.dob.get(), self.address.get(),self.ref.get()))
        conn.commit()
        conn.close()
        self.fetch_data()
        

    def delete_funn(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="hms1")
        curr = conn.cursor()
        query = "DELETE FROM data WHERE referenceno =%s"
        curr.execute(query, (self.ref.get(),))
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear_fun()
        messagebox.showinfo("Delete","Patient has been deleted successfully!")

    def iPrectioption(self):
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self. pname.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth: \t\t\t" + self.dob.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address: \t\t\t" + self.address.get() + "\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Hospital Name:\t\t\t" + self.hospname.get() + "\n")
        self.txtPrescription.insert(END," Doctor Name: \t\t\t" + self. Dname.get() + "\n") 
        self.txtPrescription.insert(END, "NHS Number: \t\t\t" + self.nhsnumber.get() + "\n")
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" + self.NameofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets: \t\t\t" + self.NoofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t" + self.lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.expdate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t" + self.dailydose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect: \t\t\t" + self.sideeffect.get() + "\n")
        self.txtPrescription.insert(END, "Must Avoid: \t\t\t" + self. mustavoid.get() + "\n")

        self.clear_fun()

    def exit(self):
        exit=messagebox.askyesno("Hospital Management System","Confirm,you want to Exit")
        if exit>0:
            root.destroy()
            return


root = Tk()
ob = Hospital(root)
root.mainloop()

