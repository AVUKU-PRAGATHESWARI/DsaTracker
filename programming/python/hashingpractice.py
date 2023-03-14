s=input("Enter the array:")
nr=int(input("Enter the number of rows:"))
r=[""]*nr
rn=0
d=1
for i in range(len(s)):
    r[rn]=r[rn]+s[i]
    if rn<nr-1 and d==1:
        rn+=1
    elif rn>0 and d==-1:
        rn-=1
    else:
        d*=-1
        rn+=d
print(" ".join(r))