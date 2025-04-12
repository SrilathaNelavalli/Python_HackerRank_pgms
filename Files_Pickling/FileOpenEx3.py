try:
    with open("stud1.py","r") as fp:
        print("type of fp is:", type(fp))
        print("file opened in read mode successfully")
        print("*"*50)
        print("file mode is:", fp.mode)
        print("name of file is:", fp.name)
        print("is file readable: ", fp.readable())
        print("is file writable:",fp.writable())
        print("is file closed:",fp.closed)
    print("is file closed after with open() as:",fp.closed)
except FileNotFoundError:
    print("file doesn't exist")



