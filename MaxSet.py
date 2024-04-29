def max_independent_set(nums: list[int]):
    nums_len = len(nums)
    if nums_len == 0:
        return []

    if nums_len == 1:
        return [nums[0]] if nums[0] > 0 else []

    # base cases
    dp = [0] * nums_len
    dp[0] = nums[0]
    if nums_len > 1:
        dp[1] = max(nums[0], nums[1])\

    # Fill dp array
    for i in range(2, nums_len):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i], nums[i])

    # Check if all calculated dp values are negative or zero
    if all(x <= 0 for x in dp):
        return []

    # Reconstruct sequence
    result = []
    i = nums_len - 1
    while i >= 0:
        if i == 0 or dp[i] == nums[i] or dp[i] == dp[i - 2] + nums[i]:
            result.append(nums[i])
            i -= 2  # skip the previous element
        else:
            i -= 1  # continue to the previous element

    return result[::-1]  # reverse the result because we started from the end
