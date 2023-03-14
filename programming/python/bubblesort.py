def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
if __name__=="__main__":
    arr=[]
    n=int(input("enter the size:"))
    for i in range(n):
        arr.append(int(input()))
    bubblesort(arr)
    for i in range(n):
        print(arr[i],end=" ")