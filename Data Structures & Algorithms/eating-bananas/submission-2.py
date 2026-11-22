class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         l,b = math.ceil(sum(piles)/h) , max(piles)
         while( l <= b):
            time = 0
            k = l + (b-l)//2
            print(k,l,b)
            for pile in piles:
                time += math.ceil(pile/k)
            print(time)
            if time <= h:
                ans = k
                b = k - 1
            else:
                l = k + 1
         return ans
               