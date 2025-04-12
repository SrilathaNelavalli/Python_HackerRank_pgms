with open("stud3.py", "x") as fp:
    print("type of fp is:", type(fp))
    print("file opened in read mode successfully")
    print("*" * 50)
    print("file mode is:", fp.mode)
    print("name of file is:", fp.name)
    print("is file readable: ", fp.readable())
    print("is file writable:", fp.writable())
    print("is file closed:", fp.closed)
print("is file closed after with open() as:", fp.closed)

#FileExistsError: [Errno 17] File exists: 'stud1.py'






