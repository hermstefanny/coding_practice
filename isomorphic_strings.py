def isIsomorphic(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    char_map = {}
    for i, c in enumerate(s):
        print(i)

        if c not in char_map:
            char_map[c] = t[i]
        elif char_map[c] != t[i]:
            return False

    print(char_map)

    if len(set(char_map.keys())) == len(set(char_map.values())):
        return True
    else:
        return False


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("paper", "gbggg"))
