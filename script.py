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

# initialize screen size
X = 500
Y = 500

def main():
    pg.init()
    screen_size = (X,Y)
    # set the pygame screen size
    screen = pg.display.set_mode(screen_size)
    # assign the name of the screen
    pg.display.set_caption("Snake")
    # set the time lock
    clock = pg.time.Clock()
    # let the score 0 and set the snake alive
    score = 0
    dead = False

    #  call function Snake and Food
    snake = fn.Snake()
    food = fn.Food()

    while True:
        for event in pg.event.get():
            # if pygame is quit
            if event.type == pg.QUIT:
                # game stops
                return False
            # if there is keyboard pressing
            if event.type == pg.KEYDOWN:
                # change snake direction
                snake.changedirection(event.key)
                if event.key == False:
                    return main()
        screen.fill((255,236,50))

        # if the snake is dead
        dead = snake.dead()
        if dead:
            # the sentence "Game Over!" will show up on the screen
            sfont = pg.font.SysFont('arial',40)
            screen.blit(sfont.render('Game Over!',1,(227,29,18)),(140,200))
            # as well as the score
            sfont = pg.font.SysFont('arial',20)
            screen.blit(sfont.render('Score:{}'.format(score),1,(0,0,22)),(20,400))
        
        # if the snake is not dead
        if not dead:
            # snake will continue moving
            snake.addbody()
            snake.deletebody()
        for rect in snake.sbody:
           pg.draw.rect(screen,(255,153,153),rect,0)
        # if the snake ate the food
        if food.rect == snake.sbody[0]:
            # score add 10
            score+=10
            # add one node to snake body
            snake.addbody()
            # remove food
            food.remove()

        # draw food
        food.pos()
        pg.draw.rect(screen,(0,0,0),food.rect,0)

        # set the clock tick, the snake moving speed
        pg.display.update()
        clock.tick(6)
main()