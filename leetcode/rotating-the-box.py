class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        int m = boxGrid.length;
        int n = boxGrid[0].length;

        char[][] res = new char[n][m];

        // Step 1: Transpose
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                res[j][i] = boxGrid[i][j];
            }
        }

        // Step 2: Reverse each row
        for(int i = 0; i < n; i++){
            reverserow(res[i]);
        }

        // Step 3: Apply gravity
        for(int col = 0; col < m; col++){
            for(int row = n - 1; row >= 0; row--){

                if(res[row][col] == '.'){
                    int stonerow = -1;

                    for(int k = row - 1; k >= 0; k--){
                        if(res[k][col] == '*') break;
                        if(res[k][col] == '#'){
                            stonerow = k;
                            break;
                        }
                    }

                    if(stonerow != -1){
                        res[row][col] = '#';
                        res[stonerow][col] = '.';
                    }
                }
            }
        }

        return res;
    }

    void reverserow(char[] row){
        int left = 0, right = row.length - 1;

        while(left < right){
            char temp = row[left];
            row[left] = row[right];
            row[right] = temp;
            left++;
            right--;
        }
    }
}