class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        clean_string = ""
        individual_string = ""

        for char in s:

            if char == "(":
                count += 1
                individual_string += char

            elif char == ")":
                count -= 1
                individual_string += char

            if count == 0:
                clean_string += individual_string[1:-1]
                individual_string = ""

        return clean_string


solution = Solution()
removed_string = solution.removeOuterParentheses("(()())(())")
print(removed_string)
