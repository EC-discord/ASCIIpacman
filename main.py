import pacman
from game import game
import ghost

game=game()
pacman=pacman.pacman(1, 1, game.grid)
ghost=ghost.ghost(len(game.grid)-2, len(game.grid[0])-2, game.grid)

while not game.win:
    game.show() #shows the current state of the grid
    if game.remainingDots==0:
        game.win=True
    if not pacman.alive:
        print("YOU DIED")
        print("GAME OVER")
        break
    if game.win:
        print("YOU WIN")
        break
    dir=input('enter a direction(wasd): ')
    pacman.move(dir, game.grid, game)
    ghost.calculatePath(pacman)
    ghost.move(ghost.direction, game.grid, pacman)