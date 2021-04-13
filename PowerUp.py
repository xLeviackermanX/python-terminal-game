from random import randint 
from Ball import *
import numpy as np
def create(x,y,speedX,speedY):
    num = randint(0,6)
    if num==0:
        obj = ExpandPaddle(x,y,speedX,speedY)
        return obj
    elif num==1:
        obj = ShrinkPaddle(x,y,speedX,speedY)
        return obj
    elif num==2:
        obj = BallMultiplier(x,y,speedX,speedY)
        return obj
    elif num==3:
        obj = FastBall(x,y,speedX,speedY)
        return obj
    elif num==4:
        obj = ThruBall(x,y,speedX,speedY)
        return obj
    elif num==5:
        obj = Canon(x,y,speedX,speedY)
        return obj
    else:
        obj = FireBall(x,y,speedX,speedY)
        return obj


class PowerUp:
    def __init__(self,x,y,speedX,speedY,s):
        self.posX = x
        self.posY = y
        self.counter=0
        self.speed = speedY
        self.speedX = speedX
        self.strength = s

    def move(powerups,balls,dash,timer):
        for p in powerups:
            p.counter+=1
            z = int(p.counter/4)
            if p.strength==14:
                z=0
            if p.posX+p.speedX<=2 or p.posX+p.speedX>=119:
                p.speedX = -p.speedX
            elif p.posY+p.speed+z<=4:
                p.speed = -p.speed-z
                p.counter = 0
            elif p.posY+p.speed+z>=dash.posY and p.posX+max(0,p.speedX)>=dash.posX and p.posX+min(0,p.speedX)<dash.posX+dash.size:
                l = p.boost(balls,dash,timer)
                balls = l[0]
                dash = l[1]
                timer = l[2]
                powerups.remove(p)
            
            elif p.posY+p.speed+z>dash.posY:
                powerups.remove(p)

            else:
                p.posY+=p.speed+z
                p.posX+=p.speedX

        return [powerups,balls,dash,timer]

class ExpandPaddle(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,9)

    def boost(self,balls,dash,timer):
        timer[0] = 120
        return [balls,dash,timer]

class ShrinkPaddle(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,10)

    def boost(self,balls,dash,timer):
        timer[1]=120
        return [balls,dash,timer]

class BallMultiplier(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,11)
    
    def boost(self,balls,dash,timer):
        ball = []
        for b in balls:
            newB = Ball(b.posX,b.posY,-b.speedX,-b.speedY,True)
            ball.append(b)
            ball.append(newB)
        return [ball,dash,timer]

class FastBall(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,12)

    def boost(self,balls,dash,timer):
        timer[3] = 120
        return [balls,dash,timer]

class ThruBall(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,13)
        
    def boost(self,balls,dash,timer):
        timer[4] = 120
        return [balls,dash,timer]

class Bomb(PowerUp):
    def __init__(self,x,y):
        super().__init__(x,y,0,1,14)

    def boost(self,balls,dash,timer):
        timer[5] = 120
        return [balls,dash,timer]

class Canon(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,15)

    def boost(self,balls,dash,timer):
        timer[6] = 120
        dash.isCanon = True
        return [balls,dash,timer]

class FireBall(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        super().__init__(x,y,speedX,speedY,16)

    def boost(self,balls,dash,timer):
        timer[7] = True
        return [balls,dash,timer]

