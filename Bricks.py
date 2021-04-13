from random import *
import numpy as np
class Bricks:
    def __init__(self,x,y):
        self.dimX=6 
        self.dimY=1
        self.posX = x
        self.isRainbow = False
        self.posY = y

    def moveDown(self):
        self.posY+=1
        return self

    #def decStrength(self):
     #   self.strength = -1
    def explode(self,bricks):
        for br in bricks:
            if br.strength<0:
                continue
            elif br.posX>=self.posX-6 and br.posX<=self.posX+6 and br.posY>=self.posY-1 and br.posY<=self.posY+1:
                br.strength = -1
                br.isRainbow = False
                if(br.change==-8):
                    bricks = br.explode(bricks)            
        return bricks



class FixedBricks(Bricks): 
    def __init__(self , x, y):
        super().__init__(x,y)
        self.strength = 3
        self.change = 0

class BossBricks(Bricks):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.strength = -1
        self.change = -1

class OneBricks(Bricks): 
    def __init__(self , x, y):
        super().__init__(x,y)
        self.strength = 0
        self.change = -1
        val = randint(0,10)
        if val==0:
            self.isRainbow = True

class TwoBricks(Bricks): 
    def __init__(self , x, y):
        super().__init__(x,y)
        self.strength = 1
        self.change = -1
        val = randint(0,10)
        if val==0:
            self.isRainbow = True


class ThreeBricks(Bricks): 
    def __init__(self , x, y):
        super().__init__(x,y)
        self.strength = 2
        self.change = -1
        val = randint(0,10)
        if val==0:
            self.isRainbow = True

class BonusBricks(Bricks):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.strength = 7
        self.change = -8

    
