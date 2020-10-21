from tkinter import Tk,Canvas,Button,Label,PhotoImage,BOTH,NORMAL,messagebox
import random,time
from PIL import ImageTk,Image
import dicebackend as db
imgn={'1':36,'2':9,'3':18,'4':54,'5':27,'6':0}#image photo to gif
SIDE=50
WIdTH=HEIGHT=SIDE*10+2

class SNL():
    def __init__(self):
        self.app=Tk()
        self.app.title("Snake and Ladder")
        self.pos=1
        self.count=0
        self.player=db.Player()
        self.__UI()

    def __UI(self):
        self.canv1=Canvas(self.app,width=WIdTH,height=HEIGHT+40)
        self.canv2=Canvas(self.app,width=WIdTH,height=50)
        self.canv1.pack(expand="yes")
        self.canv2.pack(expand="no")
        img=Image.open("s1.png")
        img=img.resize((WIdTH,HEIGHT+40),resample=0)
        self.slimg=ImageTk.PhotoImage(img)
        self.canv1.create_image(0,0,image=self.slimg,state=NORMAL,anchor="nw")
        self.dicephoto=[PhotoImage(file="dic.gif",format="gif -index %i" %(i)) for i in range(64)]
        self.lab=Label(self.canv2,image=self.dicephoto[36])
        self.lab.pack(side="left")
        self.btndice=Button(self.canv2,text="dice",width=10,height=2,command=self.dice,bg="green")
        self.btndice.pack(side="right")
        self.__creatpos()
    def dice(self):
        dice_rad=self.player.dice()
        self.pos=self.player.position(dice_rad)
        self.count+=1
        for i in range(64):
            time.sleep(0.01)
            self.lab.configure(image=self.dicephoto[i])
            self.lab.update_idletasks()

        img=imgn[str(dice_rad)]
        self.lab.configure(image=self.dicephoto[img])
        self.__creatpos()
        time.sleep(1)
        self.canv1.update_idletasks()
        self.pos=self.player.check()
        self.__creatpos()
        if self.pos==100:
            messagebox.showinfo("win","Congratuation You win in {} move\nDo you want to play more game:".format(self.count))
            self.count=0
            self.pos=1
            self.player.setpos()
            self.__creatpos()
    def __creatpos(self):
        self.canv1.delete("pla1")
        self.canv1.delete("ins")
        self.x,self.y=self.player.checkcoor()
        x1=self.x*50+15
        y1=self.y*50+15
        x2=x1+25
        y2=y1+25
        self.canv1.create_oval(x1,y1,x2,y2,width=2,fill="red",tag="pla1")
        self.canv1.create_oval(x1+3,y1+3,x2-3,y2-3,width=1,tag="ins")
        self.canv1.update_idletasks()
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    snl=SNL()
    snl.run()
