def removeDuplicates(self, nums: list[int]) -> int:
    left = 1
    for right in range(1, len(nums)):
        if nums[left-1] != nums[right]:
            left += 1
            nums[left-1] = nums[right]
    return left

print(removeDuplicates(None,[1,2,3,4,5]))