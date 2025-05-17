class Solution {
    public void sortColors(int[] nums) {
        int start =0;
        int mid =0;
        int end = nums.length-1;
        int temp;

//when mid is greater than end looop breaks
        while(mid <= end){
            if(nums[mid] == 0){
                temp = nums[start];
                nums[start]=nums[mid];
                nums[mid]=temp; 
                
                //when u get 0 at mid index then swap with start, 0 comes at begimnig 
                start++;
                mid++;
                
                }
            else if(nums[mid] == 1){

                //when 1 is encountered dont change, just increment mid and dont move the start index
                mid++;
            }

            else{
                //end is dercemented, swap is done bw mid & end
                temp = nums[end];
                nums[end]=nums[mid];
                nums[mid]=temp; 
                
                end--;

            }
        }
        
        
        
                
            
        
    }
}