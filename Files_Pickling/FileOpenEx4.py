#CASE1:if the file is opend correctly then there is no error so no Except block is executed.else block will be executed
#dothe operations.
#try(opened file sucessfully).....>else block will be executed todo operations
# CASE2if the file is notopend correctly then there is error so Except block is executed.Noelse block will be executed
# no  operations.
#try(opened file sucessfully).....> else block will be executed todo operations
#IN any of the cases finally(default) block will be executed compulsory
#in CASE1...in finall block there is no error why bcz file opened ,so fp pointing to it.its good
##in CASE2...in finall block there is an error why bcz file notopened ,so no fp value we will get error in finally block
#why bcoz... we r trying to access a fp which is not pointing to any file..so NameError
#conclusion:thats why if we opened file using open() in "r" is not good.so use with open() as is good file


try:
    fp=open("stud1.py","r")     # if we want to use open() in this situation "r", the file stud1.py is there so
                                 #no problem. if not if file is not there then
                                # in L.H.S side i.e open("stud1.py","r") it self raising exception and going to except
                                #block .and after that it will go to finally block we will get NameError why bcoz file
                                #itself is not there then there is no fp. so error will come.
                                #THATS WHY WITH OPEN() AS BEST TO OPEN A FILE
                                #IF WE R USING OPEN() make sure the file is there
    print("file opened in read mode successfully:")
    print("type of fp:",type(fp))
except FileNotFoundError:
    print("file doesn;t found")
else:
    print("name of the file is:",fp.name)
    print("file opened in :",fp.mode)
    print("is file readable:",fp.readable())
    print("is file writable:",fp.writable())
    print("....................................")
finally:
    print("i am from finally block")
    print("is file closed before close() with open():",fp.closed)
    #fp.close()
    print("is file closed after the close() with open()",fp.closed)


