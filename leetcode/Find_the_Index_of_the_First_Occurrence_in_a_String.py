class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        first_index = list()
        if haystack == needle:
            return 0
        while i + len(needle) <= len(haystack):
            if haystack[i:len(needle) + i] == needle:
                first_index.append(i)
            i += 1
        if first_index:
            return first_index[0]
        return -1


test = Solution()
print(test.strStr(haystack="hello", needle="ll"))
