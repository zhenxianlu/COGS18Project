import pygame
import random

X = 500
Y = 500
class Snake(object):
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.sbody = []
        
        for x in range(3):
            self.addbody()

    def addbody(self):
        x,y = (0,0)
        if self.sbody:
            x,y = (self.sbody[0].x, self.sbody[0].y)
        sbody = pygame.Rect(x,y,20,20)
        if self.dirction == pygame.K_LEFT:
            sbody.x -= 20
        elif self.dirction == pygame.K_RIGHT:
            sbody.x += 20
        elif self.dirction == pygame.K_UP:
            sbody.y -= 20
        elif self.dirction == pygame.K_DOWN:
            sbody.y += 20
        self.sbody.insert(0,sbody)
    
    def deletebody(self):
        self.sbody.pop()

    def move(self):
        self.addbody()
        self.deletebody()

    def changedirection(self,di):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if di in LR + UD:
            if (di in LR) and (self.dirction in LR):
              return
            if (di in UD) and (self.dirction in UD):
              return
            self.dirction = di
        
    def dead(self):
        if self.sbody[0].x not in range(X):
            return True
        if self.sbody[0].y not in range(Y):
            return True
        if self.sbody[0] in self.sbody[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.rect = pygame.Rect(-20,0,20,20)

    def remove(self):
        self.rect.x = -20

    def pos(self):
        if self.rect.x == -20:
            position = []

            for pos in range (20,X-20,20):
                position.append(pos)
            self.rect.x = random.choice(position)
            self.rect.y = random.choice(position)
            print(self.rect)