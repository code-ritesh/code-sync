class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int mindiff = Integer.MAX_VALUE;

        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        for (int i = 1; i < arr.length; i++) {
            int currdiff = arr[i] - arr[i - 1]; 

            if (currdiff < mindiff) {
                res.clear();           
                mindiff = currdiff;

                curr.add(arr[i - 1]);
                curr.add(arr[i]);
                res.add(new ArrayList<>(curr));
                curr.clear();
            }
            else if (currdiff == mindiff) {
                curr.add(arr[i - 1]);
                curr.add(arr[i]);
                res.add(new ArrayList<>(curr));
                curr.clear();
            }
        }

        return res;
    }
}