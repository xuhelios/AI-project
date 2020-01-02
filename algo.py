class App():
    def __init__(self):
        self.maze = []
        with open('data.txt', 'r') as f:
            self.x = int(f.readline())
            self.y = int(f.readline())
            self.w = int(f.readline())
            self.h = int(f.readline())
            l = [[int(num) for num in line.split()] for line in f]
            
        print(self.x, '  ', self.y)
        print("h = ",self.h, " w = ", self.w)
        print(l)
        self.maze = l

    def solve(self):

        found = False

        prev = []
        for item in range(self.h):
            bar = [(0,0) for i in range(self.w)]
            prev.append(bar)
        
        open = []
        open.append((self.x,self.y))
        close = []
        while open :
            print(open)
            print(close)
            p = open.pop(0)
            close.append(p)
            print(" p = ", p)
            if (self.maze[p[0]][p[1]] == -1):
                found = True
                break
            
            if (p[0] - 1 >= 0 and self.maze[p[0]-1][p[1]] != 1 and (not ((p[0]-1,p[1]) in close))): 
                q = (p[0]-1,p[1])
                if (not (q in open)):
                    open.append(q)
                    print("up")
                prev[q[0]][q[1]] = p
                

            if (p[0] + 1 < self.h and self.maze[p[0]+1][p[1]] != 1 and (not ((p[0]+1,p[1]) in close))): 
                q = (p[0]+1,p[1])
                if (not (q in open)):
                    open.append(q)
                    print("down")
                prev[q[0]][q[1]] = p
                

            if (p[1] - 1 >=0 and self.maze[p[0]][p[1]-1] != 1 and (not ((p[0],p[1]-1) in close))): 
                q = (p[0],p[1]-1)
                if (not (q in open)):
                    open.append(q)
                    print("left")
                prev[q[0]][q[1]] = p
                


            if (p[1] + 1 <self.w and self.maze[p[0]][p[1]+1] != 1 and (not ((p[0],p[1]+1) in close))): 
                q = (p[0],p[1]+1)
                if (not (q in open)):
                    open.append(q)
                    print("right")
                prev[q[0]][q[1]] = p


        print(found)
        return 0
    	
if __name__ == "__main__" :
    theApp = App()
    theApp.solve()
