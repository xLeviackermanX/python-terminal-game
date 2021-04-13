class Dash: 

    def __init__(self,x,y,speed):
        self.posX = x
        self.posY = y
        self.size = 8
        self.speed = speed
        self.isCanon = False

    def changeSpeed(self , increment):
        self.speed+=increment

    def changeSize(self, flag):
        if flag>0 and self.size<12:
            self.size+=4

        if flag<0 and self.size>4:
            self.size-=4

        return self

    def move(self,direction):
        x = self.posX
        x+= direction*self.speed
        if x<=2:
            x = 3;
        if x+self.size>118:
            x = 118-self.size;
        self.posX = x


