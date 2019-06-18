aa=int(input())
bb=list(map(int,input().split()))
cc=[]
for a in range(aa):
    for i in range(a+1,len(bb)):
        if(bb[i]==bb[a]):
          cc.append(bb[a])
if (len(cc)==0):
    print("unique")
else:
    cc.sort()
    li2=set(cc)
    for x in li2:
        print(a,end=" ")
