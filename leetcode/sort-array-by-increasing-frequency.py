class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int a : nums) {
            map.put(a, map.getOrDefault(a, 0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a, b) -> map.get(a).equals(map.get(b)) ? b - a : map.get(a) - map.get(b)
        ); // this helps for  If multiple values have the same frequency, sort them in decreasing order

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            pq.add(entry.getKey());
        }

        int[] res = new int[nums.length];
        int idx = 0;

        while(!pq.isEmpty()){
            int num = pq.poll();
            int freq = map.get(num);

            for(int i = 0 ; i < freq ; i++){
                res[idx++] = num;
            }
        }

        return res;
    }
}