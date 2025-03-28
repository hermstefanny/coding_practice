class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ordered_string = []
        patron = list(order)
        s_list = list(s)
        i = 0

        while len(ordered_string) < len(s_list):

            current_letter = patron[i]
            for char in s_list:
                if char == current_letter:
                    ordered_string.append(char)

            i += 1

            if i >= len(order):
                leftover = [x for x in s_list if x not in patron]
                ordered_string += leftover
                return "".join(ordered_string)

        return "".join(ordered_string)


solution = Solution()
# print(solution.customSortString("cba", "abcd"))
print(
    solution.customSortString(
        "hucw",
        "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh",
    )
)
