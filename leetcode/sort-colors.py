class Solution {
    public void sortColors(int[] nums) {
        int s = 0;
        int c = 0;
        int e = nums.length-1;

        while(c <= e ){

            if( nums[c] == 0 ){
                swap(nums , s , c);
                s++;
                c++;
            }

            else if(nums[c] == 1 )c++;

            else{
                swap(nums , c , e);
                e--;
            }

        }
    }

    void swap(int[] nums , int i , int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j]  = temp;
    }
}