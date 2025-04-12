#pgm for accepting the data dynamically from KWD and write the data to the file
print("enter the data for  writing to the file ")
with open("stud4.data","w")as fp:
    while (True):
        kwb = input()
        if (kwb == "@"):
            print("data written to the file")
            break
        else:
            fp.write(kwb+"\n")



