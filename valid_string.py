# Valid Strings
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        correspondance = {"}": "{", ")": "(", "]": "["}

        val_list = []
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in correspondance.keys():
                print(char)
                if len(val_list) == 0:
                    return False
                if val_list[-1] == correspondance.get(char):
                    val_list.pop()
                else:
                    return False

            else:
                val_list.append(char)

        if len(val_list) == 0:
            return True
        print(len(val_list))
        return False


solution = Solution()
validation = solution.isValid("([}}])")
print(validation)
