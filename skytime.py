import pygame, sys
from pygame.locals import *

hour = 12;
minute = 0;
time = '12:00'

pygame.init()
windowSurfaceObj = pygame.display.set_mode((1200, 900))

background = pygame.image.load('BackgroundClockPage.jpg')

minuteHand = pygame.image.load('MinuteHand.png')
hourHand = pygame.image.load('HourHand.png')
handCover = pygame.image.load('HandCover.png')

fontObj = pygame.font.Font('freesansbold.ttf', 32)

while True:
    # windowSurfaceObj.fill(pygame.Color(255, 255, 255))
    windowSurfaceObj.blit(background, (0, 0))

    windowSurfaceObj.blit(minuteHand, (280, 350))
    #windowSurfaceObj.blit(hourHand, (290, 375))

    rotated_hourHand = pygame.transform.rotate(hourHand, 30)# - This is how we rotate images

    windowSurfaceObj.blit(rotated_hourHand, (290, 375))
    
    windowSurfaceObj.blit(handCover, (289, 425))
    windowSurfaceObj.blit(fontObj.render(time,False, pygame.Color(0, 0, 0)), (800, 325))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
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
        
