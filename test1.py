print ("Hello User, What is your name?")
name = input()
print ("Welcome %s, Please enter your date of birth." % name)
month = input()
year = int(input())
age = 2016 - year
print ("Enter your city and zipcode")
city = input()
zipcode = input()
print ("Please confirm your details below:")
print ("Your name is %r"  % name)
print ("You were born %r, %r" % (month, year))
print ("You are %r years old" % age)
print ("You live in %r, %r." % (city, zipcode))





