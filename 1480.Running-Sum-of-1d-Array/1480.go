func runningSum(nums []int) []int {  //  [] slice of sth
    l := len(nums)
    var sum [] int
    addSum := 0
    for i := 0; i < l; i++ {
        addSum += nums[i]
        sum=append(sum,addSum)
    }
    return sum
}
