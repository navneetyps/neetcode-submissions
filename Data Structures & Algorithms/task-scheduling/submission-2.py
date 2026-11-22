class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
        ans = 0
        for task in tasks:
            task_dict[task]+=1
        queue = deque()
        pq = []
        for key in task_dict.keys():
            if task_dict[key]!=0:
                heapq.heappush(pq,(-task_dict[key],key))
        wait = n
        while pq or queue:
            ans += 1

            if pq:
                freq, char = heapq.heappop(pq)
                if freq + 1 != 0:
                    queue.append((ans + n, freq + 1, char))

            if queue and queue[0][0] == ans:
                _, f, c = queue.popleft()
                heapq.heappush(pq, (f, c))

        return ans