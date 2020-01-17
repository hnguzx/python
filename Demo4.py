'''
Created on 2020年1月11日

@author: Administrator
'''
from sys import argv
from os.path import exists

script,from_file,to_file =argv

print("Copying from %s to %s" % (from_file,to_file))
shuru=open(from_file)
indate =shuru.read()

print("the input file is %d bytes long" % len(indate))

print("Does the output file exist? %s" % exists(to_file))
print("ready,hit enturn to continue,hit ctrl-c to abort.")
input()

output=open(to_file,'w')
output.write(indate)

print("Alright, all done")
output.close()
shuru.close()