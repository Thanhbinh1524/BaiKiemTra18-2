def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []

    max_values = []
    n = len(nums)

    for i in range(n - k + 1):
        current_window = nums[i:i + k]
        max_value = max(current_window)
        max_values.append(max_value)

    return max_values

# Input
nums = [3, 4, 5, 1, 44, 3, 10, 12, 33, 1]
k = 3

# Output
result = sliding_window_max(nums, k)
print(result)  