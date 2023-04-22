print("Enter an array of numbers seperated by spaces")
array1=list(map(int,input().split()))
print("Enter an array of numbers seperated by spaces")
array2=list(map(int,input().split()))
array3=array1+array2
array3.sort()
length_of_array3=len(array3)
if length_of_array3%2==0:
    medium=length_of_array3//2
    first_element=array3[medium]
    second_element=array3[medium-1]
    print((first_element+second_element)/2)
else:
    print(array3[length_of_array3//2-1])
