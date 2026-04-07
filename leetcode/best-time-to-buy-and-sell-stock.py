class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0];
        int sell = Integer.MIN_VALUE;
        int max = Integer.MIN_VALUE;

        for(int i  : prices ){
            int profit = i - buy;
            max= Math.max(profit,max);
            buy = Math.min(buy,i);
        }

        return max;
    }
}