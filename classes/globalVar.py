import pygame
from math import pi, cos, sin

class globalVar:
    def __init__(self):
        self.sW, self.sH = 1000,800
        self.dirs = [1, 2, 3, 4]
        self.WASD = [0, 0, 0, 0]
        self.space = False
        self.done = False
        self.pDir = 0
        self.basePSpeed = 10
        self.pSpeed = 10
        self.dashMulti = 3
        self.gX, self.gY = 0, 0
        self.clock = pygame.time.Clock()
        self.newDir = 0

        self.dashEffectTimer = 0
        self.dashEffectCooldown = 0
        
        pygame.init()

        self.screen = pygame.display.set_mode([self.sW, self.sH])

        self.baseCharSprite = pygame.image.load("media/images/nugglett.jpg").convert()

        self.baseCharSprite = pygame.transform.scale(self.baseCharSprite, (50,50))
        self.actualCharSprite = self.baseCharSprite
        
        self.backSprite = pygame.image.load("media/images/2d.jpg").convert()

    def setsWsH(self, newsW, newsH):
        self.sW = newsW
        self.sH = newsH

    def getsW(self):
        return self.sW
        
    def getsH(self):
        return self.sH
    
    def exit(self):
        pygame.quit()
    
    def updateKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.done = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:self.done = True
                if event.key == pygame.K_w or event.key == pygame.K_UP: self.WASD[0] = 1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: self.WASD[1] = 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN: self.WASD[2] = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT: self.WASD[3] = 1
                if event.key == pygame.K_SPACE: self.space = True
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_w or event.key == pygame.K_UP: self.WASD[0] = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: self.WASD[1] = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN: self.WASD[2] = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT: self.WASD[3] = 0
                if event.key == pygame.K_SPACE: self.space = False

    
    def updateScreen(self):
        self.screen.blit(self.backSprite, (self.sW/2 - self.gX, self.sH/2 + self.gY))
        self.screen.blit(self.actualCharSprite, (self.sW/2, self.sH/2))
        pygame.display.flip()
        self.screen.fill(pygame.Color(0,0,0))
        self.clock.tick(60)

    
    def updateChar(self):

        if self.space:
            if self.dashEffectCooldown == 0:
                self.dashEffectTimer = 12
                self.dashEffectCooldown = 60

        if self.dashEffectTimer > 0:
            self.pSpeed = self.basePSpeed * self.dashMulti
            self.dashEffectTimer -= 1
        else:
            self.pSpeed = self.basePSpeed

        if self.dashEffectCooldown > 0:
            self.dashEffectCooldown -= 1

        q = sum(self.WASD)

        if (q == 1):

            self.newDir = self.dirs[self.WASD.index(1)]

        elif (q == 2) and (self.WASD[0] != self.WASD[2]):
                
                self.newDir = 0
                for i in range(4):
                    self.newDir = self.newDir + self.WASD[i]*self.dirs[i]/2

                if (self.WASD[0] == 1) and (self.WASD[3]==1):
                    self.newDir = 1/2

        elif (q == 3):
            self.newDir = self.dirs[self.WASD.index(0)] + 2

        if (q != 0) and (q != 4):
            self.gX = self.gX + self.pSpeed*cos((pi/2)*self.newDir)
            self.gY = self.gY + self.pSpeed*sin((pi/2)*self.newDir)

            if(self.newDir > 1) and (self.newDir < 3):
                self.actualCharSprite = pygame.transform.flip(self.baseCharSprite, True, False)
            else:
                self.actualCharSprite = self.baseCharSprite