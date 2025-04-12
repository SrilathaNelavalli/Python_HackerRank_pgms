#Program for Reading Emp Details from KBD and Save them in File (Use Pickling Process)
#EmpPickEx.py
import pickle
def saveempdata():
    with open("emp.data","ab") as fp:
        while(True):
            #read emp Data from KBD
            print("---------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("---------------------------------------")
            #Create empty list for adding emp values
            lst=list()
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #save lst data to the file
            pickle.dump(lst,fp)
            print("Emp Record Saved in a File Sucessfully")
            print("---------------------------------------")
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using Program")
                break

#Main Program
saveempdata()