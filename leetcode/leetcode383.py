def note (self, ransomNote: str, magazine: str):
    book_notes = {}
    book_magazines = {}
    for i in range (len(magazine)):
        if magazine[i] in book_magazines:
            book_magazines[magazine[i]] += 1
        else:
            book_magazines[magazine[i]] = 1
    for j in range (len(ransomNote)):
        if ransomNote[j] in book_notes:
            book_notes[ransomNote[j]] += 1
        else:
            book_notes[ransomNote[j]] = 1
    for letter in book_notes:
        if letter in book_magazines:
            if book_notes[letter] > book_magazines[letter]:
                return False
        else: return False
    return True




print(note(None, "aa", "aab"))