#pgm for demonstrating how to write the data to the  file using writlines()
#d=(100,"rs",3.4j,'python')
#with open("stud1.py","a")as fp:
 #   fp.writelines(str(d)+"\n")
  #  print("data written to the file")


print("enter the data to write to the file")
with open("stud1.py","a")as fp:
    while(True):
        kwbdata = input()
        if(kwbdata=='@'):
            print("data entered successfully")
            break
        else:
            fp.writelines(str(kwbdata)+"\n")
