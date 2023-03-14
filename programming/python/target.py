nums=list(map(int,input().split()))
target=int(input())
for i in range(len(nums)):
	for j in range(i,len(nums)):
		if nums[i]+nums[j]==target:
			print(i,j)
			break


		