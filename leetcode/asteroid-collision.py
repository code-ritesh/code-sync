class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack <Integer> st = new Stack<>();

        for(int  x : asteroids){

            while( !st.isEmpty() && x < 0 && st.peek() > 0 ){
                if( Math.abs(x) == Math.abs(st.peek())){
                    st.pop();
                }

                else if( Math.abs(x) > Math.abs(st.peek()) ){
                    st.pop();
                    continue;
                }

                x = 0;
            }

            if(x != 0 ) st.add(x);
        }

        int[] res = new int[st.size()];

        for(int i = res.length - 1 ; i >= 0 ; i--){
            res[i] = st.pop();
        }

        return res;
    }
}