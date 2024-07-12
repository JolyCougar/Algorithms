def isValid(s: str) -> bool:
    hash_map = {")": "(", "]": "[", "}": "{"}
    stack = list()
    for x in s:
        if x in hash_map:
            if stack and stack[-1] == hash_map[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)

    if stack:
        return False

    return True


print(isValid(s="(]"))
print(isValid(s="()[]{}"))
