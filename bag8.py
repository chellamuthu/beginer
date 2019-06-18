p=int(input())
q=list(map(int,input().split()))
r=[]
for i in q:
    if(i==l.index(i)):
        r.append(i)
print(*(sorted(r)))
if(len(r)==0):
    print(-1)
