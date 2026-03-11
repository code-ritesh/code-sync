class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Stack <Integer> st = new Stack<>();

        for(int i  = 2*n-1 ; i >= 0 ; i--){

            int ele = nums[i%n];

            while(!st.isEmpty() && st.peek() <= ele ) st.pop();

            if(!st.isEmpty()) ans[i%n] = st.peek();
            else ans[i%n] = -1;

            st.add(ele);

        }

        return ans;
    }
}