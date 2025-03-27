class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        clean_string = ""
        clean_array = []
        string_array = []

        for char in s:

            if char == "(":
                count += 1
                string_array.append(char)

            elif char == ")":
                count -= 1
                string_array.append(char)

            if count == 0:
                # print("breaking point")
                new_string = "".join([str(s) for s in string_array[1:-1]])
                clean_array.append(new_string)
                # print(clean_array)

                string_array = []

        clean_string = "".join([str(s) for s in clean_array])

        return clean_string


solution = Solution()
removed_string = solution.removeOuterParentheses("()()")
print(removed_string)
