import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 80)
window = pygame.display.set_mode( (800,200) )

pygame.mixer.music.load("music.mid")
pygame.mixer.music.play(-1, 0.0)

question = "]#mdnlhm#wr#ju|B#=0,"
question = "".join([chr(ord(i)-3) for i in question])

while True:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()

    text = myfont.render(question,False,(255,255,255))
    window.blit(text,( 10, 10))
    pygame.display.update()
