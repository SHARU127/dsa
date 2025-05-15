class Solution {
    public int findNumbers(int[] nums) {
       
        int count=0;
        for(int arr: nums){
            if(even(arr)){
                count++;
            }
        }
      return count;
    }

    boolean even(int arr){
        int digit = digit(arr);
        return digit%2 == 0;
    }

    int digit(int n){
       return (int)(Math.log10(n))+1;
    }
}