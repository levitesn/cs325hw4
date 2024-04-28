def powerset(inputSet: list[int]):
    def backtrack(start: int, current: list[int]):
        # add a copy of current subset
        power_set.append(current.copy())

        # look at each element starting from start index to include in the subset
        for i in range(start, len(inputSet)):
            current.append(inputSet[i])
            backtrack(i + 1, current)
            current.pop()

    power_set = []
    backtrack(0, [])  # start with starting index of 0 and empty current
    return power_set


# test cases
print(powerset([1, 2, 3]))
print(powerset([]))
