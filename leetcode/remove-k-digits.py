class Solution {
    public String removeKdigits(String num, int k) {
        Stack <Character> st = new Stack<>();
        StringBuilder sb = new StringBuilder();

        if(k == num.length() ) return "0";

        for(char ch : num.toCharArray() ){

            while(!st.isEmpty() && st.peek() > ch && k > 0 ){
                st.pop();
                k--;
            }

            st.add(ch);
        }

        while(k > 0 ){
            st.pop();
            k--;
        }

        while(!st.isEmpty()) sb.append(st.pop());

        sb.reverse();

        while(sb.length() > 1 && sb.charAt(0) == '0'){
            sb.deleteCharAt(0);
        }

        return sb.toString();
    }
}