import math

print("------------EASY------------")
print("------------Task 1------------")
num = int(input("Enter the number: "))
i = 10
while num != 0:
    if num == 0:
        break
    a = num % i
    print(int(a*10/i))
    num = num - a
    i = i*10

print("------------Task 2------------")
a = input("Enter a: ")
b = input("Enter b: ")
c = a
a = b
b = c
print("a =", a)
print("b =", b)

print("------------Task 3------------")
a = int(input("Enter you age: "))
if a < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")

print("------------NORMAL------------")
print("------------Task 1------------")
num = int(input("Enter the positive number: "))
big = 0
i = 10
while num != 0:
    if num == 0:
        break
    a = num % i
    b = int(a*10/i)
    print(b)
    num = num - a
    i = i*10
    if b > big:
         big = b
print("The biggest character is", big)

print("------------Task 2------------")
a = input("Enter a: ")
b = input("Enter b: ")
a, b = b, a
print("a =", a)
print("b =", b)

print("------------Task 3------------")
print("There is a format: ax² + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
dis = b**2 - 4 * a * c
if dis < 0:
    print("There is no roots")
elif dis == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print("x1 =", x1, "x2 =", x2)

print("------------HARD------------")
print("------------Task 1------------")
num = int(input("Enter the number: "))
i = 2
while i < num:
    if num == 1 or num == 0:
        print("This number is NOT simple")
        break
    if (num % i) == 0:
        print("This number is NOT simple")
        break
    if i == num - 1:
        print("This number is simple")
    i = i + 1

print("------------Task 2------------")
n = int(input("Enter Fibonacci number: "))
prev = 0
num = 1
if n == 1:
    print("1st Fibonacci number is 0")
else:
    for i in range(0, n-2):
        now = num
        num = num + prev
        prev = now
    print("It is", num)

print("------------Task 3------------")
n = int(input("Enter n: "))
m = int(input("Enter m: "))
i = 1
for i in range(n):
    for j in range(m):
        if i == 0:
            print("AAABBB", end='')
        elif ((i+1) % 2) == 0:
            print("BBBAAA", end='')
        elif ((i+1) % 2) == 1:
            print("AAABBB", end='')
    print()