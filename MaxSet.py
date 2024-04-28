def max_independent_set(nums: list[int]):
    nums_len = len(nums)
    if nums_len == 0:
        return []

    if nums_len == 1:
        return [nums[0]] if nums[0] > 0 else []

    # Base cases
    dp = [0] * nums_len
    dp[0] = max(0, nums[0])
    if nums_len > 1:
        dp[1] = max(dp[0], nums[1])

    # Fill dp array
    for i in range(2, nums_len):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    # No positive results
    if dp[-1] == 0:
        return []

    # Reconstruct the sequence
    result = []
    i = nums_len - 1
    while i >= 0:
        if i == 0 or dp[i] > dp[i - 1]:
            result.append(nums[i])
            i -= 2  # skip the previous element
        else:
            i -= 1  # move to the previous element

    return result[::-1]  # reverse the result because we started from the end


# test cases
print(max_independent_set([7, 2, 5, 8, 6]))
print(max_independent_set([1, 9, 9, 2, 1, 9]))
print(max_independent_set([-1, -1, 0]))
print(max_independent_set([-1, -1, -10, -34]))

