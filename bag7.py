s=int(input())
a=[int(x) for x in input().split()]
a.sort()
for i in range(s-1,-1,-1):
  print(a[i],end='')
