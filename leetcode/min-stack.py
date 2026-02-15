class MinStack {

    Stack<Integer> st;
    Stack<Integer> minst;

    public MinStack() {
        st = new Stack<>();
        minst = new Stack<>();
    }

    public void push(int val) {
        if (minst.isEmpty() || val <= minst.peek())
            minst.add(val);

        st.add(val);
    }

    public void pop() {

        int a = st.peek();
        int b = minst.peek();

        if (a == b)
            minst.pop();

        st.pop();

    }

    public int top() {
        return st.peek();
    }

    public int getMin() {
        if (minst.isEmpty())
            return -1;
        return minst.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */