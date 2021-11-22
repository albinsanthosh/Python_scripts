"""3.	Provide source file and destination file names as command line arguments.  Perform following functionality:
	Program should copy contents of source file to destination file
	If source file does not exist, display appropriate error message
	If destination file does not exist, it should be created.
	If destination file already exist, program should ask Want to Overwrite? (yes/no).  If user selects
	Yes then overwrite otherwise append
"""
import os

sfile = input("Enter source:")
dfile = input("Enter destination:")
try:
    o = open(sfile, "r")
except IOError:
    print("Source file not found 1")
except:
    print("Source file not found 2")
alltext = o.read()
if os.path.isfile(dfile):
    usin = input("Want to Overwrite? (yes/no)")
    if usin == "yes":
        w = open(dfile, "w")
        w.write(alltext)
        w.close()
    elif usin == "no":
        a = open(dfile, "a")
        a.write(alltext)
        a.close()
    else:
        print("wrong input")
else:
    wr = open(dfile, "w")
    wr.write(alltext)
    wr.close()