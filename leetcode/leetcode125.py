
# def isPalindrome(self, s: str):
#     s1 = []
#     for i in range(len(s)):
#         if s[i].isalnum():
#             s1.append(s[i].lower())
#     return s1 == s1[::-1]

def isPalindrome(self, s: str):
    left, right = 0, len(s) - 1
    while left < right:
        if not(s[left].isalnum()):
            left += 1
            continue
        if not(s[right].isalnum()):
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True



print(isPalindrome(None, "aba"))
        