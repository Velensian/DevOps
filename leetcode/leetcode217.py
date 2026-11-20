def containsDuplicate(self, nums: list[int]) -> bool:
    s = set()
    for i in range(len(nums)):
        if nums[i] in s:
            return True
        else:
            s.add(nums[i])
    return False


print(containsDuplicate(None, [1, 2, 3, 4]))  # True