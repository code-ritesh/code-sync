class Solution {
    public int totalFruit(int[] fruits) {
        int k = 2;
        Map <Integer , Integer> map = new HashMap<>();
        int n = fruits.length;
        int i = 0;
        int len = 0;

        for(int j = 0 ; j < n ; j++){
            map.put(fruits[j] , map.getOrDefault(fruits[j] , 0 ) + 1);

            while(map.size() > k ){
                map.put(fruits[i] , map.getOrDefault(fruits[i] , 0 ) - 1);

                if( map.get(fruits[i]) == 0 ) map.remove(fruits[i]);
                i++;
            }

            len = Math.max(j-i+1 , len);
        }

        return len;
    }
}