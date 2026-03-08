import java.util.*;

class Solution {
    public long subArrayRanges(int[] nums) {

        int n = nums.length;

        int[] pse = pse(nums);
        int[] nse = nse(nums);
        int[] pge = pge(nums);
        int[] nge = nge(nums);

        long minSum = 0;
        long maxSum = 0;

        for(int i = 0; i < n; i++){

            long left = i - pse[i];
            long right = nse[i] - i;
            minSum += (long)nums[i] * left * right;

            left = i - pge[i];
            right = nge[i] - i;
            maxSum += (long)nums[i] * left * right;
        }

        return maxSum - minSum;
    }

    int[] pse(int[] arr){
        int n = arr.length;
        int[] pse = new int[n];
        Stack<Integer> st = new Stack<>();

        for(int i = 0; i < n; i++){
            while(!st.isEmpty() && arr[st.peek()] > arr[i])
                st.pop();

            pse[i] = st.isEmpty() ? -1 : st.peek();
            st.push(i);
        }

        return pse;
    }

    int[] nse(int[] arr){
        int n = arr.length;
        int[] nse = new int[n];
        Stack<Integer> st = new Stack<>();

        for(int i = n-1; i >= 0; i--){
            while(!st.isEmpty() && arr[st.peek()] >= arr[i])
                st.pop();

            nse[i] = st.isEmpty() ? n : st.peek();
            st.push(i);
        }

        return nse;
    }

    int[] pge(int[] arr){
        int n = arr.length;
        int[] pge = new int[n];
        Stack<Integer> st = new Stack<>();

        for(int i = 0; i < n; i++){
            while(!st.isEmpty() && arr[st.peek()] < arr[i])
                st.pop();

            pge[i] = st.isEmpty() ? -1 : st.peek();
            st.push(i);
        }

        return pge;
    }

    int[] nge(int[] arr){
        int n = arr.length;
        int[] nge = new int[n];
        Stack<Integer> st = new Stack<>();

        for(int i = n-1; i >= 0; i--){
            while(!st.isEmpty() && arr[st.peek()] <= arr[i])
                st.pop();

            nge[i] = st.isEmpty() ? n : st.peek();
            st.push(i);
        }

        return nge;
    }
}