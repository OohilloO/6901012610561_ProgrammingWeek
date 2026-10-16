def print_all(a):
    i = 0
    while i < len(a):
        print(a[i])
        i = i + 1

def add_all(a, x):
    i = 0
    while i < len(a):
        a[i] = a[i] + x
        i = i + 1

a = [5, 9, 2]
add_all(a, 3)
print_all(a)
#8 12 5 (array ถูกเปลี่ยนค่า)

def add_x(a, x):
    a = a + x
a = 5
add_x(a, 3)
print(a)
#5 (ค่า a ไม่เปลี่ยน เพราะ pass by value)

m = [[5, 7, 9], [2, 4, 6], [8, 3, 1]]
print(m[0][0])
print(m[1][0])
#5
#2

def sum_2Dn(m):
    sum = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            sum = sum + m[i][j]
            j = j + 1
        i = i + 1
    return sum
print(sum_2Dn(m))
#45

def count_2Dn(m, x):
    count = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == x:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

def addm(A, B):
    result = []
    i = 0
    while i < len(A):
        row = []
        j = 0
        while j < len(A[i]):
            row.append(A[i][j] + B[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result
print(addm([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
#[[6, 8], [10, 12]]