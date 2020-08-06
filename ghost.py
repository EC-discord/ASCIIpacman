import random
import pacman

class ghost:
    def __init__(self, x, y, grid):
        self.x=x
        self.y=y
        self.path=None
        self.tempx=x
        self.tempy=y
        self.prevChar=grid[self.x][self.y]
        self.direction=None
        grid[self.x][self.y]=self

    def __str__(self):
        return "G"

    def calculatePath(self, pacman):
        #selects a random direction to move in and if that direction 
        #is not taking it closer to pacman, selects a random one again, recursively
        self.tempx=self.x
        self.tempy=self.y
        choices=[("x", 1), ("x", -1), ("y", 1), ("y", -1)]
        self.path=random.choice(choices)
        if self.path[0]=="x":
           if self.path[1]==1:
               self.tempx+=1
           if self.path[1]==-1:
                self.tempx-=1
        if self.path[0]=="y":
            if self.path[1]==1:
                self.tempy+=1
            if self.path[1]==-1:
                self.tempy-=1
        if (abs(self.tempx-pacman.x)>abs(self.x-pacman.x)) or (abs(self.tempy-pacman.y)>abs(self.y-pacman.y)):
            self.calculatePath(pacman)
        else:
            if self.tempx>self.x:
                self.direction="d"
            if self.tempx<self.x:
                self.direction="u"
            if self.tempy>self.y:
                self.direction="r"
            if self.tempy<self.y:
                self.direction="l"

    def move(self, direction, g, p):
        if direction=='r' and g[self.x][self.y+1]!='#':   
            g[self.x][self.y]=self.prevChar 
            self.y+=1
            if isinstance(g[self.x][self.y], pacman.pacman):
                p.alive=False
            g[self.x][self.y]=self
        if direction=='l' and g[self.x][self.y-1]!='#':
            g[self.x][self.y]=self.prevChar          
            self.y-=1
            if isinstance(g[self.x][self.y], pacman.pacman):
                p.alive=False
            g[self.x][self.y]=self
        if direction=='u' and g[self.x-1][self.y]!='#': 
            g[self.x][self.y]=self.prevChar         
            self.x-=1
            if isinstance(g[self.x][self.y], pacman.pacman):
                p.alive=False
            g[self.x][self.y]=self
        if direction=='d' and g[self.x+1][self.y]!='#': 
            g[self.x][self.y]=self.prevChar          
            self.x+=1
            if isinstance(g[self.x][self.y], pacman.pacman):
                p.alive=False
            g[self.x][self.y]=self