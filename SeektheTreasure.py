#!/usr/bin/env python
# coding: utf-8

# In[3]:


###SEEK THE TREASURE: DUNGEON GAME###
###BY ANG LI-LIAN, CREATICA HACKATHON###
###Many thanks to #https://stackoverflow.com/questions/14700889/pygame-level-menu-states and TechTim PyGame Tutorial (YouTube)

import pygame
import random
import math

#initialise game
pygame.init()
win_h = 800
win_w = 800
win = pygame.display.set_mode((win_w, win_h))


#images
walkRight = [
    pygame.image.load("lovelaceR1.png"),
    pygame.image.load("lovelaceR2.png")
]
walkLeft = [
    pygame.image.load("lovelaceL1.png"),
    pygame.image.load("lovelaceL2.png")
]
walkDown = [
    pygame.image.load("lovelaceF1.png"),
    pygame.image.load("lovelaceF2.png")
]
walkUp = [
    pygame.image.load("lovelaceB1.png"),
    pygame.image.load("lovelaceB2.png"),
]

##bigger sprite for landing page
introwalkRight  = [
    pygame.image.load("introlovelaceR1.png"),
    pygame.image.load("introlovelaceR2.png")
]
introwalkLeft = [
    pygame.image.load("introlovelaceL1.png"),
    pygame.image.load("introlovelaceL2.png")
]
introchar = pygame.image.load("introlovelace.png")

char = pygame.image.load("lovelace.png")
fire = pygame.image.load("fire.png") #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
bg = pygame.image.load("bg.png")
block = pygame.image.load("square.png")
prize = pygame.image.load('treasure.png') #Icons made by <a href="https://www.flaticon.com/authors/ddara" title="dDara">dDara</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
heart = pygame.image.load("heart.png") #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#sounds
success= pygame.mixer.Sound('success.mp3') #https://freesound.org/s/456965/
lose = pygame.mixer.Sound('dead.wav') #https://freesound.org/s/253174/
hit = pygame.mixer.Sound('hit.wav') #https://freesound.org/s/425348/
##background music
music = pygame.mixer.music.load("music.mp3") #Music by Eric Matyas www.soundimage.org
pygame.mixer.music.play(-1)

#configuring levels
levels = {0:{'level': [
                    "P        P    PPPP  ",
                    "P  PPPPP  P PPPP PP ",
                    "P  P   P  P       P ",
                    "P  P   PP P PP PPPP ",
                    "PP PPP  P    P P    ",
                    "   P P  P  PPP PPPPP",
                    "     P  PPPP       P",
                    " P   P            PP",
                    " PPPPP PPPPPPPPPP P ",
                    "S      P          P ",
                    " PPPPP PPPPPPPPPPPP ",
                    "     P        P   P ",
                    " P P P PP PPP PP PP ",
                    " P P P  P P P  P P  ",
                    " P PPP    P P  P P  ",
                    " P P   PPPP PP P P P",
                    " P   PPP         P  ",
                    " PPP     PPPPPPP P T",
                    " P P PPPPP     P P P",
                    "   P       PP  P   P"]},
          1:{'level':[
                  "PPPPPPPPPPPPPPPPPPPP",    
                  "E      P   P      TP",
                  " PPPPPPP P PPP PPPPP",
                  "E        P     PE  P",
                  " PPP PPPPPPP PPP PPP",
                  "   P   P           P",
                  "PP PPPPPPPPPPPPP PPP",
                  " P P   P   P    E  P",
                  " PPP PPP PPP P PPP P",
                  "   PE       EP P   P",
                  " P P PPP PPPPPPPPPPP",
                  " P     P   P       P",
                  " PPPPPPPPP P PPPPP P",
                  "   P P     P     P P",
                  "PPPP P PPP P PPPPP P",
                  "   P   PE     EP P P",
                  " P P PPPPPPPPP P PPP",
                  "SP P   P       P   P",
                  " PPPPPPP P PPP PPP P",
                  "         P   P     P"]},
        2:{'level':[           
                    "PP  PPP    E P   PPP",
                    "PP  PPP   P  P   PPP",
                    "P         P       TP",
                    "P         P    PEPPP",
                    "P  P  PPPPPPP   PPPP",
                    "P  P    EPPPP   PPPP",
                    "PPPP  PP   P       P",
                    "PPPP  PP   P      EP",
                    "P E   P PP   PPPPPPP",
                    "P       PP     PPPPP",
                    "PP      EP      P PP",
                    "P  P PPP PPPPP E   P",
                    "P PP P P    P      P",
                    "P PPPP P PP  PP PP P",
                    "P         P     PPPP",
                    "PPPPPPPP  P  PP  PPP",
                    "P PPPPPP  P  PP  PPP",
                    "S      P  P  PP   PP",
                    "P      P  P  PP    P",
                    "P         P  PP   EP",
        ]
          }}


#template for each level
class Scene(object):
    def __init__(self):
        pass
    
    def render(self, win):
        raise NotImplementedError
        
    def update(self):
        raise NotImplementedError
    
    def handle_events(self, events):
        raise NotImplementedError

#landing page of game
class TitleScene(object):
    def __init__(self):
        super(TitleScene, self).__init__()
        self.ada =introplayer(win_w//2, win_h-32*5)
    
    def render(self, win):
        win.blit(bg,(0,0,win_w, win_h))
        
        font1 = pygame.font.SysFont('comicsans', 35, True)
        text1 = font1.render("Seek The Treasure", 1, (0,250,0))
        
        font2 =pygame.font.SysFont('comicsans', 25)
        text2 = font2.render("Press SPACE to begin.", 1, (0,250,0))
        
        font3 =pygame.font.SysFont('comicsans', 20, False, True)
        text3 = font3.render("Created by Ang Li-Lian with PyGames", 1, (0,250,0))
        
        win.blit(text1,(win_w//2- text1.get_width()/2, win_h//2- text1.get_height()/2- text2.get_height()/2))
        win.blit(text2,(win_w//2- text2.get_width()/2, win_h//2+text2.get_height()/2+ text1.get_height()/2))
        win.blit(text3,(win_w- text3.get_width()-10, 10))

        win.blit(prize, (win_w-50,  win_h-32*5, 32,32))
        
        for y in range(5):
            for x in range(win_w//32):
                win.blit(block,(x*32,win_h-32*y, 32,32))
        
        self.ada.draw(win)
        
        pygame.display.update()

    def update(self):
        keys = pygame.key.get_pressed()
        left, right = [keys[key] for key in (pygame.K_LEFT, pygame.K_RIGHT)]
        self.ada.move(left, right)
    
    def handle_events(self, events):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.manager.go_to(GameScene(0))

#manages movement between levels
class SceneManager(object):
    def __init__(self):
        self.go_to(TitleScene())
        
    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
        
#controls game play
class GameScene(Scene):
    def __init__(self,levelno):
        super(GameScene, self).__init__()
        self.enemygroup = pygame.sprite.Group()
        self.square = 40
        
        self.levelno =levelno
        
        levelinfo = levels[levelno]
        
        level = levelinfo["level"]
        self.maze = Maze(level)
        
        x = 0
        y = 0
        path = []
        for row in level:
            for col in row:
                if col == "T":
                    self.treasure = Treasure(x, y)
                if col == "E":
                    path.append([x,y])
                    if len(path) ==2:
                        e= Enemy(path[0][0],path[0][1], sorted(path, key = lambda x: x[0]))
                        self.enemygroup.add(e)
                        path = []
                if col =="S":
                    self.ada = player(x,y)
                    self.ada.scene = self
                x += self.square
            y += self.square
            x = 0
        
    def render(self, win):
        win.blit(bg,(0,0,win_w,win_h))  
        self.maze.drawMaze(win)
        self.treasure.draw(win)
        self.ada.draw(win)
        for e in self.enemygroup:
            e.draw(win,self.maze.wall, self.ada)
        
        for i in range(self.ada.lives):
            win.blit(heart, (win_w-40*i-50, 32, 32,32))
            
        pygame.display.update()
        
    def update(self):
        keys = pygame.key.get_pressed()
        up, left, right, down = [keys[key] for key in (pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN)]
        self.ada.move(up, left, right, down, self.maze.wall, self.treasure)
                    
    def exit(self):
        if self.levelno+1 in levels:
            self.manager.go_to(TransitionScene(self.levelno+1))
        else:
            self.manager.go_to(CustomScene("You win!", self.levelno))
            
    def die(self):
        self.manager.go_to(CustomScene("You lose!", self.levelno))

    def handle_events(self, events):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()              
        
#transition between levels
class TransitionScene(object):
    def __init__(self,levelno):
        self.levelno = levelno
        super(TransitionScene,self).__init__()
        
    def render(self, win):
        win.blit(bg,(0,0))
        
        font1 = pygame.font.SysFont('comicsans', 35, True)
        font2 = pygame.font.SysFont('comicsans', 25)
        font3= pygame.font.SysFont('comicsans', 20)
        
        text= font1.render("Good job passing Level "+ str(self.levelno) +"!" , 1, (0,250,0))
        
        text1 =font2.render("But that was a warm up." , 1, (0,250,0))
        text2=font2.render("You're getting the hang of it" , 1, (0,250,0))
        
        endtext = font3.render("Press Any Key to Continue", 1, (0,250,0))
        
        win.blit(text,(win_w//2- text.get_width()/2, win_h//2- text.get_height()*2))
        
        if self.levelno ==1:
            win.blit(text1,(win_w//2- text1.get_width()/2, win_h//2- text1.get_height()/2))
        if self.levelno==2:
            win.blit(text2,(win_w//2- text2.get_width()/2, win_h//2- text2.get_height()/2))
            
        win.blit(endtext,(win_w//2- endtext.get_width()/2, win_h//2+ endtext.get_height()*2))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.manager.go_to(GameScene(self.levelno))
        
    def update(self):
        pass
    
    def handle_events(self,events):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
#final scene after dead or winning
class CustomScene(object):
    def __init__(self, text, level):
        self.text = text
        self.level = level
        super(CustomScene, self).__init__()
    
    def render(self, win):
        win.blit(bg,(0,0))
        font = pygame.font.SysFont('comicsans', 30, True)
        if self.text =="You lose!":
            text = font.render(self.text + " Retry? (Y/N)", 1, (0,250,0))
        elif self.text =="You win!":
            text = font.render(self.text + " Play Again? (Y/N)", 1, (0,250,0))
        win.blit(text,(win_w//2- text.get_width()/2, win_h//2- text.get_height()/2))
        pygame.display.update()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_y]:
            if self.text =="You lose!":
                self.manager.go_to(GameScene(self.level))
            if self.text =="You Win!":    
                main()
        elif keys[pygame.K_n]:
            pygame.quit()

    def update(self):
        pass
    
    def handle_events(self, events):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


#defines the player. I named her Ada Lovelace!
class player(object):
    def __init__(self, x, y, lives =3 ):
        self.xstart = x
        self.ystart = y
        self.x = x
        self.y = y
        self.width = 16
        self.height = 32
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount_x = 0
        self.walkCount_y= 0
        self.rect = pygame.Rect(self.x, self.y, 23,37)
        self.lives = lives

    def draw(self, win):
        if self.walkCount_x + 1 >= 10:
            self.walkCount_x = 0
        if self.walkCount_y + 1 >= 10:
            self.walkCount_y = 0
            
        if self.left:
            win.blit(walkLeft[self.walkCount_x // 5], (self.x, self.y))
            self.walkCount_x += 1
        elif self.right:
            win.blit(walkRight[self.walkCount_x // 5], (self.x, self.y))
            self.walkCount_x += 1
        elif self.up:
            win.blit(walkUp[self.walkCount_y // 5], (self.x, self.y))
            self.walkCount_y += 1
        elif self.down:
            win.blit(walkDown[self.walkCount_y // 5], (self.x, self.y))
            self.walkCount_y += 1
        else:
            win.blit(char, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, 23,37)
        
    def move(self, up, left, right, down,wall, treasure):
        keys = pygame.key.get_pressed()
        
        #if player hits wall
        if self.rect.collidelist(wall)<0:
            if left and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
                self.up= False
                self.down =False

            elif right and self.x < win_w - self.width - self.vel:
                self.x += self.vel
                self.right = True
                self.left = False
                self.up= False
                self.down =False

            elif up and self.y > 0:
                self.y -= self.vel
                self.up = True
                self.down = False
                self.left= False
                self.right =False

            elif down and self.y + self.vel + self.height < win_h :
                self.y += self.vel
                self.down = True
                self.up = False
                self.left= False
                self.right =False

            else:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
                self.walkCount = 0
        else:
            if self.left == True:
                self.x += self.vel
            elif self.right == True:
                self.x -= self.vel
            elif self.up == True:
                self.y += self.vel
            else:
                self.y -=self.vel
        
        #if player gets treasure
        if self.rect.colliderect(treasure.rect):
            success.play()
            treasure.collect()
            self.scene.exit()
                

#limited functions of player for the landing page with bigger sprite
class introplayer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 64
        self.vel = 10
        self.left = False
        self.right = False
        self.walkCount_x = 0

    def draw(self, win):
        if self.walkCount_x + 1 >= 10:
            self.walkCount_x = 0
            
        if self.left:
            win.blit(introwalkLeft[self.walkCount_x // 5], (self.x, self.y))
            self.walkCount_x += 1
        elif self.right:
            win.blit(introwalkRight[self.walkCount_x // 5], (self.x, self.y))
            self.walkCount_x += 1
        else:
            win.blit(introchar, (self.x, self.y))
        
    def move(self, left, right):
        keys = pygame.key.get_pressed()
        
        if left and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False

        elif right and self.x < win_w - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False

        else:
            self.right = False
            self.left = False
            self.walkCount = 0
        
#builds the maze
class Maze(object):
    def __init__(self, maze):
        self.square = 40
        self.maze =maze
        self.wall = []
        
    def drawMaze(self, win):
        bx = 0
        by= 0
        for row in self.maze:
            for col in row:
                if col == "P":
                    win.blit(block,(bx, by, self.square, self.square))
                    self.wall.append((bx, by, self.square, self.square))
                bx+=self.square
            by+=self.square
            bx=0
                
#builds the treasure
class Treasure(object):
    def __init__(self,x, y):
        self.width = 32
        self.height = 32
        self.x = x
        self.y= y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.visible = True
        
    def draw(self,win):
        if self.visible:
            win.blit(prize, ( self.x, self.y,self.width, self.height))
    
    def collect(self):
        font = pygame.font.SysFont('comicsans', 30, True)
        text= font.render("Treasure Collected!", 1, (0,250,0))
        win.blit(text,(win_w//2- text.get_width()/2, win_h//2- text.get_height()/2))
        
        pygame.display.update()
        
        #delay time
        i= 0
        while i <100:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i= 101
                    pygame.quit()
                    
#builds each enemy                    
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y, path):
        pygame.sprite.Sprite.__init__(self)
        self.vel = 7
        self.walk = ["x","y"]
        self.x = x
        self.y = y
        self.path = path
        self.width = 32
        self.height = 32
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, win,wall,player):
        #for easier levels, enemy follows a fixed path only
        fixed = (self.path[1][1]==self.path[0][1],self.path[1][0]==self.path[0][0])
        if True in fixed:
            if fixed[0]== True:
                step ='x'
            elif fixed[1]==True:
                step='y' 
            self.move(wall,player, False, step)
        else:
            #extra challenge
            if self.isclose(player):
                self.move(wall,player, True)
            else:
                step = random.choice(self.walk)
                self.move(wall,player, False, step)

        win.blit(fire, (self.rect))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move(self, wall,player, close, step = None):   
        if step == 'x':
            if self.vel > 0:
                if self.x + self.vel < self.path[1][0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
            else:
                if self.x - self.vel > self.path[0][0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
        elif step =='y':
            if self.vel > 0:
                if self.y + self.vel < self.path[1][1]:
                    self.y += self.vel
                else:
                    self.vel = self.vel * -1
            else:
                if self.y - self.vel > self.path[0][1]:
                    self.y += self.vel
                else:
                    self.vel = self.vel * -1

        if close == True:
            if player.x < self.x:
                self.x -= self.vel/2
            elif player.x > self.x:
                self.x += self.vel/2
            elif player.y < self.y:
                self.y -= self.vel/2
            elif player.y > self.y:
                self.y += self.vel/2
        
        #hits the player and they lose a life
        if self.rect.colliderect(player.rect):
            if player.lives >1:
                hit.play()
                player.lives -= 1
                player.x, player.y = player.xstart, player.ystart
                font = pygame.font.SysFont('comicsans', 30, True)
                text= font.render("-1 Life :(", 1, (250,0,0))
                win.blit(text,(win_w//2- text.get_width()/2, win_h//2- text.get_height()/2))
                pygame.display.update()
                
                #delay time
                i= 0
                while i <100:
                    pygame.time.delay(10)
                    i+=1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i= 101
                            pygame.quit()
            else:
                lose.play()
                player.scene.die()
                
    #hard mode where the enemy follows player
    def isclose(self, player):
        a = self.x-player.x
        b= self.y - player.y
        distance = math.sqrt((a**2)+(b**2))
        
        if distance < 150:
            return True
        else:
            return False
                                   

#mainLoop
def main():
    pygame.display.set_caption("Seek the Treasure")
    clock = pygame.time.Clock() 
    
    run = True
    
    manager = SceneManager()
    
    while run:
        clock.tick(20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(win)
    
if __name__ == "__main__":
    main()
    
pygame.quit()

