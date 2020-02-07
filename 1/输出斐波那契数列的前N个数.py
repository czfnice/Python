def a(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,b+a
        n = n + 1
    return '完成'
l = input('请输入输出斐波那契数列的前N个数')
k = float(l)
o = a(k)
print(o)