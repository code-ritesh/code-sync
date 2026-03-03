class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int n = s.length();
        int i = 0;
        int maxlen = 0;

        for (int j = 0; j < n; j++) {
            char curr = s.charAt(j);

            map.put(curr, map.getOrDefault(curr, 0) + 1);

            while (map.get(curr) > 1) {

                char left = s.charAt(i);

                map.put(left, map.get(left) - 1);

                if (map.get(left) == 0)
                    map.remove(left);
                i++;
            }

            maxlen = Math.max(j - i + 1, maxlen);
        }

        return maxlen;
    }
}