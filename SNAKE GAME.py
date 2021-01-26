import pygame
import random
import  os
pygame.mixer.init()

pygame.init()
gameWindow=pygame.display.set_mode((1200,700))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen_width = 1200
screen_height = 700
pygame.display.set_caption("SNAKE GAME-MADE BY DHEERAJ PANDEY")
bgimg=pygame.image.load("snake.jpeg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
clock=pygame.time.Clock()
font = pygame.font.SysFont(0, 55)
def plot_snake(gameWindow,red,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,red,[x,y,snake_size,snake_size])
def score_screen(text,color,x,y):
    screen_score=font.render(text,True,color)
    gameWindow.blit(screen_score,[x,y])
def welcome():
    game_exit=False
    while game_exit!=True:
        gameWindow.fill((240,210,150))
        score_screen("SNAKE GAME BY DHEERAJ",red,320,270)
        score_screen("Press space bar to continue the game",red,240,310)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit==True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('bgsound.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
def gameloop():
    if(not os.path.exists("Highscore.txt")):
        with open("Highscore.txt","w") as f:
            f.write("0")
    with open("Highscore.txt", "r") as f:
        Highscore = f.read()
    snake_x = 35
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 50
    score = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(30, screen_width / 2)
    food_y = random.randint(30, screen_height / 2)
    game_exit = False
    game_over = False
    while game_exit!=True:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(Highscore))
            gameWindow.fill(white)
            score_screen("!!Game Over!! Press Enter To Continue",blue,250,300)
            score_screen("Score:" + str(score), blue, 500, 250)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        velocity_y=-4
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=4
                        velocity_x=0
                    if event.key == pygame.K_RIGHT:
                        velocity_x=4
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-4
                        velocity_y=0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=10
                food_x = random.randint(30, screen_width / 2)
                food_y = random.randint(30, screen_height / 2)
                snake_length+=3
                if score>int(Highscore):
                    Highscore=score
            gameWindow.fill(green)
            gameWindow.blit(bgimg,(0,0))
            score_screen("Score :" + str(score) + "  High Score : "+ str(Highscore), blue, 5, 5)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, red, snake_list, snake_size)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()
welcome()
