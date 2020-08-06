from dot import dot

class pacman:
    def __init__(self, x, y, grid):
        self.alive=True
        self.x=x
        self.y=y
        self.prevChar=grid[self.x][self.y] #stores what was at the current coorindates 
                                           #before pacman moved there
        grid[self.x][self.y]=self #initializes pacman at the given coordinates

    def __str__(self):
        return "C"

    def move(self, direction, g, game):
        #checks if the coordinates pacman moves to is a wall(#) before moving
        #and if it's a dot, the dot count is reduced
        if direction=='d' and g[self.x][self.y+1]!='#':
            g[self.x][self.y]=" "
            self.y+=1
            g[self.x][self.y]=self
            if isinstance(self.prevChar, dot):
                game.remainingDots-=1
        if direction=='a' and g[self.x][self.y-1]!='#':
            g[self.x][self.y]=" "
            self.y-=1
            g[self.x][self.y]=self
            if isinstance(self.prevChar, dot):
                game.remainingDots-=1
        if direction=='w' and g[self.x-1][self.y]!='#':
            g[self.x][self.y]=" "
            self.x-=1
            g[self.x][self.y]=self
            if isinstance(self.prevChar, dot):
                game.remainingDots-=1
        if direction=='s' and g[self.x+1][self.y]!='#':
            g[self.x][self.y]=" "
            self.x+=1
            g[self.x][self.y]=self
            if isinstance(self.prevChar, dot):
                game.remainingDots-=1