class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        for i in reversed(range(len(s))):
            if s[i] == '-':
                continue
            if len(result) % (k + 1) == k:
                result += '-'
            result += s[i].upper()
        return "".join(reversed(result))


# --------------------------------------------------------------
# d = "".join(s.upper().split('-'))
# n = len(d)
# f = n % k
# if f == 0:
#     return "-".join(d[i:i + k] for i in range(0, n, k))
# else:
#     return "-".join([d[:f]] + [d[i:i + k] for i in range(f, n, k)])
print(Solution().licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))
