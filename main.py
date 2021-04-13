from Game import Game
from getchunix import *
getch = GetchUnix()
flag = 1
while flag:
    print('To start the game press y and to exit press q')
    key = getch()
    if key == 'y':
        x = Game(0,0,3)
        x.play()
        if x.lives<1:
            print('Game over , you used all your lives and your final score is: ',x.score)
        else:
            y = Game(1,x.score,x.lives)
            y.play()
            if y.lives<1:
                print('Game over , you used all your lives and your final score is',y.score)
            else:
                z = Game(2,y.score,y.lives)
                z.play()
                print('Game over , your final score is',z.score)
    elif key == 'q':
        flag = 0
