class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;

        if(n == 2 ) return Math.min(cost[n-1] , cost[n-2]);

        for(int i = 2 ; i < n ; i++){
            int a = Math.min(cost[i-1] + cost[i] , cost[i-2] + cost[i]);
            cost[i] = a;
        }

        return Math.min(cost[n-1] , cost[n-2]);


    }
}