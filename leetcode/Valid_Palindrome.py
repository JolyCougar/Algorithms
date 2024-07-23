class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_text = str()
        for x in s:
            if x.isalpha():
                clear_text += x.lower()
            elif x.isnumeric():
                clear_text += x.lower()
        return clear_text[::-1] == clear_text


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
