def canConstruct(ransomNote: str, magazine: str) -> bool:

    mag_dict = {}

    for char in magazine:
        if char not in mag_dict:
            mag_dict[char] = 1
        else:
            mag_dict[char] += 1

    print(f"The dictionary was{mag_dict}")

    for char in ransomNote:

        if char in mag_dict and mag_dict[char] > 0:
            mag_dict[char] -= 1

        else:
            return False
    return True


print(canConstruct("aa", "aab"))
print(canConstruct("aa", "ab"))
print(canConstruct("a", "b"))
