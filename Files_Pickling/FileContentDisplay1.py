##Program for Displaying the content of any file
#FileContentDisplayEx1.py
try:
    filename = input("enter the file name to display the content")
    with open(filename,"r") as fp:   #IMP::::NO need to put filename(variablename) in""(double quotes) when we are accepting file
                                #name from KWD & holding in a variable(filename).and that variable name we are mentionin
                                    #in with open() as,
                                #if we are mentioning filename dirctly in with open() as,then we need to mention
                                #the file name in ""
                                #ex:with open("stud1.data","r")
        filedata=fp.read()
        print(filedata)
except FileNotFoundError:
    print("file doesn't exists")

