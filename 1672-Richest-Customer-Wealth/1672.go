func maximumWealth(accounts [][]int) int {
    numRows := len(accounts)
    numColumns := len(accounts[0])
    richest := 0
     for i := 0; i < numRows; i++ {
         temp := 0
         for j:=0; j < numColumns; j++{
             temp += accounts[i][j]
         }
         if temp > richest{
             richest = temp
         }
     }
     return richest
}
