from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    sorted_list = sorted(strs, key=len)

    n = len(sorted_list[0])

    short_list = []

    for word in sorted_list:
        short_list.append(word[:n])

    prefix_dict = {}
    prefix = ""

    for word in short_list:
        for letter in word:
            prefix_dict[letter] = 1 + prefix_dict.get(letter, 0)

    print(prefix_dict)

    for key, value in prefix_dict.items():
        if value == len(strs):
            prefix += key
        else:
            prefix += "-"

    print(prefix)

    return prefix.split("-")[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["cir", "car"]))
print(longestCommonPrefix(["reflower", "flow", "flight"]))
