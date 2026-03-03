class Solution {
    public int maxScore(int[] arr, int k) {
        int max = 0;
        int l = 0;
        int r = 0;
        int n = arr.length;

        for(int i = 0 ;  i  < k ; i++){
            l += arr[i];
        }

        max = l;

        int rightidx = n-1;

        for(int i = k-1 ; i >= 0 ; i--){
            l -= arr[i];
            r += arr[rightidx];
            rightidx--;

            max = Math.max(l+r,max);
        }

        return max;
    }
}