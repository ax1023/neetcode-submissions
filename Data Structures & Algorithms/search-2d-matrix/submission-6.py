class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        l = 0
        r = rows

        row = None

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1     
            elif matrix[mid][-1] < target:
                l = mid + 1

        if row is None:
            return False

        l = 0
        r = cols

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
                


        