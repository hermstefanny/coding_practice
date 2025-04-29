def isSubsequence(s: str, t: str) -> bool:

    replica = ""
    ind = 0

    for char1 in s:
        pos = t.find(char1)
        print(pos)

        if ind <= pos:
            t = t.replace(char1, "", 1)
            replica += char1
            ind = pos

    if replica == s:
        return True
    else:
        return False


# print(isSubsequence("abc", "ahbgdc"))
# print(isSubsequence("axc", "ahbgdc"))
# print(isSubsequence("aac", "ahbgdc"))
# print(isSubsequence("abc", "ahbbbc"))
# print(isSubsequence("acb", "ahbgdc"))
print(isSubsequence("aza", "abzba"))
print(isSubsequence("ab", "baab"))
