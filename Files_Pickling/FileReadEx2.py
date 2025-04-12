#using readlines()
try:
    with open("stud.data","r") as fp:
        fdata=fp.readlines()
        print(fdata)
        for record in fdata:
            print(record,end="")
except FileNotFoundError:
    print("file doesnt exists")