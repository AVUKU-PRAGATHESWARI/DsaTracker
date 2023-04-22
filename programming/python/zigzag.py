string=input()
numofrows=int(input())
if numofrows==1:
    print(string)
row=0
direction=-1
rows=['' for i in range(numofrows)]
for i in string:
    rows[row]+=i 
    if row==0 or row==numofrows-1:
        direction=-1
    row+=direction
print(rows)