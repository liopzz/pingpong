from pygame import *
import random 
from button import Button
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,x=0,y=0,width =65,height=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y >5:
            self.rect.y -=8
        if keys[K_s] and self.rect.y<510:
            self.rect.y +=8
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y >5:
            self.rect.y -=8
        if keys[K_DOWN] and self.rect.y<510:
            self.rect.y +=8


window = display.set_mode((800,600))

display.set_caption('ping_pong')
background = transform.scale(image.load('bg.png'),(800,600))
player1 = Player('platformm.png',0,210,30,90)
player2 = Player2('platformm.png',770,210,30,90)
ball = GameSprite('balls.png',200,200,50,50)








clock = time.Clock()
FPS = 60

speed_x = 6
speed_y = 6
finish =False
run = True
font.init()
font = font.Font('EightBits.ttf', 35)
btn_start = Button(y=150,width=150,height = 40,text = 'начать игру',font_size=24)
btn_credits = Button(y=210,width=150,height = 40,text = 'Об авторе',font_size=24)
btn_restart = Button(y=220,width=150,height = 40,text = 'Перезапуск',font_size=24)
btn_exit = Button(y=270,width=150,height = 40,text = 'Выход',font_size=24)
btn_continue =Button(y=220,width=150,height = 40,text = 'продолжить',font_size=24)
btn_exit_in_pause = Button(y=280,width=150,height = 40,text = 'Выход',font_size=24)



lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
def game_run():
    global speed_x,speed_y,stage
    window.blit(background,(0,0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
  
    
    if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y >550 or ball.rect.y <0:
        speed_y *= -1
    if ball.rect.x <0:
        stage = 'lose1'
        finish= True
        window.blit(lose1,(300,250))
        game_over = True
    if ball.rect.x > 800:
        stage = 'lose2'
        finish = True
        window.blit(lose2,(300,250))
    display.update()
    clock.tick(FPS)
def menu(events):
    window.blit(background,(0,0))
    btn_start.update(events)
    btn_exit.update(events)
    btn_credits.update(events)
    btn_start.draw(window)
    btn_exit.draw(window)
    btn_credits.draw(window)

    global stage
    if btn_start.is_clicked(events):
        stage = 'game'
    if btn_exit.is_clicked(events):
        stage = 'off'

def pause(events):
    window.blit(background,(0,0))
    btn_continue.update(events)
    btn_exit_in_pause.update(events)
    btn_continue.draw(window)
    btn_exit_in_pause.draw(window)
    global stage
    if btn_continue.is_clicked(events):
        stage = 'game'
    if btn_exit_in_pause.is_clicked(events):
        stage = 'menu'
def restart_game():
    global background,player1,player2,ball
    display.set_caption('ping_pong')
    background = transform.scale(image.load('bg.png'),(800,600))
    player1 = Player('platformm.png',0,210,30,90)
    player2 = Player2('platformm.png',770,210,30,90)
    ball = GameSprite('balls.png',200,200,50,50)

def end_game(events):
    global stage
    btn_restart.update(events)
    btn_exit_in_pause.update(events)
    btn_restart.draw(window)
    btn_exit_in_pause.draw(window)
    if btn_restart.is_clicked(events):
        restart_game()
        stage = 'game'
    if btn_exit_in_pause.is_clicked(events):
        stage = 'menu'
        restart_game()

stage = 'menu'
while stage != 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'


    if stage == 'menu':
        menu(events)
    if stage == 'game':
        game_run()
    if stage == 'pause':
        pause(events)
    if 'lose' in stage:
        end_game(events)

    
    display.update()
    clock.tick(FPS)