a=int(input())
m=[]
for i in range(a):
  m.append(input())
r=m[0]
s,a=0,0
n=""
for i in range(len(r)):
    a=0
    for k in range(1,a):
          if r[i]==m[k][i]:
            a=a+1
    if a==a-1:
       n=n+r[i]
    else:
        break
print(n)
© 2019 GitHub, Inc.
