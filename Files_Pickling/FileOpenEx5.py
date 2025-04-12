#is the further  deep explanation for FileOpenEx4.py i.e why open() is not best for opening the file
#if we wnat to use open() for opening the file we need to again in finally block try block for handling the exception
#which we will get if we ddint find the file then we r unable to get fp &we r unable to close the unabled file
try:
    fp=open("stud1.py","r")
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
    try:
        print("is file closed before close() with open():",fp.closed)
        fp.close()
        print("is file closed after the close() with open()",fp.closed)
    except NameError:
        print("file is not able to close")
    else:
        fp.close()

