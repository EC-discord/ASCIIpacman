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
        self.remainingDots=0
        for l in self.grid:
            for e in l:
                if e==d:
                    self.remainingDots+=1

    def show(self):
        for row in self.grid:
            for c in row:
                print(str(c), end="")
            print("\n")