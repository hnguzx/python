from sys import argv
script,filename = argv
print("we're going to erase %r " % filename)
print("If you don't want that, hit ctrl+c")
print("If you do want that ,hit enturn")
input("?")

print("Opening the file ...")
target = open(filename,'w')

print("Truncating the file. GoodBye!")
target.truncate()

line1 =input("line1:")
line2 =input("line2:")
line3 =input("line3:")

print("I'm going write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

line = "%s \n%s \n%s" % (line1,line2,line3)
target.write(line)

print("and finally ,we close it.")
target.close()

target = open(filename,'r')
print(target.read())
