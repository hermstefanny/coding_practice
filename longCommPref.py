from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    sorted_list = sorted(strs, key=len)
    pattern = sorted_list[0]

    n = len(pattern)

    short_list = []

    for word in sorted_list:
        short_list.append(word[:n])

    prefix_dict = {}
    prefix = ""

    print(short_list)

    for word in short_list:
        i = 0
        for letter in word:
            if letter == pattern[i]:
                prefix_dict[letter] = 1 + prefix_dict.get(letter, 0)

            i += 1

    print(prefix_dict)

    for key, value in prefix_dict.items():
        if value >= len(strs):
            prefix += key
        else:
            prefix += "-"

    return prefix.split("-")[0]


# print(longestCommonPrefix(["flower", "flow", "flight"]))
# print(longestCommonPrefix(["dog", "racecar", "car"]))
# print(longestCommonPrefix(["cir", "car"]))
# print(longestCommonPrefix(["reflower", "flow", "flight"]))
print(longestCommonPrefix(["aa", "aa"]))
