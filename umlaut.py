#!/usr/bin/python
import sys

if(len(sys.argv) <= 1):
    print('No file given, please use as such: "umlaut.py {file}"')
    exit(1)
else:
    with open(sys.argv[1],'r') as file:
        filedata = file.read()
        filedata = filedata.replace('ae','ä')
        filedata = filedata.replace('oe','ö')
        filedata = filedata.replace('ue','ü')

        filedata = filedata.replace('Ae','Ä')
        filedata = filedata.replace('Oe','Ö')
        filedata = filedata.replace('Ue','Ü')
    with open(sys.argv[1],'w') as file:
        file.write(filedata)
        print('Succesfully Changed')