# Program for Copying the content of one file into another file
# FileCopyEx.py
try:
    src=input("enter the source file:")
    with open(src,"r") as sp:
        dest=input("enter the destination file:")
        with open(dest,"a") as dp:
            srcdata=sp.read()
            dp.write(srcdata)
    print("data copied successfully from 0{} to {}".format(src,dest))
except FileNotFoundError:
    print("file doesn't exist")
#main pgm


