#by czfnice陈泽锋
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
c = input('请输入一个变量')
d =input('请输入上面变量所要计算的次方')
b = float(d)
a = float(c)
if a > 0:
    print(power(a,b))
elif a < 0:
    print(power(a,b))
