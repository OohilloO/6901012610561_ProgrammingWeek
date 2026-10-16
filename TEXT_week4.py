n = 5
while (n > 0):
    print(n)
    n = n - 1
#5 4 3 2 1 (บรรทัดละค่า)

n = 5
while (n > 0):
    print(n)
#infinite loop พิมพ์ 5 ไม่หยุด เพราะไม่มี update

def print_line(n):
    while (n > 0):
        print("*", end="")
        n = n - 1
    print()
#พิมพ์ * n ตัวในบรรทัดเดียว แล้วขึ้นบรรทัดใหม่

import random
x = random.randint(-5, 5)
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
#รหัสไม่แสดงตอนพิมพ์ ถูกขึ้น Access granted ผิดขึ้น Access denied!

def cal_distance(x1, y1, x2, y2):
    diffx = abs(x1 - x2)
    diffy = abs(y1 - y2)
    result = sqrt(diffx*diffx + diffy*diffy)
    return result