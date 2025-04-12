#using read()
try:
    with open("stud.data","r") as fp:
        print("file opened in read mode successfully")
        fpdata=fp.read()
        print(fpdata)
except FileNotFoundError:
    print("file doesnt exist")