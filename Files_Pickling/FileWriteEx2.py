#pgm for demonstrating how to write the data to the  file
#for FileWriteEx1.py we are adding some dynamism(accepting values from KWD)
sno=int(input("enter the sno :"))  #all are global variables
name=input("enter the sname :")
marks=float(input("enter the marks :"))
print(sno,name,marks)
#write or save the data in the form of file
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(name+"\t")
    fp.write(str(marks)+"\n")  #bringing the cursor to the new line...to add next record
    print("data successfully written to the file")