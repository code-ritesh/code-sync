class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque <Integer> dq = new ArrayDeque<>();
        int n = nums.length;
        int ans[] = new int[n-k+1];
        int idx = 0;

        for(int i = 0 ; i < n ; i++){

            int x = nums[i];

            while(!dq.isEmpty() && nums[dq.peekLast()] <= x ) dq.removeLast();

            dq.addLast(i);

            // shrink the window
            if(i -k  == dq.peekFirst() ){ // i >= k 
                dq.removeFirst();
            }

            //update the ans
            if(i >= k-1){
                ans[i-k+1] = nums[dq.peekFirst()];
            }
        }

        return ans;
    }
}