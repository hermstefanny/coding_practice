class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = []
        if len(s) != len(t):
            return False

        s_list = [char for char in s]

        for char in t:
            if char in s_list:
                s_list.pop(s_list.index(char))

        if not s_list:
            return True
        else:
            return False


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
print(solution.isAnagram("a", "ab"))
