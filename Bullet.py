from Boss import *
from Bricks import *
class Bullet:
    def __init__(self,x,y):
        self.posX = x
        self.posY = y
        self.speed = -2

    
def move(bullets,bricks,boss,bossBricks):
    def func(e):
        return e.posY
    bricks.sort(key = func,reverse=True)
    for b in bullets:
        flag = False
        for br in bricks:
            if br.strength<0:
                continue
            if b.posX>=br.posX and b.posX<=br.posX+5 and (b.posY-1==br.posY or b.posY-2==br.posY):
                br.strength+=br.change
                br.isRainbow = False
                if br.change==-8:
                    bricks = br.explode(bricks)
                flag = True
            if flag==True:
                break
        if flag==True:
            bullets.remove(b)
            continue
        if b.posX==boss.posX and(b.posY-1==boss.posY or b.posY-2==boss.posY)and boss.strength>=0:
            boss.strength-=1
            if boss.strength==1 or boss.strength==3:
                bossBricks = boss.createWall(bricks)
            flag = True
            bullets.remove(b)
            continue

        for br in bossBricks:
            if br.strength<0:
                continue
            if b.posX>=br.posX and b.posX<=br.posX+5 and(b.posY-1==br.posY or b.posY-2==br.posY):
                br.strength = -1
                flag = True
                break
        if flag==True or b.posY-2<=4:
            bullets.remove(b)
        else:
            b.posY-=2

    return [bullets,bricks,boss,bossBricks]
                            


