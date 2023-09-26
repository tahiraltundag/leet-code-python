nums = [1,2,2,3,4,3,2,7]
def remove_duplicates(nums):
    replace = 1
    for i in range(1,len(nums)):
        if nums[i-1]!=nums[i]:
            nums[replace] = nums[i]
            replace+=1
    return replace
            
remove_duplicates(nums)  
