def max_independent_set(nums: list[int]):
    nums_len = len(nums)
    if nums_len == 0:
        return []

    if nums_len == 1:
        return [nums[0]] if nums[0] > 0 else []

    # base cases for dp
    dp = [0] * nums_len
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1], 0)

    # Fill dp array
    for i in range(2, nums_len):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i], 0)

    # reconstruct the sequence from the last element
    result = []
    i = nums_len - 1
    while i >= 0:
        if i == 0:
            # If we're at the first element, check to include it
            if dp[i] == nums[i] and nums[i] > 0:
                result.append(nums[i])
            break
        if i == 1:
            if dp[i] == nums[i] and nums[i] > dp[i - 1]:
                result.append(nums[i])
            break
        if dp[i] == dp[i-2] + nums[i]:
            result.append(nums[i])
            i -= 2  # move to i-2 as nums[i] was included
        else:
            i -= 1  # move to i-1 to check next possibility

    return result[::-1]  # reverse to get the original order since we reconstructed backwards
