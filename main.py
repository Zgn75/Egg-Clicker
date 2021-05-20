import pygame, sys, time
from pygame.locals import *
from millify import millify,prettify

pygame.mixer.init()
pygame.init()
music = open("music.txt", "r+")
pygame.mixer.music.load("soundtrack.wav")
x = int(music.read())
WHITE = 255,255,255
font = pygame.font.SysFont(None, 44)
cpsecond = open("clickpersecond.txt", "r+")
cps = int(cpsecond.read())
baltotal = open("totalbal.txt", "r+")
totalbal = int(baltotal.read())
totalbalM = prettify(totalbal, '.')
clock = pygame.time.Clock()
w = 800
h = 600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Tap Simulator')
Loop = True
background = pygame.image.load("Background.jpg")
egg = pygame.image.load("egg.png")
resized_egg = pygame.transform.scale(egg, (282, 352))
text = font.render(f'Your total clicks are {totalbalM}', True, WHITE)
pygame.mixer.music.play(-1,0.0)
volume = pygame.image.load("volume.png")
mute = pygame.image.load("mute.png")
resized_volume = pygame.transform.scale(volume, (100, 100))
resized_mute = pygame.transform.scale(mute, (100,100))
icon = pygame.image.load("ico.ico")
pygame.display.set_icon(icon)
while Loop: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            Loop = False


        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # 1 == lefta
                egg_rect = resized_egg.get_rect(topleft = (260,150))
                vol_rect = volume.get_rect(topleft = (700,500))
                if vol_rect.collidepoint(event.pos):
                    x += 1
                    if x > 2:
                        x = 1
                if egg_rect.collidepoint(event.pos):
                    totalbal += cps
                    totalbalM = prettify(totalbal, '.')
                    text = font.render(f'Your total clicks are {totalbalM}', True, WHITE)
                    print("Your total clicks are", totalbalM, end="\r")



    #print(pygame.mouse.get_pos()) #to get mouse pos
    screen.blit(background, (0,0))
    screen.blit(resized_volume, (700,500))
    if x == 0:
        screen.blit(background, (0,0))# [...] draw something different
    elif x == 1:
        pygame.mixer.music.unpause()
        screen.blit(resized_volume, (700,500))
    elif x == 2:
        pygame.mixer.music.pause()
        screen.blit(background, (0,0))
        screen.blit(resized_mute,(700,500))
    screen.blit(text, (235,557))    
    screen.blit(resized_egg, (260,150))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)

with open("totalbal.txt", "w") as baltotal:
    baltotal.write(str(totalbal))
baltotal.close

with open("music.txt", "w") as music:
    music.write(str(x))
music.close
pygame.quit()
sys.exit()