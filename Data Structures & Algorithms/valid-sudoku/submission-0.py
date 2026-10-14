class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = defaultdict(set)
        cols_seen = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                tile = board[i][j]

                if (tile in rows_seen[i] or
                    tile in cols_seen[j] or
                    tile in box[(i // 3, j // 3)]):
                    return False

                rows_seen[i].add(tile)
                cols_seen[j].add(tile)
                box[(i // 3, j // 3)].add(tile)


        return True
        