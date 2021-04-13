import Bricks
from colorama import Fore , Back , Style
import numpy as np

class Board:
    def __init__(self):
        self.grid = [[-1]*122]*43

    def makeGrid(self,bricks,dash,balls,powerups,boss,bossBricks,bullets):
        #selfgrid = [[-1]*40]*40
        self.grid = np.array(self.grid)
        for br in bricks:
            self.grid[int(br.posY)][int(br.posX)] = br.strength
        for br in bossBricks:
            self.grid[int(br.posY)][int(br.posX)] = br.strength
        for b in bullets:
            self.grid[int(b.posY)][int(b.posX)] = 6
        for b in balls:
            self.grid[int(b.posY)][int(b.posX)] = 4
        for p in powerups:
            self.grid[int(p.posY)][int(p.posX)] = p.strength
        self.grid[int(dash.posY)][int(dash.posX)] = 5
        if boss.strength>=0:
            self.grid[int(boss.posY)][int(boss.posX)] = 20

    def renderBoard(self,dash,strength,score,lives,level,timer,flag):
        print('Your score is:',score,end='\t')
        print('\t\t\tLevel: ',level)
        print('Lives left:',lives,end='\t')
        print('\t\t\tHP: ',end=''),
        for i in range(0,strength+1):
            print('-',end=''),
        if timer>0:
            print('\t\t\tTimer: ',end=''),
            for i in range(0,int(timer/12)):
                print('=',end=''),
        print('')
        i=4
        while i<41:
            j=0
            while j<121:
                if (i==2 or i==4):
                    print('-',end=''),
                    j+=1
                elif (j==2 or j==119) and (i>4 and i<41):
                    print('*',end=''),
                    j+=1
                elif self.grid[i][j]<0:
                    print(' ',end=''),
                    j+=1
                elif self.grid[i][j]==4:
                    if flag==True:
                        print(Fore.RED+'@',end=''),
                    else:
                        print(Fore.CYAN+'@',end=''),
                    print(Style.RESET_ALL+'',end=''),
                    j+=1
                elif self.grid[i][j]==6:
                    print('$',end=''),
                    j+=1
                elif self.grid[i][j]==20:
                    for k in range(0,6):
                        print(Back.WHITE+' ',end=''),
                    j+=6
                    print(Style.RESET_ALL+'',end=''),
                elif self.grid[i][j]>=9 and self.grid[i][j]<=16:
                    print(self.grid[i][j]-8,end=''),
                    j+=1
                elif self.grid[i][j]==5:
                    if timer>0:
                        print(Back.RED+' ',end=''),
                    else:
                        print(Back.BLUE+' ',end=''),
                    for k in range(1,dash.size-1):
                        print(Back.BLUE+' ',end=''),
                    if timer>0:
                        print(Back.RED+' ',end=''),
                    else:
                        print(Back.BLUE+' ',end=''),
                    j+=dash.size
                    print(Style.RESET_ALL+'',end=''),
                else:
                    for k in range(0,6):
                        if self.grid[i][j]==0:
                            print(Back.LIGHTYELLOW_EX+' ',end=''),
                        elif self.grid[i][j]==1:
                            print(Back.YELLOW+' ',end=''),
                        elif self.grid[i][j]==2:
                            print(Back.GREEN+' ',end=''),
                        elif self.grid[i][j]==3:
                            print(Back.RED+' ',end=''),
                        else:
                            print(Back.MAGENTA+' ',end='')
                    j+=6
                    print(Style.RESET_ALL+'',end='')
            print('\n',end=''),
            i+=1
 


