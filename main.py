import pygame
import time
import random
#import global_direction


global_direction = 1
class snejk():
    def __init__(self):

        pygame.init()

        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.green_snake = (0, 150, 0)

        self.dis_width = 600
        self.dis_height = 400

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake')

        self.clock = pygame.time.Clock()

        self.snake_block = 20
        self.food_block = 50
        self.snake_speed = 3
        self.score = 0

        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)

        self.apple_img = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/apple.png").convert_alpha()
        self.apple_img = pygame.transform.scale(self.apple_img, (self.food_block, self.food_block))

        self.head_img_top = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/blackhead20top.png").convert_alpha()
        self.head_img_left = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/blackhead20left.png").convert_alpha()
        self.head_img_right = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/blackhead20right.png").convert_alpha()
        self.head_img_down = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/blackhead20down.png").convert_alpha()
        #self.snake_img = pygame.transform.scale(self.snake_img, (self.snake_block, self.snake_block))

        self.tail_img_top = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/tail20top.png").convert_alpha()
        self.tail_img_left = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/tail20left.png").convert_alpha()
        self.tail_img_right = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/tail20right.png").convert_alpha()
        self.tail_img_down = pygame.image.load("/Users/Voytek/Desktop/Programming/Python/keras_mfcc/images/tail20down.png").convert_alpha()
        #self.tail_img = pygame.transform.scale(self.tail_img, (self.snake_block, self.snake_block))


    def turn_snakes_head(self, x, y):
        if global_direction == 0:
            snake_head_turned = self.head_img_down
        if global_direction == 1:
            snake_head_turned = self.head_img_top
        if global_direction == 3:
            snake_head_turned = self.head_img_left
        if global_direction == 4:
            snake_head_turned = self.head_img_right
        self.dis.blit(snake_head_turned, (x, y))

    def tail_direction(self, x, y, direct):
        if direct == 0:
            tail_turned = self.tail_img_down
        if direct == 1:
            tail_turned = self.tail_img_top
        if direct == 3:
            tail_turned = self.tail_img_left
        if direct == 4:
            tail_turned = self.tail_img_right
        self.dis.blit(tail_turned, (x, y))


    def snake_image(self, x, y):
        self.dis.blit(self.snake_img, (x, y))


    def apple(self, x, y):
        self.dis.blit(self.apple_img, (x, y))

    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.yellow)
        self.dis.blit(value, [0, 0])


    def our_snake(self, snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.black, [x[0], x[1], snake_block, snake_block])


    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])


    def gameLoop(self):
        game_over = False
        game_close = False


        x1 = round(self.dis_width / 2 / self.snake_block) * self.snake_block
        y1 = round(self.dis_height / 2 / self.snake_block) * self.snake_block

        x1_change = 0
        y1_change = -1

        snake_List = []
        Length_of_snake = 35

       # for i in range(self.snake_block,1, -1):
        #    snake_List.append([round(self.dis_width / 2 / self.snake_block) * self.snake_block, round(self.dis_height / 2 / self.snake_block) * self.snake_block + 1])

        foodx = round(random.randrange(0, self.dis_width - self.snake_block, self.snake_block))
        foody = round(random.randrange(0, self.dis_height - self.snake_block, self.snake_block))

        while not game_over:

            while game_close == True:
                self.dis.fill(self.blue)
                self.message("You Lost! Press C-Play Again or Q-Quit", self.red)
                self.Your_score(self.score)

                pygame.display.update()


                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.score = 0
                            self.gameLoop()
                            '''
            #print(global_direction.direction)
            if global_direction.direction == 0:
                y1_change = self.snake_block
                x1_change = 0
            elif global_direction.direction == 1:
                y1_change = -self.snake_block
                x1_change = 0
            elif global_direction.direction == 3:
                x1_change = -self.snake_block
                y1_change = 0
            elif global_direction.direction == 4:
                x1_change = self.snake_block
                y1_change = 0
            '''
            global global_direction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -1
                        y1_change = 0
                        global_direction = 3
                    elif event.key == pygame.K_RIGHT:
                        x1_change = 1
                        y1_change = 0
                        global_direction = 4
                    elif event.key == pygame.K_UP:
                        y1_change = -1
                        x1_change = 0
                        global_direction = 1
                    elif event.key == pygame.K_DOWN:
                        y1_change = 1
                        x1_change = 0
                        global_direction = 0



            if x1 >= self.dis_width:
                x1 = 0 #-x1_change
            elif x1 < 0:
                x1 =  self.dis_width #round(self.dis_width / self.snake_block) * self.snake_block
            if y1 >= self.dis_height:
                y1 = 0 # -y1_change
            elif y1 < 0:
                y1 = self.dis_height #round(self.dis_height / self.snake_block) * self.snake_block
            x1 += x1_change
            y1 += y1_change

            self.dis.fill(self.blue)
            #pygame.draw.rect(self.dis, self.green, [foodx, foody, self.food_block, self.food_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_Head.append(global_direction)
            snake_List.append(snake_Head)


            if len(snake_List) > Length_of_snake:
                del snake_List[0]



            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            self.our_snake(self.snake_block, snake_List)
            self.Your_score(self.score)
            self.apple(foodx, foody)
            self.turn_snakes_head(snake_List[-1][0], snake_List[-1][1])
            self.tail_direction(snake_List[0][0], snake_List[0][1], snake_List[0][2])
            #self.snake_image(snake_List[-1][0], snake_List[-1][1])
    
            pygame.display.update()

            if x1 >= foodx and x1 <= foodx+self.food_block and y1 >= foody and y1 <= foody + self.food_block:
                foodx = round(random.randrange(0, self.dis_width - self.food_block, self.snake_block))
                foody = round(random.randrange(0, self.dis_height - self.food_block, self.snake_block))
                Length_of_snake += self.snake_block
                self.score += 1
                

            self.clock.tick(40)

        pygame.quit()
        quit()


waz = snejk()
waz.gameLoop()

