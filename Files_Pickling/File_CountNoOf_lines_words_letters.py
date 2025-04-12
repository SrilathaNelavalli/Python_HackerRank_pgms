with open("stud4.data","r") as fp:
    fdata=fp.readlines()
    print(fdata)
    print("no of lines are{} :".format(len(fdata)))
    nl=0
    nw=0
    nc=0
    for line in fdata:
        nl=nl+1
        sw=line.split()
        print(sw,type(sw))
        nw=nw+len(sw)
        nc=nc+len(line)
    print("no of lines {}:".format(nl))
    print("no of words {}:".format(nw))
    print("no of chars {}:".format(nc))





