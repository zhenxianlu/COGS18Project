import pygame as pg
import random

X = 500
Y = 500
class Snake(object):
    def __init__(self):
        rand_move = random.choice([pg.K_UP,pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT])
        self.dirction = rand_move
        self.sbody = []
        
        for x in range(1):
            self.addbody()

    def addbody(self):
        x,y = (220,220)
        if self.sbody:
            x,y = (self.sbody[0].x, self.sbody[0].y)
        sbody = pg.Rect(x,y,20,20)
        if self.dirction == pg.K_LEFT:
            sbody.x -= 20
        elif self.dirction == pg.K_RIGHT:
            sbody.x += 20
        elif self.dirction == pg.K_UP:
            sbody.y -= 20
        elif self.dirction == pg.K_DOWN:
            sbody.y += 20
        self.sbody.insert(0,sbody)
    
    def deletebody(self):
        self.sbody.pop()

    def changedirection(self,di):
        LR = [pg.K_LEFT, pg.K_RIGHT]
        UD = [pg.K_UP, pg.K_DOWN]
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
        self.rect = pg.Rect(-20,0,20,20)

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