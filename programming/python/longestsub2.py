string=input()
d={}
i=0
j=0
ans=0
while(j<len(string)):
    if string[j] not in d or i>d[string[j]]:
        d[string[j]]=j
        ans=max(ans,j-i+1)
    else:
        i=d[string[j]]+1
        ans=max(ans,j-i+1)
        j-=1 
    j+=1
print(ans)