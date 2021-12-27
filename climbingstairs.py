class Solution:
    def climbStairs(self, n: int) -> int:
        if ( n == 1 ):
         return 1
        if  (n==2):
         return 2
 
        else:
         return findStep(n - 1) + findStep(n - 2)
        