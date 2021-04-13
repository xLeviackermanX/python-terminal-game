import externalClasses as ex
import numpy as np
import subprocess
from random import randint,seed

class Game:
    
    def __init__(self,level,base,life):
        self.bricks=[]
        self.total = 0
        self.base = base
        self.bullets = []
        self.level = level
        if self.level==2:
            ex.os.system("aplay mixkit-quick-bomb-drop-explosion-1697.wav > /dev/null 2>&1 &")
        seed(1) 
        self.boss = ex.Boss(57)
        if level!=2:
            self.boss.strength = -1
        self.bossBricks = []
        j=4
        while j<=117:
            b = ex.BossBricks(j,8)
            self.bossBricks.append(b)
            j+=6

        if level==0:
            i = 10
            while i<=14:
                j = 30
                while j<=90:
                    value = randint(0,4)
                    if value==0:
                        b = ex.OneBricks(j,i)
                        self.total+=1
                        self.bricks.append(b)
                    elif value==1:
                        self.total+=2
                        b = ex.TwoBricks(j,i)
                        self.bricks.append(b)
                    elif value==2:
                        self.total+=3
                        b = ex.ThreeBricks(j,i)
                        self.bricks.append(b)
                    elif value==3:
                        self.total+=4
                        b = ex.FixedBricks(j,i)
                        self.bricks.append(b)
                    else:
                        self.total+=8
                        b = ex.BonusBricks(j,i)
                        self.bricks.append(b)
                    j+=6
                i+=1
        elif level==1:
            i = 8
            while i<=30:
                j = 15
                while j<=116:
                    value = randint(0,10)
                    if value==0:
                        b = ex.OneBricks(j,i)
                        self.total+=1
                        self.bricks.append(b)
                    elif value==1:
                        self.total+=2
                        b = ex.TwoBricks(j,i)
                        self.bricks.append(b)
                    elif value==2:
                        self.total+=3
                        b = ex.ThreeBricks(j,i)
                        self.bricks.append(b)
                    elif value==3:
                        self.total+=4
                        b = ex.FixedBricks(j,i)
                        self.bricks.append(b)
                    elif value==4:
                        self.total+=8
                        b = ex.BonusBricks(j,i)
                        self.bricks.append(b)
                    j+=6
                i+=1

        else:
            i=10
            while i<=20:
                j = 5
                while j<=112:
                    value = randint(3,20)
                    if value==0:
                        b = ex.OneBricks(j,i)
                        self.total+=1
                        self.bricks.append(b)
                    elif value==1:
                        self.total+=2
                        b = ex.TwoBricks(j,i)
                        self.bricks.append(b)
                    elif value==2:
                        self.total+=3
                        b = ex.ThreeBricks(j,i)
                        self.bricks.append(b)
                    elif value==3:
                        self.total+=4
                        b = ex.FixedBricks(j,i)
                        self.bricks.append(b)
                    elif value==100:
                        self.total+=8
                        b = ex.BonusBricks(j,i)
                        self.bricks.append(b)
                    j+=6
                i+=1

 
        #b = ex.BonusBricks(57,11)
        #self.bricks.append(b)
        self.dash = ex.Dash(57,38,2)
        self.score = base
        self.lives = life
        self.getch =ex.GetchUnix()
        self.quit = 1
        self.moveBricks = False
        ball = ex.Ball(60,38,0,-1,True)
        self.balls = []
        self.balls.append(ball)
        self.thruFlag = 0
        self.powerups = []
        self.timer = [0,0,0,0,0,0,0,False]
        self.moveBrickTimer = 20
        self.timer = np.array(self.timer)

    def alarmHandler(self,signum, frame):
        raise ex.AlarmException

    def takeInput(self,timeout=0.5):
        ex.signal.signal(ex.signal.SIGALRM, self.alarmHandler)
        ex.signal.setitimer(ex.signal.ITIMER_REAL,timeout)
        try:
            #while ex.signal.getitimer(ex.signal.ITIMER_REAL):
                #print(ex.signal.getitimer(ex.signal.ITIMER_REAL))
            key = self.getch()
            # if key=='a':
            #     self.dash.move(-1)
            # elif key=='d':
            #     self.dash.move(1)
            # elif key=='q':
            #     ex.sys.exit(0)
            # subprocess.call('clear')
            # x = ex.Board()
            # x.makeGrid(self.bricks,self.dash,self.balls,self.powerups)
            # x.renderBoard(self.dash)
            ex.signal.setitimer(ex.signal.ITIMER_REAL,0)
            return key
        except ex.AlarmException:
            print('',end=''),
        ex.signal.setitimer(ex.signal.ITIMER_REAL,0)
        ex.signal.signal(ex.signal.SIGALRM, ex.signal.SIG_IGN)
        return ''

    def waitTime(self,timeout=0.1):
        ex.signal.signal(ex.signal.SIGALRM,self.alarmHandler)
        ex.signal.setitimer(ex.signal.ITIMER_REAL,timeout)
    	#ex.signal.signal(ex.signal.SIGALRM,self.alarmHandler)
       # ex.signal.setitimer(ex.signal.ITIMER_REAL,timeout)
        try:
            while ex.signal.getitimer(ex.signal.ITIMER_REAL)!=0:
            	a = 1
            ex.signal.setitimer(ex.signal.ITIMER_REAL,0)
            return '' 
        except ex.AlarmException:
            print('',end=''),
        ex.signal.setitimer(ex.signal.ITIMER_REAL,0)
        ex.signal.signal(ex.signal.SIGALRM, ex.signal.SIG_IGN)
        return ''

    def moveBalls(self):
        # print(yoyo)
        for b in self.balls:
            l = b.move(self.bricks,self.dash,self.powerups,self.boss,self.bossBricks,self.thruFlag,self.timer[7])
            b = l[0]
            self.bricks = l[1]
            self.powerups = l[2]
            self.boss = l[3]
            self.bossBricks = l[4]
            self.timer[7] = l[5]
            if b.inBoard == False:
                self.balls.remove(b)
        #print(b.posY,b.speedY)

    def usePowerUps(self):
        if self.timer[0]>self.timer[1] and self.timer[0]>0:
            self.dash.size = 12
        if self.timer[1]>self.timer[0] and self.timer[1]>0:
            self.dash.size = 4
        if self.timer[3]==120:
            for b in self.balls:
                if b.speedY!=2 and b.speedY!=-2:
                    b = b.changeSpeedX(b.speedX)
                    b = b.changeSpeedY(b.speedY)
        if self.timer[5]==120:
            self.lives-=1
        if self.timer[4]==120:
            self.thruFlag=1
        if self.timer[6]>0 and self.timer[6]%6==0:
            self.dash.isCanon = True
            ex.os.system("aplay mixkit-laser-cannon-shot-1678.wav > /dev/null 2>&1 &")
            b = ex.Bullet(self.dash.posX,self.dash.posY)
            b1 = ex.Bullet(self.dash.posX+6,self.dash.posY)
            self.bullets.append(b)
            self.bullets.append(b1)
    
    def checkIfLost(self):
        if len(self.balls)==0:
            self.lives-=1
            if self.lives <1:
                print('Sorry you lost all your lives!')
                self.quit = 0
            else:
                ball = ex.Ball(60,38,0,-1,True)
                self.balls.append(ball)
                self.dash.posX = 57
        for br in self.bricks:
            if br.strength>0 and br.posY>=37:
                print('Sorry you lost and the game is over!')
                self.lives=-1
                self.quit = 0
                break
        if self.lives<1:
            print('Sorry you lost all your lives!')
            self.quit = 0

    def checkIfWon(self):
        flag = 0
        self.score = 0
        for br in self.bricks:
          #  print(br.streng)
            if br.strength >= 0:
                if br.strength!=3:
                    flag =1
                if br.isRainbow==True:
                	self.score+=1
                else:
                	self.score+=br.strength+1
        self.score = self.base+self.total - self.score
        if (flag==0 and self.level!=2) or (self.level==2 and self.boss.strength<0):
            print('Congrats! You completed this round!.')
            self.quit = 0

    def changeColor(self):
        for br in self.bricks:
            if br.isRainbow==True:
                br.strength = int((br.strength+1)%3)

    def resetPowerUps(self):
        for i in range(0,7):
            self.timer[i]-=1
        self.moveBrickTimer-=1
        if self.moveBrickTimer==0 and self.level!=2:
            self.moveBricks = True
        if self.timer[0]==0 and self.dash.size==12:
            self.dash.size = 8
        if self.timer[1]==0 and self.dash.size==4:
            self.dash.size = 8
        if self.timer[3]==0:
            for b in self.balls:
                k = int(b.speedX/2)
                k1 = int(b.speedY/2)
                if b.speedY==2 or b.speedY==-2:
                    b = b.changeSpeedX(-k)
                    b = b.changeSpeedY(-k1)
        if self.timer[4]==0:
            self.thruFlag=0
        if self.timer[6]==0:
            self.dash.isCanon = False

    def play(self):
            while self.quit:
                self.changeColor()
                self.moveBalls()
                ex.os.system("clear")
                if self.boss.strength>=0:
                    self.powerups = self.boss.createBomb(self.powerups)
                l = ex.PowerUp.move(self.powerups,self.balls,self.dash,self.timer)
                self.powerups = l[0] 
                self.balls = l[1] 
                self.dash = l[2]
                self.timer = l[3]
                self.usePowerUps()
                self.resetPowerUps()
                l=ex.move(self.bullets,self.bricks,self.boss,self.bossBricks)
                self.bullets = l[0]
                self.bricks = l[1]
                self.boss = l[2]
                self.bossBricks = l[3]
                x = ex.Board()
                x.makeGrid(self.bricks,self.dash,self.balls,self.powerups,self.boss,self.bossBricks,self.bullets)
                x.renderBoard(self.dash,self.boss.strength,self.score,self.lives,self.level,self.timer[6],self.timer[7])
                self.checkIfLost()
                self.checkIfWon()
                key = self.takeInput()
                if key=='a':
                    self.dash.move(-1)
                elif key=='d':
                    self.dash.move(1)
                elif key=='q':
                    ex.sys.exit(0)
                elif key=='x':
                    self.quit = 0
                if self.boss.strength>=0:
                    self.boss.move(self.dash)
               # key = self.waitTime()
