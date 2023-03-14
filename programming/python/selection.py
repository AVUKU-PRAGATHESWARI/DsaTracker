def selectionsort(arr,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if arr[i]<arr[min_idx]:
                min_idx=i
        arr[step],arr[min_idx]=arr[min_idx],arr[step]
size=int(input())
array=[]
for i in range(size):
    i=int(input("Enter the size of array["+str(i)+"]element"))
    array.append(i)
selectionsort(array,size)
for i in range(size):
    print(array[i],end=" ")
