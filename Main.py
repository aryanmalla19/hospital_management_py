# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import tkinter as tk
from tkinter import ttk
# def main():
#     """
#     the main function to be ran when the program runs
#     """
#     # Initialising the actors
    
    
#     admin.write_patientRecords(patients)
#     patients_list=admin.read_patientRecords()
#     #patients_file.write(patients)
#     # keep trying to login tell the login details are correct
#     while True:
#         if admin.login():
#             running = True # allow the program to run
#             break
#         else:
#             print('Incorrect username or password.')

#     while running:
#         # print the menu
#         print('Choose the operation:')
#         print(' 1- Register/view/update/delete doctor')
#         print(' 2- Discharge patients')
#         print(' 3- View discharged patient')
#         print(' 4- Assign doctor to a patient')
#         print(' 5- Update admin detais')
#         print(' 6- Get Management Report')
#         print(' 7- View all the patients')
#         print(' 8- Quit')

#         # get the option
#         op = input('Option: ')

#         if op == '1':
#           admin.doctor_management(doctors)
#             # 1- Register/view/update/delete doctor
#          #ToDo1
          

#         elif op == '2':
#             # 2- View or discharge patients
#             #ToDo2
            

#             while True:
#                 op = input('Do you want to discharge a patient(Y/N):').lower()

#                 if op == 'yes' or op == 'y':
#                     #ToDo3
#                     admin.discharge(patients,discharged_patients)

#                 elif op == 'no' or op == 'n':
#                     break

#                 # unexpected entry
#                 else:
#                     print('Please answer by yes or no.')
        
#         elif op == '3':
#             # 3 - view discharged patients
#             #ToDo4
#             admin.view_discharge(discharged_patients)

#         elif op == '4':
#             # 4- Assign doctor to a patient
#             admin.assign_doctor_to_patient(patients, doctors)

#         elif op == '5':
#             # 5- Update admin detais
#             admin.update_details()

#         elif op == '6':
#             # 6 - Quit
#             #ToDo5
#             admin.get_management_report(doctors,patients)
        
#         elif op == '7':
#             patients=admin.read_patientRecords()
#             print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode')
#             admin.view(patients)

#         elif op=='8':
#             quit()

#         else:
#             # the user did not enter an option that exists in the menu
#             print('Invalid option. Try again')

class GUI():
    def __init__(self):
        self.admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
        self.doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
        self.patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Headache',True), Patient('Mike','Jones', 37,'07555551234','L2 2AB','Headache'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','Common Cold',True)]
        self.discharged_patients = []
        self.admin_login_GUI()

    def admin_login_GUI(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management-Login Admin")
        self.root.geometry("400x350")
        self.root.configure(bg="#34568B")

# Heading Label
        label_heading = tk.Label(self.root, text="Admin", font=("Arial", 20, "bold"), bg="#34568B", fg="white")
        label_heading.pack(pady=15)

# Username Label and Entry
        label_username = tk.Label(self.root, text="Username:", font=("Arial", 12), bg="#34568B", fg="white")
        label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.root, font=("Arial", 12),bd=0)
        self.entry_username.pack()
        
# Password Label and Entry
        label_password = tk.Label(self.root, text="Password:", font=("Arial", 12), bg="#34568B", fg="white")
        label_password.pack(pady=6)
        self.entry_password = tk.Entry(self.root, show="*", font=("Arial", 12),bd=0)
        self.entry_password.pack()

# Login Button
        btn_login = tk.Button(self.root, text="Login", command=self.login, font=("Arial", 12),bd=0, bg="#955251", fg="white", width=10)
        btn_login.pack(pady=20)

        self.label_result = tk.Label(self.root, text="", font=("Arial", 20), fg="white")
        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.label_result.pack()
        if(self.admin.login(username,password)):
            self.label_result.config(text="Login Successful", fg="green",bg="#FFFFFF",padx=2)
            self.main_menu()
        else:
            self.label_result.config(text="Login Failed", fg="red")
    
    def main_menu(self):
        root = tk.Tk()
        root.title("Main Panel")

# Define the options
        options = [
            (" 1- Register/view/update/delete doctor", self.option1_method),
            (" 2- Discharge patients", self.option2_method),
            (" 3- View discharged patient", self.option3_method),
            (" 4- Assign doctor to a patient", self.option4_method),
            (" 5- Update admin details", self.option5_method),
            (" 6- Get Management Report", self.option6_method),
            (" 7- View all the patients", self.option7_method),
            (" 8- View all the patients from same family", self.option8_method),
            ("Quit", self.option9_method)]

# Customize front-end design
        root.configure(bg="#F0F0F0")  # Set background color
        root.geometry("500x600")


        label_font = ("Arial", 18, "bold")  # Set label font
        button_font = ("Arial", 12, "bold")  # Set button font

# Create label
        label = tk.Label(root, text="Choose an operation", font=label_font, bg="#F0F0F0")
        label.pack(pady=20)

# Create buttons for each option
        for option, method in options:
            button = tk.Button(root, text=option, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=method,width=40,bd=0)
            button.pack(pady=5)
        root.mainloop()
    
    def option1_method(self):
        self.doctor_main_panel()

    def option2_method(self):
        patients=self.admin.read_patientRecords()
        self.discharge_patients(patients)
       
    def option3_method(self):
        self.view_everything(self.discharged_patients)

    def option4_method(self):
        Admin.assign_doctor_to_patient(self.patients,self.doctors)
        self.look_terminal()

    def option5_method(self):
        self.update_admin_details()

    def option6_method(self):
        Admin.get_management_report(self.doctors,self.patients)
        self.look_terminal()
    def option7_method(self):
        file=self.admin.read_patientRecords()
        self.view_everything(file)

    def option8_method(self):
        self.group_patients(self.patients)

    def option9_method():
        quit()

    def view_everything(self,list_everything):
        window=tk.Tk()
        window.state('zoomed')
        window.title("Viewing Patients")
        table=ttk.Treeview(window,columns=("Name","Doctor","Age","Mobile","Address"),show="headings")
        table.heading("Name",text="Full Name")
        table.heading("Doctor",text="Doctor's Name")
        table.heading("Age",text="Age")
        table.heading("Mobile",text="Mobile")
        table.heading("Address",text="Address")
        table.pack()
        table.pack(fill = 'both', expand = True)
        
        for i in list_everything:
            x=i.split("|")
            Name=x[0]
            Doctor=x[1]
            Age=x[2]
            Mobile=x[3]
            Address=x[4]
            data=(Name,Doctor,Age,Mobile,Address)
            table.insert(parent="", index=0,values=data)
    
    def discharge_patients(self,list_everything):
        window = tk.Tk()
        window.state('zoomed')
        window.title("Discharge Patients")
        window.config(bg="white")
        label = tk.Label(window, text="Select patient and press delete button to discharge a patient",bg="white",bd=0)
        label.pack(pady=10)
        self.table=ttk.Treeview(window,columns=("Name","Doctor","Age","Mobile","Address"),show="headings")
        self.table.heading("Name",text="Full Name")
        self.table.heading("Doctor",text="Doctor's Name")
        self.table.heading("Age",text="Age")
        self.table.heading("Mobile",text="Mobile")
        self.table.heading("Address",text="Address")
        self.table.pack()
        self.table.pack(fill = 'both', expand = True)
        
        for i in list_everything:
            x=i.split("|")
            Name=x[0]
            Doctor=x[1]
            Age=x[2]
            Mobile=x[3]
            Address=x[4]
            data=(Name,Doctor,Age,Mobile,Address)
            self.table.insert(parent="", index=0,values=data)


        self.table.bind('<Delete>', self.delete_items)
        window.mainloop()

    def delete_items(self,_):
        for i in self.table.selection():
            discharge=self.table.item(i)['values']
        for i in self.table.selection():
                self.table.delete(i)
        self.discharged_patients.append(f"{discharge[0]}|{discharge[1]}|{discharge[2]}|{discharge[3]}|{discharge[4]}")
        index=0
        for i in self.patients:
            if(discharge[0] in str(i) and str(discharge[3]) in str(i)):
                del self.patients[index]
            index+=1
        self.admin.write_patientRecords(self.patients)

    def doctor_main_panel(self):
        root = tk.Tk()
        root.title("Doctor's Main Panel")
        root.geometry("600x400")
# Customize front-end design
        root.configure(bg="#dfe2db")  # Set background color

        label_font = ("Arial", 18, "bold")  # Set label font
        button_font = ("Arial", 12, "bold")  # Set button font

# Create label
        label = tk.Label(root, text="Choose an operation:", font=label_font, bg="#F0F0F0",bd=0)
        label.pack(pady=20)

# Create buttons with modern design and colors
        button1 = tk.Button(root,bd=0, text=" 1 - Register Doctor",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.method1)
        button1.pack(pady=10)

        button2 = tk.Button(root,bd=0, text=" 2 - View All Doctors",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.method2)
        button2.pack(pady=10)

        button3 = tk.Button(root,bd=0, text=" 3 - Update Doctor",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.method3)
        button3.pack(pady=10)

        button4 = tk.Button(root,bd=0, text=" 4 - Delete Doctor",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.method4)
        button4.pack(pady=10)

        root.mainloop()

    def method1(self):
        self.register_doc()

    def method2(self):
        window=tk.Tk()
        window.state('zoomed')
        window.title("Viewing Doctor Details")
        table=ttk.Treeview(window,columns=("Name","Spec"),show="headings")
        table.heading("Name",text="Doctor's Full Name")
        table.heading("Spec",text="Speciality")
        table.pack()
        table.pack(fill = 'both', expand = True)
        
        for i in self.doctors:
            i=str(i)
            x=i.split("|")
            Name=x[0]
            Spec=x[1]
            data=(Name,Spec)
            table.insert(parent="", index=0,values=data)

    def method3(self):
        window=tk.Tk()
        window.state('zoomed')
        window.title("Update Doctor Details")
        window.config(bg="white")
        label = tk.Label(window, text="Double click in doctor row to update",bg="white",bd=0)
        label.pack(pady=10)
        self.table_doc=ttk.Treeview(window,columns=("Name","Spec"),show="headings")
        self.table_doc.heading("Name",text="Doctor's Full Name")
        self.table_doc.heading("Spec",text="Speciality")
        self.table_doc.pack()
        self.table_doc.pack(fill = 'both', expand = True)
        
        for i in self.doctors:
            i=str(i)
            x=i.split("|")
            Name=x[0]
            Spec=x[1]
            data=(Name,Spec)
            self.table_doc.insert(parent="", index=0,values=data)
        self.table_doc.bind('<Double-1>', self.update_doc)

    def method4(self):
        window=tk.Tk()
        window.state('zoomed')
        window.title("Delete Doctor Details")
        window.config(bg="white")
        label = tk.Label(window, text="Select Doctor row and press delete button to delete Doctor:",bg="white",bd=0)
        label.pack(pady=10)
        self.table_doc=ttk.Treeview(window,columns=("Name","Spec"),show="headings")
        self.table_doc.heading("Name",text="Doctor's Full Name")
        self.table_doc.heading("Spec",text="Speciality")
        self.table_doc.pack()
        self.table_doc.pack(fill = 'both', expand = True)
        
        for i in self.doctors:
            i=str(i)
            x=i.split("|")
            Name=x[0]
            Spec=x[1]
            data=(Name,Spec)
            self.table_doc.insert(parent="", index=0,values=data)
        self.table_doc.bind('<Delete>', self.delete_doc)
        self.table_doc.mainloop()  
    
    def delete_doc(self,_):
        for i in self.table_doc.selection():
            deleted_doc=self.table_doc.item(i)['values']
            self.table_doc.delete(i)
        index=0
        for i in self.doctors:
            if(deleted_doc[0] in str(i) and str(deleted_doc[1]) in str(i)):
                del self.doctors[index]
            index+=1

    def update_doc(self,_):
        for i in self.table_doc.selection():
            self.selected_doc=self.table_doc.item(i)['values']
            self.update_doc_GUI()

    def update_doc_GUI(self):
        self.rroot = tk.Tk()
        self.rroot.title("Update Doctor Details")
        self.rroot.geometry("600x400")
# Customize front-end design
        self.rroot.configure(bg="#dfe2db")  # Set background color

        label_font = ("Arial", 18, "bold")  # Set label font
        button_font = ("Arial", 12, "bold")  # Set button font

# Create label
        label = tk.Label(self.rroot, text="Choose the field to be updated:", font=label_font, bg="#F0F0F0",bd=0)
        label.pack(pady=20)

# Create buttons with modern design and colors
        button1 = tk.Button(self.rroot,bd=0, text=" 1- First name",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_first_name)
        button1.pack(pady=10)

        button2 = tk.Button(self.rroot,bd=0, text=" 2- Surname",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_surname)
        button2.pack(pady=10)

        button3 = tk.Button(self.rroot,bd=0, text=" 3- Speciality",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_speciality)
        button3.pack(pady=10)


# Create labels
        self.first_name_label = tk.Label(self.rroot, text="First Name:")
        

        self.surname_label = tk.Label(self.rroot, text="Surname:")
        

        self.speciality_label = tk.Label(self.rroot, text="Speciality:")
        

# Create entry fields
        self.first_name_entry = tk.Entry(self.rroot)
        self.surname_entry = tk.Entry(self.rroot)
        self.speciality_entry = tk.Entry(self.rroot)
        

# Create submit button
        self.submit_button = tk.Button(self.rroot, text="Submit", command=self.submit_form)
        self.rroot.mainloop()

    def submit_form(self):
        name=self.first_name_entry.get()
        surname=self.surname_entry.get()
        speciality=self.speciality_entry.get()
        index=0
        for i in self.doctors:
            if(self.selected_doc[0] in str(i) and str(self.selected_doc[1]) in str(i)):
                ii=index
            index+=1
        if(name!=""):
           self.doctors[ii].set_first_name(name)
        elif(surname!=""):
           self.doctors[ii].set_surname(surname)
        elif(speciality!=""):
           self.doctors[ii].set_speciality(speciality)
        self.method2()
        self.rroot.destroy()

    def update_first_name(self):
        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.submit_button.pack(pady=10)

    def update_surname(self):
        self.surname_label.pack()
        self.surname_entry.pack()
        self.submit_button.pack(pady=10)

    def update_speciality(self):
        self.speciality_label.pack()
        self.speciality_entry.pack()
        self.submit_button.pack(pady=10)

    def register_doc(self):
        root = tk.Tk()
        root.title("Register Doctor")
        root.configure(bg="#F0F0F0")

        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)

# Create labels
        first_name_label = tk.Label(root, text="First Name:", font=label_font, bg="#F0F0F0")
        first_name_label.grid(row=0, column=0, padx=10, pady=10)

        surname_label = tk.Label(root, text="Surname:", font=label_font, bg="#F0F0F0")
        surname_label.grid(row=1, column=0, padx=10, pady=10)

        specialty_label = tk.Label(root, text="Specialty:", font=label_font, bg="#F0F0F0")
        specialty_label.grid(row=2, column=0, padx=10, pady=10)

# Create entry fields
        self.first_name_entry_register = tk.Entry(root, font=entry_font)
        self.first_name_entry_register.grid(row=0, column=1, padx=10, pady=10)

        self.surname_entry_register = tk.Entry(root, font=entry_font)
        self.surname_entry_register.grid(row=1, column=1, padx=10, pady=10)

        self.specialty_entry_register = tk.Entry(root, font=entry_font)
        self.specialty_entry_register.grid(row=2, column=1, padx=10, pady=10)

# Create submit button
        submit_button = tk.Button(root, text="Submit", font=label_font, bg="#4CAF50", fg="white", command=self.register_doctor_details)
        submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def register_doctor_details(self):
        first_name = self.first_name_entry_register.get()
        surname = self.surname_entry_register.get()
        specialty = self.specialty_entry_register.get()
    
        self.doctors.append(Doctor(first_name,surname,specialty))
        self.method2()

    def update_admin_details(self):
        root = tk.Tk()
        root.title("Update Admin detailss")
        root.geometry("600x400")
# Customize front-end design
        root.configure(bg="#dfe2db")  # Set background color

        label_font = ("Arial", 18, "bold")  # Set label font
        button_font = ("Arial", 12, "bold")  # Set button font

# Create label
        label = tk.Label(root, text="Choose an operation:", font=label_font, bg="#F0F0F0",bd=0)
        label.pack(pady=20)

# Create buttons with modern design and colors
        button1 = tk.Button(root,bd=0, text="Admin name",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_admin_name)
        button1.pack(pady=10)

        button2 = tk.Button(root,bd=0, text="Admin password",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_admin_password)
        button2.pack(pady=10)

        button3 = tk.Button(root,bd=0, text="Admin address",width=25, font=button_font, bg="#355C7D", fg="white", padx=10, pady=5, command=self.update_admin_address)
        button3.pack(pady=10)

        root.mainloop()

    def update_admin_name(self):
        root = tk.Tk()
        root.title("Name Form of Doctor")
        root.geometry("300x200")
        root.configure(bg="#F0F0F0")

# Create label
        label_font = ("Arial", 14, "bold")
        label = tk.Label(root, text="Enter New Admin Name", font=label_font, bg="#F0F0F0")
        label.pack(pady=20)

# Create entry field
        entry_font = ("Arial", 12)
        self.name_entry_adminn = tk.Entry(root, font=entry_font)
        self.name_entry_adminn.pack(pady=10)

# Create submit button
        submit_button = tk.Button(root, text="Submit", font=entry_font, bg="#4CAF50", fg="white", command=self.submit_admin_name)
        submit_button.pack(pady=10)
        root.mainloop()

    def update_admin_password(self):
        root = tk.Tk()
        root.title("Password Form of Doctor")
        root.geometry("300x200")
        root.configure(bg="#F0F0F0")

# Create label
        label_font = ("Arial", 14, "bold")
        label = tk.Label(root, text="Enter New Admin Password", font=label_font, bg="#F0F0F0")
        label.pack(pady=20)

# Create entry field
        entry_font = ("Arial", 12)
        self.password_entry_adminn = tk.Entry(root, font=entry_font)
        self.password_entry_adminn.pack(pady=10)

# Create submit button
        submit_button = tk.Button(root, text="Submit", font=entry_font, bg="#4CAF50", fg="white", command=self.submit_admin_password)
        submit_button.pack(pady=10)
        root.mainloop()
        
    def update_admin_address(self):
        root = tk.Tk()
        root.title("Address Form of Doctor")
        root.geometry("300x200")
        root.configure(bg="#F0F0F0")

# Create label
        label_font = ("Arial", 14, "bold")
        label = tk.Label(root, text="Enter New Admin Address", font=label_font, bg="#F0F0F0")
        label.pack(pady=20)

# Create entry field
        entry_font = ("Arial", 12)
        self.admin_entry_adminn = tk.Entry(root, font=entry_font)
        self.admin_entry_adminn.pack(pady=10)

# Create submit button
        submit_button = tk.Button(root, text="Submit", font=entry_font, bg="#4CAF50", fg="white", command=self.submit_admin_address)
        submit_button.pack(pady=10)
        root.mainloop()

    def look_terminal(self):
        root = tk.Tk()
        root.title("Please look terminal")
        root.configure(bg="#F0F0F0")
        root.geometry("600x400")

        first_name_label = tk.Label(root, text="Please look terimal for further information", bg="#F0F0F0")
        first_name_label.grid(row=0, column=0, padx=10, pady=10)
        root.mainloop()

    def submit_admin_name(self):
        name=self.name_entry_adminn.get()
        self.main_menu()
    
    def submit_admin_password(self):
        password=self.password_entry_adminn.get()
        self.main_menu()

    def submit_admin_address(self):
        address=self.admin_entry_adminn
        self.main_menu()
        
    def group_patients(self,patients):
        sameFamily=[]
        for patient in patients:
            if(patient.get_surname()=="Smith"):
                sameFamily.append(str(patient))
        self.view_everything(sameFamily)


g=GUI()