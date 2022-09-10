
def get_aspected_index(two_pair_values, target_value):
    ans = -1  # initial index/if not found

    for i, val in enumerate(two_pair_values):
        if val[0]+val[1] == target_value:
            ans = i  # Last matched Index
    return ans
# -----Function-End-----


# -----Input-----
two_pair_values = [
    [1, 5],
    [9, -7],
    [0, 8],
    [6, 3],
    [4, 11],
    [14, 0],
    [8, 1],
    [4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)  # result -1 or index
