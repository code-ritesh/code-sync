class Solution {
    public int search(int[] nums, int target) {
        int s = 0;
        int e = nums.length-1;
        
        while(s <= e ){
            int mid =  s + (e-s)/2;

            if(nums[mid] == target) return mid;

            // left half sorted
            else if(nums[s] <= nums[mid]){
                // check target in it
                if( target >= nums[s] && target < nums[mid] ){
                    return helper(nums,s,mid-1,target);
                }

                else s = mid+1;
            }

            // right half sorted
            else if( nums[mid] <= nums[e]){
                // checks target
                if(target > nums[mid] && target <= nums[e]){
                    return helper(nums,mid+1,e,target);
                }

                else e = mid-1;
            }
        }


        return -1;

    }

    int helper(int[] nums, int s, int e, int target) {
        if (s > e)
            return -1;

        while (s <= e) {
            int mid = s + (e - s) / 2;

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                s = mid + 1;
            else
                e = mid - 1;
        }

        return -1;
    }

}