print("Enter an array of numbers seperated by space")
array=list(map(int,input().split(" ")))
print("Enter the target number")
target=int(input())
length_of_given_array=len(array)
for i in range(length_of_given_array):
    for j in range(i,length_of_given_array):
        if array[i]+array[j]==target:
            print("["+str(i)+','+str(j)+"]")
            break