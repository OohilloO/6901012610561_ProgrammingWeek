a = [5, 9, 2]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
#5 9 2 (บรรทัดละค่า)

s = "Hello"
t = ""
i = 0
while i < len(s):
    t = t + str(i) + "\t" + s[i] + "\n"
    i = i + 1
print(t)
#แสดง index คู่กับตัวอักษร 0 H / 1 e / 2 l / 3 l / 4 o

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#อ่านทั้งไฟล์แล้วพิมพ์ ไฟล์ปิดเองอัตโนมัติ

a = []
with open("example.txt", "r") as file:
    for line in file:
        num = int(line)
        a.append(num)
print(a)
#ถ้าไฟล์มี 5, 2, 7 ทีละบรรทัด จะได้ [5, 2, 7]

with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")
#ต้องใส่ \n เอง ต่างจาก print()

try:
    with open("example.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("Error: example.txt is not found")
#ถ้าไม่มีไฟล์ จะแสดงข้อความ error แทนโปรแกรมพัง