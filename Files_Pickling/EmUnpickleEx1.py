import pickle
def  retrivevdata():
    try:
        with open("emp.data","rb") as rp:
            print("file opened successfully")
            record=pickle.load(rp)      #file pointer is pointing to 1st record,loading it &printing
            print(record)
            record = pickle.load(rp)  #file pointer is pointing to 2nd record,loading it &printing

                                        #if 100 records are there i need to load 100 times &print 100 times na
                                        #so i am reading continuosly so using "while(true)"
            print(record)
    except EOFError:
        print("records are over")
retrivevdata()

#see EmUnpickleEx1.py for dynamisam for this pgm


        