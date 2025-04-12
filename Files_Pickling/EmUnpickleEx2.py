import pickle
def  retrivevdata():
    try:
        with open("emp.data","rb") as rp:
            print("file opened successfully")
            while(True):
                record=pickle.load(rp)      #file pointer is pointing to 1st record,loading it
                #print(record)
                for val in record:          #now here we have 1st record at 1st time[10,ss,80]
                    print("\t{}".format(val),end="\t")  #startin with some tabe space print 10 &end="\t" after printing 10
                                                        #immediately end with tab space and print 2nd vale ss&print with tab
                                                        #    space print 80

                print()                     #after printing 1st record it will come out of for loop the we are bringing curser to
                                            #new line to print 2nd record in new line
    except EOFError:
        print("records are over")
retrivevdata()