n = 5
print(n)
#5

n = n - 1
print(n)
#4

n = 5
if (n > 0):
    print(n)
    n = n - 1
#5

if (n > 0):
    print(n)
    n = n - 1
#4

n = 5
while (n > 0):
    print(n)
    n = n - 1
#5
#4
#3
#2
#1

n = 5 
while (n > 0): 
    print(n)
#จะแสดงผล 5 ออกมาเรื่อยๆไม่มีวันหยุด

while (n > 0):
    print("*",end="") # do not add a newline
    n = n - 1
print() # add a newline

import random
x = random.randint(-5, 5)
print(x)
if x < 0:
    print("x is negative")
else:
    print("x is not negative")

import getpass
user_password = getpass.getpass("Enter your password: ")
if user_password == "secret123":
    print("Access granted :)")
else:
    print("Access denied!")
#ต้องใส่รหัสให้ถูกถ้าถูกจะขึ้น Access granted ถ้าผิดจะขึ้น Access denied!