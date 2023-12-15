from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,symptom,isFamily=False):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(first_name,surname)
        self.__age=age
        self.__mobile=mobile
        self.__address=postcode
        self.__doctor = 'None'
        self.__symptoms=[symptom]
        self.isFamily=isFamily

    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        for i in self.__symptoms:
            print(i)

    def set_new_symptoms(self,symptom):
        self.__symptoms=symptom

    def get_symptoms(self):
        return self.__symptoms
    
    def __str__(self):       
        return (f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__address:^10}")