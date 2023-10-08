import os
a=open("data.txt","r")
data= a.read()
numofchars=len(data)
numofwords=len(data.split())
numoflines=len(data.splitlines())
print(numofchars,numofwords,numoflines)