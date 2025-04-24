from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    if len(strs) <= 1:
        return strs[0]

    pattern = []
    for letter in strs[0]:
        pattern.append(letter)

    prefix_dict = {}
    prefix = ""

    for word in strs[1:]:
        i = 0
        for letter in word:
            if i >= len(pattern):
                break
            if letter == pattern[i]:
                prefix_dict[letter] = 1 + prefix_dict.get(letter, 0)

            i += 1

    for key, value in prefix_dict.items():
        if value == len(strs) - 1:
            prefix += key

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
