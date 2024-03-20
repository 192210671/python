'''22. Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''


nums=[5,7,7,8,8,10]
target=8
start=-1
end=-1

for i  in range(len(nums)):
    if nums[i]==target:
        if start==-1:
            start=i
        end=i    
result=[start,end]
print(result)       