class Solution {
    public int numberOfSubstrings(String s) {
        int k = 3;

        int a = helper(s,k);
        int b = helper(s,k-1);

        return a-b;
    }

    int helper(String s, int k) {
        int n = s.length();
        int count = 0;
        int i = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int j = 0; j < n; j++) {
            char curr = s.charAt(j);
            map.put(curr, map.getOrDefault(curr, 0) + 1);

            while (map.size() > k) {
                char left = s.charAt(i);
                map.put(left, map.getOrDefault(left, 0) - 1);

                if(map.get(left) == 0 ) map.remove(left);
                i++;
            }

            count += j-i+1;
        }

        return count;
    }
}