with open("stud4.data","r") as fp:
    print("file opened successfully in read mode")
    print("file pointer points to the index of {} ".format(fp.tell()))
    fdata=fp.read(6) #now fp is pointing to starting pointb i.e 0th index,i am trying to print(python)  6 letter of fp pointing
                        #position.
    #fdata=fp.read()
    print(fdata)
    print("file pointer points to the index of {} ".format(fp.tell()))
    #after printing 'python', fp is poing to next letter (nothing but space) which there at 6th index positon

    print("..........setting the fp position to 10th index using seek() ..............")
    fp.seek(10)
    print("file pointer points to the index of {} ".format(fp.tell()))
    fdata=fp.read(2)
    print(fdata)
    print("file pointer points to the index of {} ".format(fp.tell()))
    print(".......... ....from 12 th index onward reading entire data..........")
    fdata=fp.read()
    print(fdata)
    print("file pointer points to the index of {} ".format(fp.tell()))



