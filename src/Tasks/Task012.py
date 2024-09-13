"""
Class and Object Assignment

Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, printdetails,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.
"""

class Employee:
    name = None
    age = None
    phone = None
    adress = None
    eid = None

    def __init__(self,name,age,phone,adress,eid):
        print("Called, object is created")
        self.name = name
        self.age = age
        self.phone = phone
        self.adress = adress
        self.eid = eid


    def walk(self):
        print("Walking")

    def talk(self):
        print("Talking")

    def print_emp_details(self):
        print("Employee Details")
        print("Name-", self.name)
        print("age-", self.age)
        print("Phone-", self.phone)
        print("adress-", self.adress)
        print("eid-", self.eid)

E1 = Employee("Suji", 33, 987574833, "TG", 230)
E2 = Employee("Manasvi", 8, 3454645, "AP", 234)
E3 = Employee("Chandu", 38, 65768795, "AP", 345)

E1.print_emp_details()
E1.talk()

E2.print_emp_details()
E2.walk()

E3.print_emp_details()
E3.talk()