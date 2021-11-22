"""4.	Create a class Employee having members as follows:
emp_no
emp_name
emp_basic
Constructor to initialize members
Ask user to enter details of an employee and set them in an Employee object.
Store details of this object in a file emp.txt
     	Read employee details from the file and display those details
"""


class Employee:
    def __init__(self, emp_no, emp_name, emp_basic):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_basic = emp_basic


eno = int(input("Enter employee no:"))
ename = input("Enter employee name:")
ebasic = int(input("Enter employee basic:"))
a = Employee(eno, ename, ebasic)
w = open("emp.txt", "w")
w.write("{0},{1},{2}".format(a.emp_no, a.emp_name, a.emp_basic))
w.close()
r = open("emp.txt", "r")
print(r.read())
r.close()
