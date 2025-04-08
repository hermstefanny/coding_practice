def canConstruct(ransomNote: str, magazine: str) -> bool:

    mag_dict = {}
    note = ""

    for char in magazine:
        if char not in mag_dict:
            mag_dict[char] = 1
        else:
            mag_dict[char] += 1

    print(f"The dictionary was{mag_dict}")

    for char in ransomNote:

        if char in mag_dict and mag_dict[char] > 0:
            mag_dict[char] -= 1
            note += char

    print(f"And now it is{mag_dict}")
    print(note)

    if note == ransomNote:
        return True
    else:
        return False


print(canConstruct("aa", "aab"))
print(canConstruct("aa", "ab"))
print(canConstruct("a", "b"))
