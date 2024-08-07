"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 """

"""Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9"""

class Solution:
    def backtrack(self, row: int) -> None:
        if row == self.n:
            solution = ["".join(board_row) for board_row in self.board]
            self.res.append(solution)
            return

        for col in range(self.n):
            pos_idx = row + col
            neg_idx = row - col
            if (
                # col is occupied
                col in self.occupied_cols
                or
                # +diag is occupied
                pos_idx in self.occupied_pos_diag
                or
                # -diag is occupied
                neg_idx in self.occupied_neg_diag
            ):
                # skip this col
                continue

            # mark as occupied
            self.occupied_cols.add(col)
            self.occupied_pos_diag.add(pos_idx)
            self.occupied_neg_diag.add(neg_idx)

            # check if next sol. fits
            self.board[row][col] = "Q"
            self.backtrack(row + 1)
            self.board[row][col] = "."

            # unmark occupied
            self.occupied_cols.remove(col)
            self.occupied_pos_diag.remove(pos_idx)
            self.occupied_neg_diag.remove(neg_idx)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        # col
        self.occupied_cols = set()
        # row + col
        self.occupied_pos_diag = set()
        # row - col
        self.occupied_neg_diag = set()

        self.res = []
        self.board = [["."] * n for _ in range(n)]
        self.backtrack(0)

        return self.res
