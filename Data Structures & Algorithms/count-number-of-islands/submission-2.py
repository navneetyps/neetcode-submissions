class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        island_count = 0
        n, m = len(grid),len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j]=="1":
                    island_count +=1
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        a,b = queue.popleft()
                        if grid[a][b]=="1":
                            for x,y in directions:
                                xn,yn = a+x,b+y
                                if xn >= 0 and xn < n and yn>= 0 and yn < m: 
                                    if (xn,yn) not in visited:
                                        visited.add((xn,yn))
                                        queue.append((xn,yn))
        return island_count




