class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if self.search(row, 0, len(row) - 1, target):
                    return True
                else:
                    return False
        
        return False

    def search(self, row:List[int], l: int, r: int, target: int) -> bool:
        if l > r:
            return False
        else:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                return self.search(row, mid + 1, r, target)
            else:
                return self.search(row, l, mid - 1, target)
        