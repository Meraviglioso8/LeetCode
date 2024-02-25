class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum =[]
        runSum = 0
        for i in range (len(nums)):
            runSum += nums[i]
            sum.append(runSum)
        return sum
