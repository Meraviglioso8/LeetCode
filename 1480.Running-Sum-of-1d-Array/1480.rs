impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut sum: Vec<i32> = Vec::new();
        let mut addSum: i32 = 0;
        for num in &nums {
            addSum+=num;
            sum.push(addSum);
    }
        return sum;
    }
}
