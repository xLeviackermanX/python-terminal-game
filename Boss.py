from random import randint
from PowerUp import *
from Bricks import *
import os
class Boss:
    def __init__(self,x):
        self.posX = x
        self.posY = 5
        self.strength = 5
        
    def move(self,dash):
        self.posX = dash.posX

    def createBomb(self,powerups):
        value = randint(0,10)
        if value == 0:
            os.system("aplay mixkit-short-explosion-1694.wav > /dev/null 2>&1 &")
            x = Bomb(self.posX,self.posY)
            powerups.append(x)
        return powerups

    def createWall(self,bossBricks):
        for br in bossBricks:
            br.strength = 0
        return bossBricks


