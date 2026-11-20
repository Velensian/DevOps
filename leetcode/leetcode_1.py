def two_sum(nums, target):
    book = {}
    for i in range(len(nums)):
        book[nums[i]] = i

    for j in range(len(nums)):
        num2 = target - nums[j]
        if num2 in book and book[num2] != j:
            return [j, book[num2]]

print(two_sum([3, 3], 6))