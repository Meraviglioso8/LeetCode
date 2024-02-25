class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int l = nums.size();
        vector<int> sum;
        int addSum=0;
        for (int i=0;i<l;++i){
                addSum += nums[i];
                sum.push_back(addSum);
        }
        return sum;
    }
};
