#Simple Length Unit Converter:
print ("LENGTH UNIT CONVERSIONS:")
x = 0.453592 #conversion factor lb to kg
y = 2.54 #conversion factor inch to cm
print ("Enter the length in Inches:")
length = int(input())
inches_to_cm  =  length * y
print ("%d inches converts to %d centimeters." % (length, inches_to_cm))

#Simple Weight Unit Converter:
print ("WEIGHT UNIT CONVERSIONS:")
print ("Enter weight in Pounds")
weight = int(input())
lb_to_kg = weight * x
print ("%d pounds coverts to %d kilograms" % (weight, lb_to_kg))