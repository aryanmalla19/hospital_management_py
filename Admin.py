from Doctor import Doctor
class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.username = username
        self.password = password
        self.address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        if(len(a_list)==0):
            print("Data is empty")
        else:
            for index, item in enumerate(a_list):
                print(f'{index+1:3}|{item}')

    def login(self,username,password) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        #Get the details of the admin


        # check if the username and password match the registered ones
        #ToDo1
        if(self.username==username and self.password==password):
            return True
        else:
            return False

    def find_index(index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        print('Enter the doctor\'s details:')
        first_name=input("Enter the first name:")
        surname=input("Enter the surname:")
        speciality=input("Enter the speciality:")
        return first_name,surname,speciality
    

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op=input("Input:")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            doctor_fname,doctor_surname,doctor_speciality=self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if doctor_fname == doctor.get_first_name() and doctor_surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists=True
                    break

            #ToDo6
            if(name_exists==False):
                doctors.append(Doctor(doctor_fname,doctor_surname,doctor_speciality))
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)
            

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                if(len(doctors)!=0):
                    try:
                        index = int(input('Enter the ID of the doctor: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index!=False:
                            break
                        else:
                            print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                    except ValueError: # the entered id could not be changed into an int
                        print('The ID entered is incorrect')
                 
                    
            
            # menu
            if(len(doctors)!=0):
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
                op = int(input('Input: ')) # make the user input lowercase

                if(op==1):
                    new_first_name=input("Enter the new first name:")
                    doctors[index].set_first_name(new_first_name)
                elif(op==2):
                    new_surname=input("Enter the new surname:")
                    doctors[index].set_surname(new_surname)
                
                elif(op==3):
                    new_speciality=input("Enter the new speciality:")
                    doctors[index].set_speciality(new_speciality)
                else:
                    print("Invalid input!!")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            if(len(doctors)!=0):
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                if(doctor_index>=0 and doctor_index < len(doctors)):
                    del doctors[doctor_index]
                else:
                    print('The id entered is incorrect')

        #if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(patients):
            print(f'{index+1:3}|{item}')
        #ToDo10

    def assign_doctor_to_patient(patients, doctors):
        assign=[]
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(patients):
            print(f'{index+1:3}|{item}')

        patient_index =input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        for index, item in enumerate(doctors):
            print(f'{index+1:3}|{item}')
        doctor_index = int(input('Please enter the doctor ID: '))

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if Admin.find_index(doctor_index,doctors)!=False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                Admin.write_patientRecords(patients)

                # link the patients to the doctor and vice versa
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----List of Patients-----")
        self.view(patients)
        if(len(patients)!=0):
            patient_index = int(input('Please enter the patient ID: '))-1
            discharge_patients.append(patients[patient_index])
            del patients[patient_index]
            print("Sucessfully discharged.\n")
            self.write_patientRecords(patients)
               
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(discharged_patients):
            print(f'{index+1:3}|{item}')
        #ToDo13

    def read_patientRecords(self):
        patient_List = []
        file_name = 'patients_file.txt'
        try:  
            with open(file_name, 'r') as fd:
                for i in fd:
                    i.split(',')
                    patient_List.append(i)
        except FileNotFoundError:
            print("File does not exist")
        finally:
            return patient_List
    
    def write_patientRecords(patients):
        file_name = 'patients_file.txt'
        file=open(file_name, 'w')
        for patient in patients:
            s=str(patient)
            file.write(f"{s}\n")
        file.close()

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter the new username: ')
            self.__username = username
            print("Sucessfully changed username")
        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if(password == input('Enter the new password again: ') and self.__password!=password):
                self.__password = password
                print("Sucessfully changed password")
            else:
                print("Sorry something went wrong")
        elif op == 3:
            address = input('Enter the new address: ')
            self.__address= address
            print("Sucessfully changed address")
        else:
            print("Invaild input !")
    
    def get_management_report(doctors,patients):
            print("-----Management Reports-----")
            print('Choose the operation:')
            print(' 1 - Total number of doctors in the system')
            print(' 2 - Total number of patients per doctor')
            print(' 3 - Total number of appointments per month per doctor')
            print(' 4 - Total number of patients based on the illness type.')
            op = input('Choose an option: ')
            try:
                if op =='1':
                    print('-------------Hospital Management System--------------')
                    print(f"The total number of doctors: {len(doctors)}")
                elif op =='2':
                    print('-------------Hospital Management System--------------')
                    for doctor in doctors:
                        totalPatients = doctor.get_total_patients()
                        print(f"{doctor.full_name()} has {totalPatients} patients")
                elif op =='3':
                    print('-------------Hospital Management System--------------')
                    for doctor in doctors:
                        total_appointments = doctor.get_total_appointments()
                        print(f"{doctor.full_name()} has {total_appointments} this month")
                elif op=='4':
                    print('-------------Hospital Management System--------------')
                    disc={}
                    for patient in patients:
                        symptoms_list = patient.get_symptoms()
                        total=0
                        for c in patients:
                            for symptom in symptoms_list:
                                if symptom in c.get_symptoms():
                                    total+=1
                            disc[symptom]=total
                    pair_list = list(disc.items())
                    for i in range(len(pair_list)+1):
                        print(f"The total number of patients with {pair_list[i][0]} is {pair_list[i][1]}")
                else:
                    print("Invalid Option")    
            except Exception as e:
                print(e)