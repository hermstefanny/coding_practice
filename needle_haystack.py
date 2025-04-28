def strStr(haystack: str, needle: str) -> int:

    index = []
    m = len(haystack)
    n = len(needle)

    if m < n:
        return -1

    for i in range(m):
        if haystack[i] == needle[0] and i + n - 1 < m:
            ind, new_i = i, i
            for j in range(n):
                if haystack[new_i] == needle[j]:
                    new_i += 1
                else:
                    break

            if new_i - ind == n:
                print("completed")
                index.append(ind)

    if not index:
        return -1
    else:
        return index[0]


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("hello", "ll"))
print(strStr("mississippi", "issip"))
