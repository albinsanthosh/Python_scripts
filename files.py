"""2.	Create a file names.txt and store 10 different user names in that file, one user name in one line.
Now write a script that accepts user name as command line argument, checks whether a similar name exists
in names.txt, if yes, it asks you to provide the Age, Salary and Phone no for that user and store all these
details in a file called userdata.txt in the current directory.
"""
import re

o=open("names.txt","r")
print(o.tell())
uname=input("Enter username:")
b=o.readlines()
c=[]
for i in b:
    c.append(i.rstrip('\n'))
if uname in c:
    age=input("Enter age:")
    sal=input("Enter sal:")
    phno=input("Enter phoneno:")
    w=open("userdata.txt","a+")
    w.write("\n")
    w.write(r"{0},{1},{2},{3}".format(uname,age,sal,phno))
    w.close()
else:
    print("Not available")
o.close()
print("Wrote to file")