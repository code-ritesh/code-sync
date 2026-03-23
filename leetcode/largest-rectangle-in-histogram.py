class Solution {
    public int largestRectangleArea(int[] heights) {

        int area = 0;

        int[] left = pse(heights);
        int[] right = nse(heights);

        for (int i = 0; i < heights.length; i++) {

            int width = right[i] - left[i] - 1;
            int currArea = heights[i] * width;

            area = Math.max(area, currArea);
        }

        return area;
    }

    // Previous Smaller Element index
    int[] pse(int[] heights) {

        Stack<Integer> st = new Stack<>();
        int[] pse = new int[heights.length];

        for (int i = 0; i < heights.length; i++) {

            while (!st.isEmpty() &&
                   heights[st.peek()] >= heights[i]) {

                st.pop();
            }

            if (st.isEmpty())
                pse[i] = -1;
            else
                pse[i] = st.peek();

            st.push(i);
        }

        return pse;
    }

    // Next Smaller Element index
    int[] nse(int[] heights) {

        Stack<Integer> st = new Stack<>();
        int n = heights.length;
        int[] nse = new int[n];

        for (int i = n - 1; i >= 0; i--) {

            while (!st.isEmpty() &&
                   heights[st.peek()] >= heights[i]) {

                st.pop();
            }

            if (st.isEmpty())
                nse[i] = n;
            else
                nse[i] = st.peek();

            st.push(i);
        }

        return nse;
    }
}