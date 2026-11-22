class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = []
        ans = []
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        for i in range(0,k):
            ans.append(heapq.heappop(heap)[1])
        return ans
