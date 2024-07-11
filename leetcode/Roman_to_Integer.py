def romanToInt(s: str) -> int:
    count = 0
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    list_num = ["V", "X", "L", "C", "D", "M", "I"]
    for x in range(len(s)):
        if x + 1 < len(s) and nums[s[x]] < nums[s[x + 1]]:
            count -= nums[s[x]]
        else:
            count += nums[s[x]]
    return count


print(romanToInt(s="LVIII"))
