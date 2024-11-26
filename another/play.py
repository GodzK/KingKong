starthour = float(input("when to start hour : "))
startmin = float(input("when to start min : "))
stophour = float(input("when to stop : "))
stopmin = float(input("when to stop min : "))


min = (stophour - starthour)* 60 + (stopmin - startmin)


hour = (min //60 )
ansmin = (min%60)
print(hour,ansmin)
