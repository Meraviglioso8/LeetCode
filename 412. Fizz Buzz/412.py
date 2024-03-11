class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = list()
        for i in range(n):
            i += 1
            print(i)
            if i % 3 == 0 and i % 5 == 0:
                l.insert(i,"FizzBuzz")
            elif i % 3 == 0:
                l.insert(i,"Fizz")
            elif i % 5 == 0:
                l.insert(i,"Buzz")
            else: 
                l.insert(i,str(i))
        return l
