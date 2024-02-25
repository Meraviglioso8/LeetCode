class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        num_rows = len(accounts)
        num_columns = len(accounts[0]) 
        richest = 0
        for i in range (num_rows):
            temp = 0
            for j in range (num_columns):
                temp += accounts[i][j]
            if (temp > richest):
                richest = temp
        return richest
