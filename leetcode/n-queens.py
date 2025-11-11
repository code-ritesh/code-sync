class Solution {
    List<List<String>> result = new ArrayList<>();

    // Check if placing a queen at (row, col) is safe
    boolean isSafe(boolean[][] board, int row, int col) {
        int n = board.length;
        int i = row, j = col;

        // check upward column
        while (i >= 0) {
            if (board[i][j]) return false;
            i--;
        }

        // check upper-left diagonal
        i = row; j = col;
        while (i >= 0 && j >= 0) {
            if (board[i][j]) return false;
            i--;
            j--;
        }

        // check upper-right diagonal
        i = row; j = col;
        while (i >= 0 && j < n) {
            if (board[i][j]) return false;
            i--;
            j++;
        }

        return true;
    }

    void solve(boolean[][] board, int row) {
        int n = board.length;

        // all queens placed successfully
        if (row == n) {
            addBoard(board);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = true;  // place queen
                solve(board, row + 1);
                board[row][col] = false; // backtrack
            }
        }
    }

    // convert true/false board → String board
    void addBoard(boolean[][] board) {
        int n = board.length;
        List<String> temp = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(board[i][j] ? 'Q' : '.');
            }
            temp.add(sb.toString());
        }

        result.add(temp);
    }

    public List<List<String>> solveNQueens(int n) {
        boolean[][] board = new boolean[n][n];
        solve(board, 0);
        return result;
    }
}