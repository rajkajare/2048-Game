import logic
import pygame
pygame.init()
pygame.mixer.init()










#### GAMEDISPLAY ####
dis_width = 800
dis_height = 600
gameDisplay = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()











#### COLOR ####
red = (255, 0, 0)
bright_red = (238, 75, 43)
green = (0, 255, 0)
bright_green = (170, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
background = "#92877d"
back_color = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8",
              8: "#f2b179", 16: "#f59563", 32: "#f67c5f",
              64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
              512: "#edc580", 1024: "#edc53f", 2048: "#edc22e" }
text_color = {0: "#9e948a", 2: "#776e65", 4: "#776e65",
              8: "#f9f6f2", 16: "#f9f6f2", 32: "#f9f6f2",
              64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
              512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}










#gameIcon
iconImg = pygame.image.load("icon.ico")
pygame.display.set_icon(iconImg)










#sound
won_song = pygame.mixer.Sound("sounds/won.mp3")
lose_song = pygame.mixer.Sound("sounds/lose.mp3")
comp_song = pygame.mixer.Sound("sounds/comp.mp3")
notcomp_song = pygame.mixer.Sound("sounds/notcomp.mp3")
def sound(statement):
    if statement == "notcomp":
        notcomp_song.play()
    elif statement == "comp":
        comp_song.play()
    elif statement == "YOU WON!!":
        won_song.play()
    else:
        lose_song.play()










#### INTERFACE ####
class block():

    block_width = 180
    block_height = 130

    def __init__(self, value, x_coordinate, y_coordinate):
        self.value = value
        self.x = 16 + (196 * y_coordinate)
        self.y = 16 + (146 * x_coordinate)
        self.draw()
    def draw(self):
        block_rect = pygame.Rect(self.x, self.y, self.block_width, self.block_height)
        pygame.draw.rect(gameDisplay, back_color[self.value], block_rect)
        font = pygame.font.Font("freesansbold.ttf", 50)
        text = font.render(str(self.value), True, text_color[self.value])
        text_rect = text.get_rect(center=block_rect.center)
        gameDisplay.blit(text, text_rect)
def interface(array):
    for i in range(4):
        for j in range(4):
            helper = block(array[i][j], i, j)










#### ADDING EFFECT ####
def adding(value, i, j):
    helper = 1
    while helper != 12:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        og_x = 16 + (196 * j)
        og_y = 16 + (146 * i)

        x = og_x + 81 - (8.1 * (helper))
        y = og_y + 58.5 - (5.85 * (helper))
        w = 18 * helper
        h = 13 * helper
        tsize = 5 * helper

        if helper != 11:
            button_rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(gameDisplay, back_color[value], button_rect)
            font = pygame.font.Font("freesansbold.ttf", tsize)
            text = font.render(str(value), True, text_color[value])
            text_rect = text.get_rect(center=button_rect.center)
            gameDisplay.blit(text, text_rect)
        else:
            block(value, i, j)
        pygame.display.update()
        clock.tick(60)
        helper += 1










#### ONLYTEXT ####
def onlyText(msg, size, color, x, y):
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(x, y))
    gameDisplay.blit(text, text_rect)










def wonLose(statemant):
    onlyText(statemant, 90, black, 400, 250)
    sound(statemant)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        button3 = button(106, 370, 250, 50, green, bright_green, "PLAY AGAIN")
        button4 = button(440, 370, 250, 50, red, bright_red, "QUIT GAME")

        if button3.isClicked():
            game_loop()
            return
        if button4.isClicked():
            return

        pygame.display.update()
        clock.tick(15)










#### Button ####
class button():
    def __init__(self, x_coordinate, y_coordinate, width, height, button_color,button_touchcolor, text):
        self.x = x_coordinate
        self.y = y_coordinate
        self.w = width
        self.h = height
        self.bc = button_color
        self.btc = button_touchcolor
        self.text = text
        self.draw()

    def draw(self):
        button_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if self.buttonArea():
            color = self.btc
        else:
            color = self.bc
        pygame.draw.rect(gameDisplay, color, button_rect)
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render(self.text, True, white)
        text_rect = text.get_rect(center = button_rect.center)
        gameDisplay.blit(text, text_rect)

    def buttonArea(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x, self.y) , (self.w, self.h))
        return button_rect.collidepoint(mouse_pos)

    def isClicked(self):
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and self.buttonArea():
            return True
        else:
            return False










##### GAMEINTRO ####
def game_intro():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        gameDisplay.fill(back_color[4])
        onlyText("2 0 4 8", 120, text_color[4], 400, 180)
        onlyText("IMRK", 30, text_color[4], 730, 565)

        button1 = button(265, 310, 280, 50, back_color[64], back_color[16], "PLAY GAME")
        button2 = button(265, 390, 280, 50, "#654321", "#8B7355", "QUIT")

        if button1.isClicked():
            game_loop()
            return
        if button2.isClicked():
            return

        pygame.display.update()
        clock.tick(15)










#### GAMELOOP ####
def game_loop():

    ans = logic.operator("start")
    flag = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ans = logic.operator("left")
                    flag = True
                elif event.key == pygame.K_UP:
                    ans = logic.operator("up")
                    flag = True
                elif event.key == pygame.K_RIGHT:
                    ans = logic.operator("right")
                    flag = True
                elif event.key == pygame.K_DOWN:
                    ans = logic.operator("down")
                    flag = True

        gameDisplay.fill(background)
        interface(ans[0])
        if flag:
            if ans[1]:
                helper = logic.add()
                adding(helper[0], helper[1], helper[2])
                if ans[2]:
                    sound("comp")
                else:
                    sound("notcomp")
            flag = False
        if ans[3]:
            wonLose("YOU WON!!")
            return
        if not ans[4]:
            wonLose("YOU LOSE!!")
            return


        pygame.display.update()
        clock.tick(15)











game_intro()
pygame.quit()