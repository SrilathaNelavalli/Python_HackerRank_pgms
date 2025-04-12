import pickle
def  retrivevdata():
    try:
        with open("emp.data","rb") as rp:
            print("file opened successfully")
            record=pickle.load(rp)      #file pointer points to the first record at first time,if we run the pgm
            print(record)               #we get 1st record

           # without using while loop if iam trying to get the 2nd record  irrespective of how many times i run the pgm also
            #i get the 1st record only...i.e every time when i run pgm it is by default poins to 1st record only
         #IT IS DISCOVERD BY SRILATHA only
        #IF we want to SAY in INTERVIEW by default fp is pinting to the first record only then we need to say
        #.......by using tell(), it will give position of fp,when we are trying to read just print tell(),then it will givefp is at
        #0th position like that

    except EOFError:
        print("records are over")
retrivevdata()