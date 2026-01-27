class Solution {
    public int searchInsert(int[] arr, int target) {
        int s = 0;
        int e = arr.length-1;

        int res = -1;

        while(s <= e ){
            int mid = s + (e-s)/2;

            if( arr[mid] == target ){
                return mid;
            }

            else if( arr[mid] < target ){
                res = mid;
                s = mid+1;
            }

            else e = mid-1;
        }

        return res+1;
    }
}