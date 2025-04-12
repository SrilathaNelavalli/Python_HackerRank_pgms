try:
    fp=open("stud5.data","w")      #here we r giving relative path(stud.py). so it will check in current working
                                #folder(11amfiles)
    print(fp)
except FileNotFoundError:
    print("file doesn't exist ")