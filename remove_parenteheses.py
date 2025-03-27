class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        left_string = ""
        right_string = ""
        for char in s:

            if char == "(":
                count += 1

            elif char == ")":
                count -= 1

            left_string += char

            if count < 0:

                left_string = left_string[:-1]
                count = 0

        count = 0
        for char in left_string[::-1]:
            if char == ")":
                count += 1
            elif char == "(":
                count -= 1
            right_string += char

            if count < 0:

                right_string = right_string[:-1]
                count = 0

        clean_string = right_string[::-1]
        return clean_string


solution = Solution()
print(solution.minRemoveToMakeValid("))(("))
