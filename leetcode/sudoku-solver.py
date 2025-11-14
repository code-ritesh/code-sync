class Solution {

    
    boolean isValid(char[][] board, int row, int col, char c) {

        for (int i = 0; i < 9; i++) {

            // Row check
            if (board[row][i] == c) return false;

            // Column check
            if (board[i][col] == c) return false;

            // 3x3 box check
            int boxRow = (row / 3) * 3 + i / 3;
            int boxCol = (col / 3) * 3 + i % 3;

            if (board[boxRow][boxCol] == c) return false;
        }

        return true;
    }


    // Backtracking solver
    boolean solve(char[][] board) {

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {

                if (board[i][j] == '.') {

                    for (char c = '1'; c <= '9'; c++) {

                        if (isValid(board, i, j, c)) {
                            board[i][j] = c;

                            if (solve(board)) return true;  

                            board[i][j] = '.';  
                        }
                    }

                    return false; 
                }
            }
        }

        return true; // there is no empty cell
    }


    public void solveSudoku(char[][] board) {
        solve(board);
    }
}