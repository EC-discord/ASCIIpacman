from dot import dot

d=dot()

class game:
    def __init__(self):
        self.win=False
        self.grid=[
                  ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                  ['#',d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,'#'],
                  ['#',d,'#','#',d,d,d,d,d,d,d,d,d,d,'#','#',d,'#'],
                  ['#',d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,'#'],
                  ['#',d,'#','#',d,d,d,d,d,d,d,d,d,d,'#','#',d,'#'],
                  ['#',d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,'#'],
                  ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

        self.remainingDots=-1 #pacman starts on a dot so instead of starting count from 0, we start from -1
        for l in self.grid:
            for e in l:
                if e==d:
                    self.remainingDots+=1

    def show(self):
        for g in self.grid:
            for c in g:
                print(c, end="")
            print("\n")