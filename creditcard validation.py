import re
n = input("enter credit card number: ")
m = re.fullmatch("([4-6]{1})([0-9]{3}-?)([0-9]{4}-?){2}([0-9]{4})",n)
if m != None:
    print("valid credit card")
else:
    print("invalid credit card")
    
