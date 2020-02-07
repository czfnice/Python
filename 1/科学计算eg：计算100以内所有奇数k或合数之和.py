p = input('输入生成最后一个数（请输入奇数或合数）：')
o = int(p)
l = 0
while o > 0:
  l = l + o
  o = o - 2
print(l)