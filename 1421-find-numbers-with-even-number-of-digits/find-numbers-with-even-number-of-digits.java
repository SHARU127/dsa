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
        if(n < 0){
            n = n *-1;
        }
        
        if(n == 0){
         return 1;
        }
        int count=0;
        while(n > 0){
         count++;
         n=n/10;
        }
        return count;
    }
}