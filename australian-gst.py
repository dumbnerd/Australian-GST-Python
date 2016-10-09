#!/usr/bin/python3.5
#=Btronz Australian GST Python Script

y = float(input("Total amount including GST is :$ "))
r = y / 11
e = r * 10
print("Including GST ${:0.2f}".format(y))
print("Excluding GST ${:0.2f}".format(e))
print("GST Amount ${:0.2f}".format(r))
