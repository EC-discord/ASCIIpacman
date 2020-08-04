class pacman():
    def __init__(self, x, y, grid):
        self.char="C"
        self.x=x
        self.y=y
        self.prevChar=grid[self.x][self.y] #stores what was at the current coorindates before pacman moved there
        grid[self.x][self.y]="C"

    def move(self, direction, g, game):
        if direction=='w' and g[self.x-1][self.y]!='#':
            if hasattr(self.prevChar, "eatable"):
                self.prevChar=" "
            g[self.x][self.y]=self.prevChar
            self.x-=1             
        elif direction=='s' and g[self.x+1][self.y]!='#':
            if hasattr(self.prevChar, "eatable"):
                self.prevChar=" "
            g[self.x][self.y]=self.prevChar
            self.x+=1
        elif direction=='a' and g[self.x][self.y-1]!='#':
            if hasattr(self.prevChar, "eatable"):
                self.prevChar=" "
            g[self.x][self.y]=self.prevChar
            self.y-=1
        elif direction=='d' and g[self.x][self.y+1]!='#':
            if hasattr(self.prevChar, "eatable"):
                self.prevChar=" "
            g[self.x][self.y]=self.prevChar
            self.y+=1
        if hasattr(g[self.x][self.y], "eatable"):
            game.remainingDots-=1
        g[self.x][self.y]=self.char