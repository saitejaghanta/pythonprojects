import math

lineAB = float(input("enter length AB: "))
lineBC = float(input("enter length BC: "))

lineAC = math.hypot(lineAB, lineBC)

lineBM = lineAC / 2
lineBE = lineBC / 2

angleMBC = math.degrees(math.acos(lineBE / lineBM))
print ("The angle is %r°" % (int(round(angleMBC))))
