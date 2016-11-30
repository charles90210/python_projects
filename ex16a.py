from sys import argv
#specifies the arguements to pass to argv
script, filename = argv

print ("Let's see what this file contains")

#Variable check declared and called to open and close our file
check = open(filename)
print (check.read())
print ("Now lets close the file")
print (check.close())
print ("file successfully closed")

print ("we will now edit the file contents")

print ("Do you want to continue?")
input ("Y/N?----->")

#w+ allows you to read the file and then write to it at the same time
target = open(filename, 'w+')
print ("Deleting file content.......")

print ("Enter text to write to file:")
#input text to be written to the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")

print ("Writing new content to file.......")

#This allows us to print out multiple lines at the same time with just one target.write command
target.write("%s \n %s \n %s \n %s \n" % (line1, line2, line3, line4))

print ("Now lets see if our file was edited correctly:")

#'r' allows us to open the file in read mode 
target = open(filename, 'r')
print (target.read())

print ("Close and Exit")
target.close()
