# 03 POTD 
# Problem: 79. Word Search
# Language:  python3 
# Link: https://leetcode.com/problems/word-search/submissions/1221830507

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_word(x: int, y: int, index: int) -> bool:
            if index == len(word) - 1:
                return board[x][y] == word[index]
            if board[x][y] != word[index]:
                return False
            temp = board[x][y]
            board[x][y] = "0"
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != "0":
                    if search_word(new_x, new_y, index + 1):
                        return True
            board[x][y] = temp
            return False

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                 if board[i][j] == word[0] and search_word(i, j, 0):
                    return True
        return False
