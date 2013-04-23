import pygame, sys
from pygame.locals import *

hour = 12;
minute = 0;
time = '12:00'

#--initiate the program / make the surface
pygame.init()
windowSurfaceObj = pygame.display.set_mode((1200, 900))

#Load Assets
background = pygame.image.load('BackgroundClockPage.jpg')
menuBackground = pygame.image.load('uiBackground.jpg')

minuteHand = pygame.image.load('MinuteHand.png')
hourHand = pygame.image.load('HourHand.png')
handCover = pygame.image.load('HandCover.png')
menuButton = pygame.image.load('UiButton.png')
menuButton2 = pygame.image.load('UiButton.png')

fontObj = pygame.font.Font('freesansbold.ttf', 32)



while True:
#----Menu-------------
    windowSurfaceObj.blit(background, (0, 0))
    windowSurfaceObj.blit(minuteHand, (280, 350))
    windowSurfaceObj.blit(hourHand, (290, 375))
    windowSurfaceObj.blit(handCover, (289, 425))
    windowSurfaceObj.blit(fontObj.render(time,False, pygame.Color(0, 0, 0)), (800, 325))
    
    windowSurfaceObj.blit(menuBackground, (0, 0))
    windowSurfaceObj.blit(menuButton, (400, 300))
    windowSurfaceObj.blit(menuButton2, (400, 400))

#---Main Game Loop----
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                menuBackground.set_alpha(0)
                menuButton.set_alpha(0)
                menuButton2.set_alpha(0)
            if event.key == K_UP: # - increments hours by 1 
                hour += 1;
                if hour > 12:
                    hour = 1
                time = str(hour) + ':'
                if minute < 10:
                    time += '0'
                time += str(minute)
            if event.key == K_DOWN: # - increments minutes by 5
                minute += 5;
                if minute == 60:
                    minute = 0
                time = str(hour) + ':'
                if minute < 10:
                    time += '0'
                time += str(minute)
            if event.key == K_ESCAPE: # - Quit app
                pygame.quit()
                sys.exit()

    pygame.display.update()
