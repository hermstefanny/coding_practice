def canConstruct(ransomNote: str, magazine: str) -> bool:

    mag_dict = {}
    note = ""

    for char in magazine:
        if char not in mag_dict:
            mag_dict[char] = 1
        else:
            mag_dict[char] += 1

    print(mag_dict)

    for char in ransomNote:
        if char in mag_dict:
            mag_dict[char] -= 1
            note += char

    print(mag_dict)
    print(note)


print(canConstruct("aa", "aab"))
print(canConstruct("aa", "ab"))
print(canConstruct("a", "b"))
