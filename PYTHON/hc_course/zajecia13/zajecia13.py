# PyGame - prosty projakt gry
import pygame, random
from pygame.locals import *
pygame.init()
window_width = 800
window_height = 600
velocity = 20
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont("MS Comic Sans", 30)

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Hardcoder Game")
# pygame.display.set_icon("corgi_icon.png")

RED, GREEN, BLUE, WHITE = (255,0,0), (0,255,0), (0,0,255), (255,255,255)
player_width = 150
player_height = 150
meat_width = 100
meat_height = 100
player = pygame.Rect(window_width/2,window_height - player_height, player_width, player_height)
balls = []
points = 0
pygame.mixer.music.load("mario.mid")
pygame.mixer.music.play(-1, 0.0)
action_sound = pygame.mixer.Sound("item.wav")

player_img = pygame.image.load("corgi.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
meat_img = pygame.image.load("meat.png")
meat_img = pygame.transform.scale(meat_img, (meat_width, meat_height))
background_img = pygame.image.load("idylla.png")
background_img = pygame.transform.scale(background_img, (window_width, window_height))

while True:
    # window.fill((0,0,0))
    window.blit(background_img, (0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.left > 0:
            player.left -= velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.right < window_width:
            player.right += velocity
    if keys[pygame.K_SPACE]:
        new_ball = pygame.Rect( random.randint(0,window_width), 0, meat_width, meat_height)
        balls.append(new_ball)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    for ball in balls[:]:
        ball.bottom += 10
        if player.colliderect(ball):
            points += 1
            balls.remove(ball)
            action_sound.play()
        elif ball.bottom >= window_height:
            points -= 1
            balls.remove(ball)
        else:
            window.blit(meat_img, ball)


    window.blit(player_img, player)
    points_text = myfont.render("POINTS: " + str(points), False, WHITE)
    window.blit(points_text, (window_width*0.1, window_height-100))
    pygame.display.update()
    clock.tick(10)
