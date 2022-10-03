class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "O1"
            directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for x, y in directions:
                dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    dfs(i, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "O1":
                    board[i][j] = "O"
        