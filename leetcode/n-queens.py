import java.util.*;

class Solution {
    List<List<String>> res;

    boolean isSafe(char[][] board, int row, int col) {
        int n = board.length;
        int r = row, c = col;

        // upper left
        while (r >= 0 && c >= 0) {
            if (board[r][c] == 'Q') return false;
            r--;
            c--;
        }

        r = row;
        c = col;

        // upper right
        while (r >= 0 && c < n) {
            if (board[r][c] == 'Q') return false;
            r--;
            c++;
        }

        // same column (upper)
        r = row;
        c = col;
        while (r >= 0) {
            if (board[r][c] == 'Q') return false;
            r--;
        }

        return true;
    }

    void solve(char[][] board, int row) {
        int n = board.length;

        if (row == n) {
            ArrayList<String> temp = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                temp.add(new String(board[i]));
            }
            res.add(temp);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                solve(board, row + 1);
                board[row][col] = '.';
            }
        }
    }

    public List<List<String>> solveNQueens(int n) {
        res = new ArrayList<>(); // ✅ initialize class-level res
        char[][] board = new char[n][n];

        // fill board with dots
        for (int i = 0; i < n; i++) {
            for(int j = 0 ; j < n ; j++){
                board[i][j] = '.';
            }
        }

        solve(board, 0);
        return res;
    }
}