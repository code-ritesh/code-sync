class Solution {

    boolean isValid(char[][] board, int row, int col, char digit) {
        int n = board.length;

        for (int i = 0; i < n; i++) {
            if (board[row][i] == digit) return false;
            if (board[i][col] == digit) return false;
        }

        int sr = (row / 3) * 3;
        int sc = (col / 3) * 3;

        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                if (board[sr + a][sc + b] == digit) return false;
            }
        }

        return true;
    }

    boolean helper(char[][] board) {
        int n = board.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                if (board[i][j] == '.') {

                    for (char d = '1'; d <= '9'; d++) {

                        if (isValid(board, i, j, d)) {
                            board[i][j] = d;

                            if (helper(board)) return true;

                            board[i][j] = '.';
                        }
                    }

                    // ❗ If no digit works, must backtrack
                    return false;
                }
            }
        }

        // ❗ No empty cells left → solved
        return true;
    }

    public void solveSudoku(char[][] board) {
        helper(board);
    }
}