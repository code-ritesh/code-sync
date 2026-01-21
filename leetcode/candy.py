class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;

        int[] l2r = new int[n];
        int[] r2l = new int[n];

        Arrays.fill(l2r,1);
        Arrays.fill(r2l,1);

        for(int i = 1 ; i < n ; i++){
            if(ratings[i-1] < ratings[i]){
                l2r[i] = Math.max(l2r[i] , l2r[i-1] + 1);
            }
        }

        for(int i = n-2 ;  i >= 0 ; i--){
            if(ratings[i] > ratings[i+1]){
                r2l[i] = Math.max(r2l[i],r2l[i+1]+1);
            }
        }

        int count = 0 ;

        for(int i = 0 ; i < n ; i++){
            count += Math.max(l2r[i],r2l[i]);
        }

        return count;
    }
}