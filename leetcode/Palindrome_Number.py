def isPalindrome(x: int) -> bool:
    x = str(x)
    if x == x[::-1]:
        return True
    return False


print(isPalindrome(121))