class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [{} for _ in range(0, len(board))]
        col = [{} for _ in range(0, len(board))]

        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                row[x][board[x][y]] = 1 + row[x].get(board[x][y], 0)
                col[y][board[x][y]] = 1 + col[y].get(board[x][y], 0)


        # row validation
        for r in row:
            for x in r.keys():
                if x != "." and r[x] > 1:
                    return False

        # col validation
        for c in col:
            for x in c.keys():
                if x != "." and c[x] > 1:
                    return False

        # square validation
        for square in range(0, 9):
            s = set()
            for x in range(0, 3):
                for y in range(0, 3):
                    r_f = (square // 3) * 3 + x
                    c_f = (square % 3) * 3 + y
                    if board[r_f][c_f] == ".":
                        continue
                    if board[r_f][c_f] in s:
                        return False
                    s.add(board[r_f][c_f])
        
        return True


                


        
        return True


            
                

        