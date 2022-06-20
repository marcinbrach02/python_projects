import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('MS Comic Sans', 30)

# inicjalizacja
window_width, window_height = 800, 500
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("HardCoder Game")

# definicje kolorów
RED, GREEN, BLUE, WHITE = (255,0,0),  (0,255,0), (0,0,255), (255,255,255)

# obiekt gracza
player_width, player_height = 200, 200
player = pygame.Rect(window_width/2-player_width/2,window_height-player_height,player_width,player_height)
meat_width, meat_height = 100, 100
balls = []

points = 56 #licznik

# muzyka w tle
pygame.mixer.music.load("mario.mid")
pygame.mixer.music.play(-1, 0.0)
# efekty dźwiękowe
action_sound = pygame.mixer.Sound("item.wav")

# wczytane grafiki
player_img = pygame.image.load("corgi.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
meat_img = pygame.image.load("meat.png")
meat_img = pygame.transform.scale(meat_img, (meat_width, meat_height))
background_img = pygame.image.load("idylla.png")
background_img = pygame.transform.scale(background_img, (window_width, window_height))

# pętla główna gry
velocity = 20
while True:
    window.blit(background_img, (0, 0)) # obraz tła
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.left > 0:
            player.left -= velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.right < window_width:
            player.right += velocity
    if keys[pygame.K_SPACE]:
        new_ball=pygame.Rect(random.randint(0,window_width),0,meat_width,meat_height)
        balls.append(new_ball)

    #pygame.draw.rect(window, RED, player)
    window.blit(player_img, player)

    for ball in balls[:]:
        ball.bottom += 10
        if player.colliderect(ball):
            action_sound.play()
            points += 1
            balls.remove(ball)
        elif ball.bottom >= window_height:
            points -= 1
            balls.remove(ball)
        else:
            #pygame.draw.rect(window, GREEN, ball)
            window.blit(meat_img, ball)

    # licznik punktów
    points_text = myfont.render('POINTS: '+str(points), False, WHITE)
    window.blit(points_text,(window_width*0.1,window_height-100))

    pygame.display.update()
    clock.tick(10)