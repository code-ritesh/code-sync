class Solution {
    public int findCenter(int[][] edges) {
        int p[] = edges[0];
        int q[] = edges[1];

        if( p[0] == q[0] || p[0] == q[1] ) return p[0];

        return p[1];
    }
}