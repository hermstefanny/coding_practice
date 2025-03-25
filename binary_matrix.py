class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def binarySearch(left, right, row):
            mid = (left + right) // 2
            if left > right:
                return False

            if target == row[mid]:
                return True

            elif target < row[mid]:
                return binarySearch(left, mid - 1, row)
            elif target > row[mid]:
                return binarySearch(mid + 1, right, row)

        for row in matrix:
            left = 0
            right = len(row) - 1
            is_in_row = binarySearch(left, right, row)
            if is_in_row:
                return is_in_row

        return False


solution = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
result = solution.searchMatrix(matrix, target)
print(result)
