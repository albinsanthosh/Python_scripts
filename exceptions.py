"""2.	Create a class Customer having following members:
cust_no
cust_name
cust_phone
Constructor to initialize all instance variables
Method – display_customer()  printing customer details

Ask user to enter customer details.
Check if cust_phone is a 10 digit number.
If yes then create the Customer object and call the display_customer() method.
If not then raise user defined exception called InvalidPhoneException."""


class Customer:
    def __init__(self, cust_no, cust_name, cust_phone):
        self.cust_no = cust_no
        self.cust_name = cust_name
        self.cust_phone = cust_phone

    def display_customer(self):
        print(self.cust_no, self.cust_name, self.cust_phone)

class InvalidPhoneException(Exception):
    def helloz(self):
        print("InvalidPhoneException handled")

uno=int(input("Enter no:"))
uname=input("Enter name:")
uphone=int(input("Enter phone:"))
try:
    if 999999999<uphone<10000000000:
        a=Customer(uno,uname,uphone)
        a.display_customer()
    else:
        raise InvalidPhoneException
except InvalidPhoneException as z:
    z.helloz()
