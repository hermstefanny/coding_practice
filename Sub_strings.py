def isSubsequence(s: str, t: str) -> bool:

    replica = ""

    for char1 in s:
        for char2 in t:
            if char2 == char1:
                replica += char2

                t = t.replace(char2, "")
                print()
                break

    print(replica)
    if replica == s:
        return True
    else:
        return False


# print(isSubsequence("abc", "ahbgdc"))
# print(isSubsequence("axc", "ahbgdc"))
# print(isSubsequence("aac", "ahbgdc"))
# print(isSubsequence("abc", "ahbbbc"))
print(isSubsequence("acb", "ahbgdc"))
