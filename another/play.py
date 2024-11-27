# 1. write a function "f1()" that receives two strings and returns true
# if the first string is a part of the second string, otherwise return false
 
def f1(str1:str , str2:str):
    if str1 in str2:
        return True
    else:
        return False
print(f1("Joox" , "BixJoox"))
# 2. write a function "f2()" that receives two floats (two sides of right angle of a right triangle)
# and returns the side opposite to the right angle
 
def f2(a,b):
    
    ans = a**2 + b**2
    squareroot = ans**0.5
    return squareroot
print(f2(3,4))


# 3. write a function "f3()" that receives a list and returns the second-largest value in the list
# note that there may be many items whose values are equal. Return None if there is none.

def f3(lst:list):
    sort = sorted(lst)
    second = sort[1]
    count = 0
    for i in range(len(lst)):
        if count > 1:
            return False
        if second == sort[i]:
            count = count + 1
            
    return second



print(f3([10,30,50,90,60]))

# 4. write a function "f4()" that receives a list (x) and a boolean function (f) and
# returns the number of items in the list that f(x[i] return True.

check = lambda x: x[0] == "a"

def f4(lst:list , f):
    count = 0
    for i in range(len(lst)):
        if check(lst[i]) == True:
            count = count + 1
    return count

print(f4(["a" , "t" , "a" , "t"] , check))
            
