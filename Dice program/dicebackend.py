import random

class Player():
    def __init__ (self):
        self.pos=1
        self.ladder={'4':56,'12':50,'14':55,'22':58,'41':79,'54':88}
        self.snake={'96':42,'94':71,'75':32,'47':16,'37':3,'28':10}
    def setpos(self):
        self.pos=1
    def dice(self):
        self.rad=random.randint(1,6)
        return self.rad
    def position(self,pos):
        if (self.pos+pos)<100:
            self.pos+=pos
        else:
            self.pos=200-(self.pos+pos)
        return self.pos
    def check(self):
        if str(self.pos) in self.ladder:
            self.pos=self.ladder[str(self.pos)]
        elif str(self.pos) in self.snake:
            self.pos=self.snake[str(self.pos)]
        return self.pos
    def checkcoor(self):
        if(self.pos%20==0):
            self.x=0
            self.y=10-self.pos//10
        elif(self.pos%10==0):
            self.x=9
            self.y=10-self.pos//10
        elif (self.pos//10)%2==1:
            self.x=10-self.pos+((self.pos//10)*10)
            self.y=9-self.pos//10
        else:
            self.x=self.pos-((self.pos//10)*10)-1
            self.y=9-self.pos//10
        return self.x,self.y
