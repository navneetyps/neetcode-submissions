class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        max_area = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
                queue = deque([(r,c)])
                grid[r][c] = 0
                area = 0
                while queue:
                    area +=1
                    a,b = queue.popleft()
                    for x,y in directions:
                        xn,yn = a +x,b+y
                        if xn >=0 and xn<rows and yn>=0 and yn<cols and grid[xn][yn] ==1:
                            grid[xn][yn] = 0
                            queue.append((xn,yn))
                return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area,bfs(i,j))  
        return max_area

