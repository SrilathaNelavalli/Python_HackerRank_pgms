#Program for Demnstrating How to write the Data to the file
#FileWriteEx3.py
x=("Pyt","C++","java")
with open("stud2.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the File")