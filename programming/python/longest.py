s=input()
i=0
j=0
d={}
ans=0
while j<len(s):
    if s[j] not in d or i>d[s[j]]:
        ans=max(ans,(j-i+1))
        d[s[j]]=j
        print(d)
    else:
        i=d[s[j]]+1
        ans=max(ans,(j-i+1))
        j-=1 
        
        print(d)
    j+=1
print(ans)