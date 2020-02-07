def fact(n):
    if n ==1:
        return 1
    return n * fact(n - 1)
a = input('输入要计算的阶乘')
l = float(a)
f = fact(l)
print(f)