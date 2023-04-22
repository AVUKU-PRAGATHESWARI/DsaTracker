print("Enter an array of seperated by spaces")
array=list(map(int,input().split()))
newarray=[]
print("Enter an element to remove fro the given array")
remove_element=int(input())
"""
for i in array:
    if i not in newarray:
        newarray.append(i)
    else:
        continue
print(newarray)"""
for i in array:
    if i==remove_element:
        continue
    else:
        newarray.append(i)
print(newarray)