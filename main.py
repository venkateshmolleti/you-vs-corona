import pygame
from pygame import event
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1280,720))
mixer.music.load('nightmare.wav')
mixer.music.play(-1)
pygame.display.set_caption("you v/s corona")
icon = pygame.image.load('patient.png')
pygame.display.set_icon(icon)
ven=pygame.image.load('patient.png')
bg=pygame.image.load('download.jpg')
bull=pygame.image.load('hand-sanitizer.png')
bx=0
by=650
bxc=0
byc=20
bstate="ready"
px=300
py=650
score=0
font=pygame.font.Font('freesansbold.ttf',32)
tfont=pygame.font.Font('freesansbold.ttf',64)
textx=10
texty=10


def show(x,y):
    scorev=font.render("score :" +str((score)) ,True,(255,255,255))
    screen.blit(scorev, (x, y))
def gameover():
    textfont=tfont.render("GAME OVER\nSTAY HOME\nSTAY SAFE",True,(255,255,255))
    screen.blit(textfont, (0, 400))


def play(px,py):
    screen.blit(ven,(px,py))
pc=0
emy=[]
ex=[]
ey=[]
emxc=[]
emyc=[]
for i in range(6):
    emy.append(pygame.image.load('bacteria.png'))
    ex.append(random.randint(0,226))
    ey.append(random.randint(0,217))
    emxc.append(8)
    emyc.append(50)

def enemy(ex,ey,j):
    screen.blit(emy[j],(ex,ey))
def fire(bx,by):
    global bstate
    bstate="fire"
    screen.blit(bull,(bx+16,by+10))
def collision(bx,by,ex,ey):
    c=(((bx-ex)**(2))+((by-ey)**(2)))**(0.5)
    if(c<27):
        return True
    return False
h=0
t=True
while(t):
    #screen.fill((0,0,250))
    screen.blit(bg,(0,0))
    for i in pygame.event.get():
        if(i.type==pygame.QUIT):
            t=False
        if(i.type==pygame.KEYDOWN):
            if(i.key==pygame.K_LEFT):
                pc=-10
            if (i.key == pygame.K_RIGHT):
                    pc = 10
            if (i.key == pygame.K_SPACE):
                if(bstate=="ready"):
                    bultsound=mixer.Sound('laser.wav')
                    bultsound.play()
                    bx=px
                    fire(bx,by)

        if(i.type==pygame.KEYUP):
            if(i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT ):
                pc=0

    px+= pc
    if (px <= 0):
        px = 0
    elif (px >= 1200):
        px = 1200
    for j in range(6):
        if(ey[j]>600):
            for k in range(6):
                ey[j]=100000
            gameover()
            break
        ex[j]+=emxc[j]
        if (ex[j]<= 0):
            emxc[j] = 8
            ey[j]+=emyc[j]
        elif (ex[j] >= 1200):
            emxc[j]= -8
            ey[j]+=emyc[j]
        co = collision(bx, by, ex[j], ey[j])
        if (co):
            by = 650
            bstate = "ready"
            score += 1
            print(score)
            ex[j]=random.randint(0, 226)
            ey[j]=random.randint(0, 217)
        enemy(ex[j],ey[j],j)
    if(by<=0):
        by=650
        bstate="ready"
    if(bstate == "fire"):
        fire(bx,by)
        by-=byc
    co=collision(bx,by,ex[j],ey[j])
    if(co):
        mixer.Sound('explosion.wav').play()
        by=650
        bstate="ready"
        score+=1
        #print(score)
        ex[j] = random.randint(0, 226)
        ey [j]= random.randint(0, 217)
    play(px,py)
    show(textx,texty)
    pygame.display.update()
    continue


