import re
s = input("enter EmailID: ")
m = re.fullmatch("\w[a-zA-Z0-9_.-]*@gmail[.]com",s)
if m != None:
    print("valid EmailID")
else:
    print("Invalid EmailID")

