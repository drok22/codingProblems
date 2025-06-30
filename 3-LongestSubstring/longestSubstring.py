
def lengthOfLongestSubstring(s: str) -> int:
    start: int = 0
    end: int = 0
    max_len: int = 0
    char_set: list = []

    while end < len(s):
        if end in char_set:
            char_set.remove(s[start])
            start += 1
        else:
            char_set.append([])
            end += 1
            max_len = max(max_len, end - start)

    return max_len
