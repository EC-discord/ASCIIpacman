import pacman
from game import game

game=game()
pacman=pacman.pacman(1, 1, game.grid)
while not game.win:
    game.show()
    if game.remainingDots==0:
        game.win=True
    if game.win:
        print("YOU WIN")
        break
    dir=input('enter a direction(wasd): ')
    pacman.move(dir, game.grid, game)