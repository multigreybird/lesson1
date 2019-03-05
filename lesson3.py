print("------------EASY------------")
print("------------Task 1------------")

def rounding(a, b):
    c = a * (10**b)
    if (c % 1) > 0.5:
        c = c + 1
    c = (int(c))/(10**b)
    return c

num = float(input("Введите число которое хотите округлить: "))
digit = int(input("Введите разряд до которого хотите округлить: "))

res = rounding(num, digit)
print(res)

print("------------Task 2------------")

def is_good(a):
    s1 = a[0] + a[1] + a[2]
    s2 = a[3] + a[4] + a[5]
    if s1 == s2:
        return True
    else:
        return False

num = (input("Введите номер билета (6 цифр): "))
num = list(map(int, num))
res = is_good(num)
print(res)

print("------------NORMAL------------")
print("------------Task 1------------")

def Fib(a, b):
    fib = list()
    fib.append(1)
    fib.append(1)
    for i in range(2, b):
        fib.append((fib[i-1] + fib[i-2]))
    return fib[a-1:]

num1 = int(input("Введите номер начального числа: "))
num2 = int(input("Введите номер конечного числа: "))

res = Fib(num1, num2)
print(res)

print("------------Task 2------------")

def new_sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]




num = list(map(int, (input("Введите массив: "))))
new_sort(num)
print(num)