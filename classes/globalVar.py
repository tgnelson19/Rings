import pygame
from math import pi

class globalVar:
    def __init__(self):
        self.sW, self.sH = 1920, 1080
        self.WASD = [0,0,0,0] #WASD
        self.dirs = [pi/2, pi, -pi/2, 0]
        self.space = False
        self.pDir = 0
        self.pSpeed = 0

    def setsWsH(self, newsW, newsH):
        sW = newsW
        sH = newsH

    def getsW(self):
        return self.sW
        
    def getsH(self):
        return self.sH
    
    def update(self, newWASD):

        if (sum(self.WASD) == 0):
            self.pDir = 0 
            self.pSpeed = 0