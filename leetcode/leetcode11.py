def obiom(height: list[int]) -> int:
    water_max = 0
    left = 0
    right = len(height) - 1
    while left < right:
        level = (right - left) * min(height[left], height[right])
        water_max = max(level, water_max)
        if height[left] <= height[right]:
            left += 1
            continue
        if height[right] < height[left]:
            right -= 1
    return water_max
print(obiom(list([1, 8, 6, 2, 5, 4, 8, 3, 7])))
