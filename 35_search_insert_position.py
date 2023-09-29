nums = [1,2,4,5,7,8]
target = 7

def search_insert(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return l

search_insert(nums, target)
