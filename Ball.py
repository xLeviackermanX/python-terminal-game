from math import *
import os
from Bricks import *
import PowerUp
import sys

class Ball:

    def __init__(self, x , y , speedX , speedY, inBoard):
        self.posX = x
        self.posY = y
        self.speedX = speedX
        self.speedY = speedY
        self.inBoard = inBoard

    def changeSpeedX(self,x):
        self.speedX += x
        return self

    def changeSpeedY(self,y):
        self.speedY += y
        return self
    
    def checkCollisionWithWalls(self,ix,iy):
        yo = False
        if self.posX+ix>=118:
            self = self.changeSpeedX(-2*self.speedX)
            yo = True
        if self.posX+ix<=2:
            self = self.changeSpeedX(-2*self.speedX)
            yo = True
        if self.posY+iy<=4:
            self = self.changeSpeedY(-2*self.speedY)
            self.posY = 5
            yo = True
        if self.posY+iy>39:
            self = self.changeSpeedY(-2*self.speedY)
            yo = True
            self.inBoard = False
        if yo==True:
            os.system("aplay mixkit-light-impact-on-the-ground-2070.wav > /dev/null 2>&1 &")
        return self
            
    def checkCollisionWithBricks(self,bricks,powerups,ix,iy,thruFlag,flag):
        yo = False
        x = self.posX+ix
        y = self.posY+iy
        def func(e):
            return e.posX
        if ix==1:
            bricks.sort(key = func)
        else:
            bricks.sort(key = func , reverse = True)

        for br in bricks:
            if br.strength<0:
                continue
            elif ix==1 and iy!=0 and x==br.posX and y==br.posY:
                self = self.changeSpeedX(-2*self.speedX)
                self = self.changeSpeedY(-2*self.speedY)
                self.posX+=ix
                self.posY+=iy
                yo = True
                br.isRainbow = False
                if thruFlag==1:
                    br.strength=-1
                else:
                    br.strength+=br.change
                if br.strength==-1:
                    powerup= PowerUp.create(br.posX,br.posY,-self.speedX,-self.speedY)
                    powerups.append(powerup)
                if br.change==-8 or flag==True:
                    flag = False
                    bricks = br.explode(bricks)
                break
            elif ix==-1 and iy!=0 and x==br.posX+5 and y==br.posY:
                self = self.changeSpeedX(-2*self.speedX)
                self = self.changeSpeedY(-2*self.speedY)
                self.posX+=ix
                self.posY+=ix
                if thruFlag==1: 
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
                br.isRainbow = False

                if br.strength==-1:
                    powerup= PowerUp.create(br.posX,br.posY,-self.speedX,-self.speedY)
                    powerups.append(powerup)
                if br.change==-8 or flag==True:
                    flag=False
                    bricks = br.explode(bricks)
                break
            elif self.posY==br.posY and (x==br.posX or x==br.posX+5):
                self = self.changeSpeedX(-2*self.speedX)
                self.posX+=ix
                self.posY-=iy
                if thruFlag==1:
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
                br.isRainbow = False

                if br.strength==-1:
                    powerup = PowerUp.create(br.posX,br.posY,-self.speedX,self.speedY)
                    powerups.append(powerup)
                if br.change == -8 or flag==True:
                    flag = False
                    bricks = br.explode(bricks)
                break
            elif self.posX>=br.posX and self.posX<=br.posX+5 and y==br.posY:
                self = self.changeSpeedY(-2*self.speedY)
                self.posX-=ix
                self.posY+=iy
                if thruFlag==1:
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
                br.isRainbow = False

                if br.strength==-1:
                    powerup=PowerUp.create(br.posX,br.posY,self.speedX,-self.speedY)
                    powerups.append(powerup)
                if br.change ==-8 or flag==True:
                    flag=False
                    bricks = br.explode(bricks)
                break
        if yo==True:
            os.system("aplay mixkit-light-impact-on-the-ground-2070.wav > /dev/null 2>&1 &")
        return [self,bricks,powerups,flag]

    def checkCollisionWithBossBricks(self,bricks,ix,iy,thruFlag):
        yo = False
        x = self.posX+ix
        y = self.posY+iy
        def func(e):
            return e.posX
        if ix==1:
            bricks.sort(key = func)
        else:
            bricks.sort(key = func , reverse = True)

        for br in bricks:
            if br.strength<0:
                continue
            elif ix!=0 and iy!=0 and x==br.posX and y==br.posY:
                self = self.changeSpeedX(-2*self.speedX)
                self = self.changeSpeedY(-2*self.speedY)
                self.posX+=ix
                self.posY+=iy
                yo = True
                if thruFlag==1:
                    br.strength=-1
                else:
                    br.strength+=br.change
                break
            elif ix!=0 and iy!=0 and x==br.posX+5 and y==br.posY:
                self = self.changeSpeedX(-2*self.speedX)
                self = self.changeSpeedY(-2*self.speedY)
                self.posX+=ix
                self.posY+=ix
                if thruFlag==1: 
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
                break
            elif self.posY==br.posY and (x==br.posX or x==br.posX+5):
                self = self.changeSpeedX(-2*self.speedX)
                self.posX+=ix
                self.posY-=iy
                if thruFlag==1:
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
               
                break
            elif self.posX>=br.posX and self.posX<=br.posX+5 and y==br.posY:
                self = self.changeSpeedY(-2*self.speedY)
                self.posX-=ix
                self.posY+=iy
                if thruFlag==1:
                    br.strength=-1 
                else:
                    br.strength+=br.change
                yo = True
                
                break
        return [self,bricks]

    def checkCollisionWithBoss(self,br,bricks,ix,iy):
        yo = False
        x = self.posX+ix
        y = self.posY+iy
        if br.strength<0:
            return self,br,bricks
        elif ix!=0 and iy!=0 and x==br.posX and y==br.posY:
            self = self.changeSpeedX(-2*self.speedX)
            self = self.changeSpeedY(-2*self.speedY)
            self.posX+=ix
            self.posY+=iy
            yo = True
            
        elif ix!=0 and iy!=0 and x==br.posX+5 and y==br.posY:
            self = self.changeSpeedX(-2*self.speedX)
            self = self.changeSpeedY(-2*self.speedY)
            self.posX+=ix
            self.posY+=ix
            yo = True
        elif self.posY==br.posY and (x==br.posX or x==br.posX+5):
            self = self.changeSpeedX(-2*self.speedX)
            self.posX+=ix
            self.posY-=iy
           
            yo = True
           
        elif self.posX>=br.posX and self.posX<=br.posX+5 and y==br.posY:
            self = self.changeSpeedY(-2*self.speedY)
            self.posX-=ix
            self.posY+=iy
           
            yo = True

        if yo==True:
            br.strength-=1
            if br.strength==1 or br.strength==3:
                bricks = br.createWall(bricks)
        if yo==True:
            os.system("aplay mixkit-short-explosion-1694.wav > /dev/null 2>&1 &")
        return self,br,bricks
         
    def checkCollisionWithDash(self,dash,bricks,ix,iy):
       yo = False
       if self.posX+ix>=dash.posX and self.posX+ix<dash.posX+dash.size and self.posY+iy==dash.posY:
            yo = True
            self = self.changeSpeedY(-2*self.speedY)
            k = int(dash.size/4)
            delta = abs(self.speedY)
            if self.posX+ix>=dash.posX and self.posX+ix<dash.posX+k:
                self = self.changeSpeedX(-2*delta)
            elif self.posX+ix>=dash.posX+k and self.posX+ix<dash.posX+2*k:
                self = self.changeSpeedX(-delta)
            elif self.posX+ix>=dash.posX+2*k and self.posX+ix<dash.posX+3*k:
                self = self.changeSpeedX(delta)
            else:
                self = self.changeSpeedX(2*delta)
            for br in bricks:
                br = br.moveDown()
       if yo == True:
           os.system("aplay mixkit-light-impact-on-the-ground-2070.wav > /dev/null 2>&1 &")
       return self,bricks

    def move(self,bricks,dash,powerups,boss,bossBricks,thruFlag,flag):
        y = abs(self.speedY)
        x = abs(self.speedX)
        if self.speedX!=0:
            ix = int(self.speedX/x)
        else:
            ix = 0
        iy = int(self.speedY/y)
        k = int(x/y)
        if(k==0):
            for i in range(y):
                self ,bricks= self.checkCollisionWithDash(dash,bricks,0,iy)
                self = self.checkCollisionWithWalls(0,iy)
                iy = int(self.speedY/y)
                self, boss, bossBricks= self.checkCollisionWithBoss(boss,bossBricks,0,iy)
                iy = int(self.speedY/y)
                l = self.checkCollisionWithBricks(bricks,powerups,0,iy,thruFlag,flag)
                self = l[0]
                bricks = l[1]
                powerups = l[2]
                flag = l[3]
                l = self.checkCollisionWithBossBricks(bossBricks,0,iy,thruFlag)
                self = l[0]
                bossBricks = l[1]
                iy = int(self.speedY/y)
                self.posY+=iy
        else:
            for i in range(y):
                for j in range(k-1):
                    self,bricks = self.checkCollisionWithDash(dash,bricks,ix,0)
                    self = self.checkCollisionWithWalls(ix,0)
                    if self.speedX!=0:
                        x = abs(self.speedX)
                        ix = int(self.speedX/x)
                    self, boss, bossBricks= self.checkCollisionWithBoss(boss,bossBricks,ix,0)
                    l = self.checkCollisionWithBricks(bricks,powerups,ix,0,thruFlag,flag)
                    self = l[0]
                    bricks = l[1]
                    powerups = l[2]
                    flag = l[3]
                    l = self.checkCollisionWithBossBricks(bossBricks,ix,0,thruFlag)
                    self = l[0]
                    bossBricks = l[1]
                    x = abs(self.speedX)
                    ix = 0
                    if self.speedX!=0:
                        ix = int(self.speedX/x)
                    self.posX+=ix
        
                self,bricks = self.checkCollisionWithDash(dash,bricks,ix,iy)
                self = self.checkCollisionWithWalls(ix,iy)
                iy = int(self.speedY/y)
                x = abs(self.speedX)
                if x!=0:
                    ix = int(self.speedX/x)
                self, boss, bossBricks = self.checkCollisionWithBoss(boss,bossBricks,ix,iy)
                l = self.checkCollisionWithBricks(bricks,powerups,ix,iy,thruFlag,flag)
                self = l[0]
                bricks = l[1]
                powerups = l[2]
                flag = l[3]
                l = self.checkCollisionWithBossBricks(bossBricks,ix,iy,thruFlag)
                self = l[0]
                bossBricks = l[1]
                x = abs(self.speedX)
                ix = 0
                if self.speedX!=0:
                    ix = int(self.speedX/x)
                iy = int(self.speedY/y)
                self.posX+=ix
                self.posY+=iy
        return [self, bricks , powerups,boss, bossBricks,flag]
