class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        math_symbols = ["*", "+", "-"]

        possible_expressions = []
        position = 0
        possible_expression = expression

        while position < (len(expression) // 2):

            math_expression = ""
            count = 0

            for char in possible_expression:

                if char not in math_symbols:
                    if count == 0:
                        math_expression += "(" + char
                        count += 1

                    elif count == 1:
                        math_expression += char + ")"
                        count += -1
                        # return math_expression

                else:
                    math_expression += char
                    # count += 1

            possible_expressions.append(math_expression)
            position = +2
            possible_expressions = possible_expressions[2:]

        return math_expression


solution = Solution()
calculation = solution.diffWaysToCompute("2*3-4*5")
print(calculation)
