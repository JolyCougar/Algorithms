from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit2char = {'1': '', '2': 'abc', '3': 'def',
                      '4': 'ghi', '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        result = ['']

        for d in digits:
            tem = []
            for c in digit2char[d]:
                tem = tem + [r + c for r in result]

            result = tem

        return result


# ---------------------------------------------------------------------------
# mapping = {
#     '2': ['a', 'b', 'c'],
#     '3': ['d', 'e', 'f'],
#     '4': ['g', 'h', 'i'],
#     '5': ['j', 'k', 'l'],
#     '6': ['m', 'n', 'o'],
#     '7': ['p', 'q', 'r', 's'],
#     '8': ['t', 'u', 'v'],
#     '9': ['w', 'x', 'y', 'z']
# }
# rtn = []
# for digit in digits:
#     if len(rtn) == 0:
#         rtn.extend(mapping[digit])
#     else:
#         new_rtn = []
#         for item in mapping[digit]:
#             for prefix in rtn:
#                 new_rtn.append(prefix + item)
#         rtn = new_rtn
# return rtn

print(Solution().letterCombinations("23"))
