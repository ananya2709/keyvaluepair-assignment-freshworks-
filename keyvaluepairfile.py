import os.path
from os import path
import json 
import time 
class kvp:
    def __init__(self):
        fileloc="c:/Python38/Scripts/"
    def __init__(self,f):
        fileoc=f
    def create(filename,filedata,ttl=0):
        if(len(filename)<=32):
            dict1={}
            completeName = os.path.join(fileloc, filename+".txt")  
            f = open(completeName, "x")
            print(type(filedata))
            if(isinstance(filedata,dict)):
                filedata = json.dumps(filedata) 
                f.write(filedata)
            else:
                filedata=str(filedata)
                f.write(filedata)
            if(os.stat(completeName).st_size>=16000):
                print("data must be within 16KB")
                os.remove(completeName)
            else:
                print("data wiithn 1kb")
            if(ttl>0):
               ts = time.time() 
               dict1.update({filename:ts+ttl})
                

        
        else:
            print("length of filename should not exceed 32")


    def read(filename,fileloc):
        completeName = os.path.join(fileloc, filename+".txt")
        if(ttl):
            if(dict1[filename]>time.time()):
                f = open(completeName, "r")
                print(f.read())
            else:
                print("read operation cannot be done because the time to live for the file has expired")
        else:
            f = open(completeName, "r")
            print(f.read())

    def delete(filename,fileloc):
        completeName = os.path.join(fileloc, filename+".txt")
        os.remove(completeName)
        if(ttl):
            if(dict1[filename]>time.time()):
                os.remove(completeName)
            else:
                print("read operation cannot be done because the time to live for the file has expired")
        else:
            os.remove(completeName)

