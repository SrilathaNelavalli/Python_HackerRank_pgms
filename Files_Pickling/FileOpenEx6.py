#if we use with open() as for opening the file in read mode ,then we no need to close the file the moment
#when the pvm control goes inside of indentation block of with open() as  th file is active ,when pvm control
#comes out of the indentation block automatically the file will be closed.so no need to do finally block for connection
#closing
try:
    with open("stud.py","r") as fp:
        print("the file is opened successfully in read mode")
        print("the type of file is: ",type(fp))
        print("---------------------------------")
        print("name of the file is:", fp.name)
        print("file opened in :", fp.mode)
        print("is file readable:", fp.readable())
        print("is file writable:", fp.writable())
        print("*" * 50)
        print("i am in   with open() as indentation block")
        print("is file closed: ",fp.closed)     # # we r in the block .so file will be closed
        print("*"*50)
    print("i am out of with open() as indentation block")
    print("is file closed: ", fp.closed)    # we r out of block .so file will be closed
except FileNotFoundError:
    print("the file doesn;t exist")
