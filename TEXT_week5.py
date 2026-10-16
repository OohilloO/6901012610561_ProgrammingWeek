n = 5
sum = 0
count = 1
while count <= n:
    sum = sum + count
    count = count + 1
print("Sum =", sum)
#Sum = 15

def sum_1_to_n(n):
    sum = 0
    count = 1
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum

def main():
    n = 5
    print("Sum from 1 to", n, "=", sum_1_to_n(n))
    n = 10
    print("Sum from 1 to", n, "=", sum_1_to_n(n))
if __name__ == "__main__":
    main()
#Sum from 1 to 5 = 15
#Sum from 1 to 10 = 55

a = [5, 9, 2]
i = 0
while i < len(a):
    print("a[", i, "] = ", a[i])
    i = i + 1
#a[0] = 5, a[1] = 9, a[2] = 2

a = [5, 9, 2]
max = a[0]
i = 0
while i < len(a):
    if max < a[i]:
        max = a[i]
    i = i + 1
#max = 9

# Parallel arrays (graphic-mode)
def setup():
    size(1000, 1000)
    i = 0
    while i < n:
        x.append(random(100, 900))
        y.append(random(100, 500))
        s.append(random(1, 5))
        i = i + 1
def draw():
    background(255)
    i = 0
    while i < n:
        draw_circle(x[i], y[i], 20)
        y[i] = y[i] + s[i]
        i = i + 1
#วงกลม n วงตกลงมาด้วยความเร็วต่างกัน