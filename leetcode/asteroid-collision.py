class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack <Integer> st = new Stack<>();

        for(int x : asteroids){

            while(!st.isEmpty() && st.peek() > 0 && x < 0 ){

                if( Math.abs(x) > st.peek() ){
                    st.pop();
                    continue; // check for another elements in stack
                }

                else if( st.peek() == Math.abs(x) ){
                    // if both of same size and have different direction just remove the stack one 
                    st.pop();
                }

                x = 0;
            }

            if(x != 0 ) st.add(x);
        }

        int[] res = new int[st.size()];

        for(int i = res.length -1 ; i >= 0 ; i--){
            res[i] = st.pop();
        }

        return res;
    }
}