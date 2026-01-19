class Solution {

    HashMap<String, Boolean> map = new HashMap<>();

    public boolean isScramble(String a, String b) {
        int n = a.length();

        if (n != b.length())
            return false;
        if (a.equals(b))
            return true;
        if (n <= 1)
            return false;

        String key = a + " " + b;
        if (map.containsKey(key))
            return map.get(key);

        for (int i = 1; i < n; i++) {

            // without swap
            boolean withoutSwap = isScramble(a.substring(0, i), b.substring(0, i)) &&
                    isScramble(a.substring(i), b.substring(i));

            // with swap
            boolean withSwap = isScramble(a.substring(0, i), b.substring(n - i)) &&
                    isScramble(a.substring(i), b.substring(0, n - i));

            if (withoutSwap || withSwap) {
                map.put(key, true);
                return true;
            }
        }

        map.put(key,false);

        return false;
    }
}