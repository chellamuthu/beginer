s=int(input())
m=[]
for i in range(s):
    m.append(input())
r=m[0]
s,a=0,0
n=""
for i in range(len(r)):
    a=0
    for k in range(1,s):
          if r[i]==m[k][i]:
            a=a+1
    if a==s-1:
       n=n+r[i]
    else:
        break
print(n)
