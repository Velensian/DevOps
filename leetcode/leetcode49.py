def anag(self, strs: list[str]) -> list[list[str]]:
    book = {}
    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        if key in book:
            book[key].append(strs[i])
        else:
            book[key] = [strs[i]]
    return list(book.values())

print(anag(None, ["eat", "tea", "tan", "ate", "nat", "bat"]))