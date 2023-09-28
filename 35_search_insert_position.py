def search_insert_position(nums, val):
    replace = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[replace] = nums[i]
            replace += 1
    return replace
