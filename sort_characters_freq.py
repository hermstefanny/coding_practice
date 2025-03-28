class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictionary_freq = {}

        for char in s:
            if char not in dictionary_freq.keys():
                dictionary_freq[char] = char
            else:
                dictionary_freq[char] += char

        sorted_list = sorted(dictionary_freq.values(), key=len, reverse=True)

        return "".join(sorted_list)


solution = Solution()
print(solution.frequencySort("tree"))
print(solution.frequencySort("cccaaa"))
print(solution.frequencySort("Aabb"))
