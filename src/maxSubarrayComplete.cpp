class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int max_sf = -999;
        int max_current = 0;
        int max_element = -99999;
        
        for (int i=0; i< nums.size();i++){
            
            if (nums[i] > max_element){
                max_element = nums[i];
            }
            
        }
        if (max_element < 0) {
            return max_element;
        }
        
        
        for (int i=0; i< nums.size();i++) {
            max_current += nums[i];
            
            if (max_current > max_sf) {
                max_sf = max_current;
            }
            if (max_current < 0) {
                max_current = 0;
            }
            
            
        }
        
        return max_sf;
    }
};
