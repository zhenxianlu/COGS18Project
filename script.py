# Final Project: Snake Game
# Using the module pygame to create a snake game
# After running, a screen will pop up
# and a pink snake will show on the topleft of the screen
# with a random black dot (food)
# the goal of this game is to eat as much food as you can
# every dot you eat will add 10 points to your total score
# but if you hit the wall or hit yourself, 
# the game is over. 


import pygame as pg
from my_module import functions as fn


X = 500
Y = 500
def main():
    pg.init()
    screen_size = (X,Y)
    screen = pg.display.set_mode(screen_size)
    pg.display.set_caption("Snake")
    clock = pg.time.Clock()
    score = 0
    dead = False

    snake = fn.Snake()
    food = fn.Food()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == False:
                    return main()
        screen.fill((255,236,50))

        dead = snake.dead()
        if dead:
            sfont = pg.font.SysFont('arial',40)
            screen.blit(sfont.render('Game Over!',1,(227,29,18)),(140,200))
            sfont = pg.font.SysFont('arial',20)
            screen.blit(sfont.render('Score:{}'.format(score),1,(0,0,22)),(20,400))
        
        if not dead:
            snake.addbody()
            snake.deletebody()
        for rect in snake.sbody:
           pg.draw.rect(screen,(255,153,153),rect,0)
        if food.rect == snake.sbody[0]:
            score+=10
            snake.addbody()
            food.remove()

        food.pos()
        pg.draw.rect(screen,(0,0,0),food.rect,0)

        pg.display.update()
        clock.tick(6)
main()