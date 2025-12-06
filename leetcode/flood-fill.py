class Solution {
    int rows;
    int cols;


    void dfs(int[][] image, int i , int j , int currColor , int color , boolean  visited[][]){

        if(i < 0 || j < 0 || j >= cols || i >= rows || image[i][j] != currColor || visited[i][j]) return;

        visited[i][j] = true;

        image[i][j] = color;

        dfs(image , i+1 , j , currColor , color , visited);
        dfs(image , i-1 , j , currColor , color , visited);
        dfs(image , i, j-1 , currColor , color , visited);
        dfs(image , i , j+1 , currColor , color , visited);
    }


    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        rows = image.length;
        cols = image[0].length;

        boolean[][] visited = new boolean[rows][cols]; // all false

        int curr = image[sr][sc];

        dfs(image , sr , sc , curr , color , visited);

        return image;






    }
}