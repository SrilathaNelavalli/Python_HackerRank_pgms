#pgm for demonstrating how to write the data to the  file
sno=10
name="devishi"
marks=99
#print(sno,sname,marks)
#write or save the data in the form of file
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(name+"\t")
    fp.write(str(marks)+"\n")
    print("data successfully written to the file")