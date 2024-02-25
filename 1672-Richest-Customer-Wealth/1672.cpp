class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int num_rows = accounts.size();
        int num_columns = accounts[0].size();
        int richest = 0;
        for (int i=0;i<num_rows;++i){
            int tempSum = 0;
            for (int j=0;j<num_columns;++j){
                tempSum+= accounts[i][j];
            }
            if (tempSum>richest){
                richest = tempSum;
            }
        }
        return richest;
    }
};
