impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let num_rows = accounts.len();
        let num_columns = accounts[0].len();
        let mut richest = 0;
        for i in 0..num_rows{
            let mut temp = 0;
            for j in 0..num_columns{
                temp+=accounts[i][j];
            }
            if temp > richest {
                richest = temp;
            }
        }
        return richest;
    }
}
