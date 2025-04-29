def isSubsequence(s: str, t: str) -> bool:

    replica = ""

    i, j = 0, 0

    if not s:
        return True

    while j < len(t):
        if s[i] == t[j]:
            replica += t[j]
            i += 1
        if i >= len(s):
            break
        j += 1
    print(replica)

    if replica == s:
        return True
    else:
        return False


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("aac", "ahbgdc"))
print(isSubsequence("abc", "ahbbbc"))
print(isSubsequence("acb", "ahbgdc"))
print(isSubsequence("aza", "abzba"))
print(isSubsequence("ab", "baab"))
print(isSubsequence("", "ahbgdc"))
print(isSubsequence("b", "abc"))
