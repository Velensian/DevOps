
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    book = {}
    book2 = {}
    for i in range(len(s)):
        if s[i] in book:
            book[s[i]] += 1
        else:
            book[s[i]] = 1
        if t[i] in book2:
            book2[t[i]] += 1
        else:
            book2[t[i]] = 1
    return book == book2

print(isAnagram(None, "segs", 'abc'))
