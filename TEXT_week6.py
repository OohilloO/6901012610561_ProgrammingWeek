a = [5, 9, 2]
sum = 0
i = 0
while i < len(a):
    sum = sum + a[i]
    i = i + 1
print(sum / len(a))
#5.333... (ค่าเฉลี่ย)

s = "Hello"
i = 0
while i < len(s):
    print(ord(s[i]))
    i = i + 1
#72 101 108 108 111

print(ord('a'))   #97
print(ord('A'))   #65
print(ord('0'))   #48
print(ord(0))     #Error: TypeError (ต้องเป็น string ยาว 1)
print(chr(97))    #a

s = "Hello"
t = ""
i = 0
while i < len(s):
    t = t + str(i) + "\t" + s[i] + "\n"
    i = i + 1
print(t)
#0 H / 1 e / 2 l / 3 l / 4 o

s = "Hello"
s[0] = "J"
#Error: TypeError: 'str' object does not support item assignment

s = "J" + s[4] + s[1]
#สร้าง string ใหม่ "Joe"

print(s.upper())      #HELLO
print("A".isalpha())  #True
print("3".isalpha())  #False
print("3".isdigit())  #True
print("3".isalnum())  #True