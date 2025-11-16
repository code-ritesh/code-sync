class Solution {

    void helper(int[] candidates, int target , int idx , List<Integer> curr , List<List<Integer>> ans){
        int n = candidates.length;

        if(target < 0 ) return;

        if(target == 0 ){
            ans.add(new ArrayList<>(curr));
            return;
        }

        for(int i = idx ; i < n ; i++){
            if( i > idx && candidates[i] == candidates[i-1] ) continue;

            curr.add(candidates[i]);
            helper(candidates , target - candidates[i] ,  i + 1 , curr , ans);
            curr.remove(curr.size() - 1);
        }

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans  = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        Arrays.sort(candidates);

        helper(candidates , target , 0 , curr , ans);

        return ans;


    }
}