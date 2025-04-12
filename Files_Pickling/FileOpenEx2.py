# in FileOpenEx1.py we r trying to open stud.py and it is not there in current folder so it is giving error.
# i am creating stud.py in FileOpenEx2.py .

fp=open("stud.py","w")
print("file opened in write mode")
print("type of fp=",type(fp))   #type of fp=        <class '_io.TextIOWrapper'>
                                #like a=10
                                #print(type(a))  o/p:<class 'int'>

                                #i.e fp is an objectb of which type?
                                #ans: _io.TextIOWrapper(fp belongs to this class(_io.TextIOWrapper) )
