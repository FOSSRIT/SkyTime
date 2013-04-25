import pygame, sys
from pygame.locals import *

hour = 12;
minute = 0;
time = '12:00'

goal_time = '4:20'

#--initiate the program / make the surface
pygame.init()
windowSurfaceObj = pygame.display.set_mode((1200, 900))

#Load Assets
background = pygame.image.load('BackgroundClockPage.jpg')
menuBackground = pygame.image.load('uiBackground.jpg')
victory = pygame.image.load('sun.gif')

minuteHand = [pygame.image.load('MinuteHand.png')]
minuteHand.append(pygame.transform.rotate(minuteHand[0], -30))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -60))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -90))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -120))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -150))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -180))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -210))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -240))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -270))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -300))
minuteHand.append(pygame.transform.rotate(minuteHand[0], -330))

hourHand_12 = pygame.image.load('HourHand.png')
hourHand_01 = pygame.transform.rotate(hourHand_12, -30)
hourHand_02 = pygame.transform.rotate(hourHand_12, -60) 
hourHand_03 = pygame.transform.rotate(hourHand_12, -90)
hourHand_04 = pygame.transform.rotate(hourHand_12, -120)
hourHand_05 = pygame.transform.rotate(hourHand_12, -150)
hourHand_06 = pygame.transform.rotate(hourHand_12, -180)
hourHand_07 = pygame.transform.rotate(hourHand_12, -210)
hourHand_08 = pygame.transform.rotate(hourHand_12, -240)
hourHand_09 = pygame.transform.rotate(hourHand_12, -270)
hourHand_10 = pygame.transform.rotate(hourHand_12, -300)
hourHand_11 = pygame.transform.rotate(hourHand_12, -330)


handCover = pygame.image.load('HandCover.png')
menuButton = pygame.image.load('UiButton.png')
menuButton2 = pygame.image.load('UiButton.png')

fontObj = pygame.font.Font('freesansbold.ttf', 32)



while True:

    windowSurfaceObj.blit(background, (0, 0))
    windowSurfaceObj.blit(fontObj.render(time,False, pygame.Color(0, 0, 0)), (800, 325))
    #windowSurfaceObj.blit(handCover, (289, 425))
    #windowSurfaceObj.blit(menuBackground, (0, 0))
    #windowSurfaceObj.blit(menuButton, (400, 300))
    #windowSurfaceObj.blit(menuButton2, (400, 400))
    if time == goal_time:
        windowSurfaceObj.blit(victory, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    minute = 0
                    hour = 12
                    time = '12:00'
                if event.key == K_ESCAPE: # - Quit app
                    pygame.quit()
                    sys.exit()
    else: 

        if minute == 0:
            windowSurfaceObj.blit(minuteHand[0], (280, 350))
        elif minute == 5:
            windowSurfaceObj.blit(minuteHand[1], (280, 350))
        elif minute == 10:
            windowSurfaceObj.blit(minuteHand[2], (285, 380))
        elif minute == 15:
            windowSurfaceObj.blit(minuteHand[3], (295, 420))
        elif minute == 20:
            windowSurfaceObj.blit(minuteHand[4], (280, 420))
        elif minute == 25:
            windowSurfaceObj.blit(minuteHand[5], (270, 420))
        elif minute == 30:
            windowSurfaceObj.blit(minuteHand[6], (273, 450))
        elif minute == 35:
            windowSurfaceObj.blit(minuteHand[7], (230, 425))
        elif minute == 40:
            windowSurfaceObj.blit(minuteHand[8], (203, 420))
        elif minute == 45:
            windowSurfaceObj.blit(minuteHand[9], (208, 415))
        elif minute == 50:
            windowSurfaceObj.blit(minuteHand[10], (215, 370))
        elif minute == 55:
            windowSurfaceObj.blit(minuteHand[11], (235, 350))


        if hour == 12:
            windowSurfaceObj.blit(hourHand_12, (290, 375))
        elif hour == 1:
            windowSurfaceObj.blit(hourHand_01, (280, 375))
        elif hour == 2:
            windowSurfaceObj.blit(hourHand_02, (280, 395))
        elif hour == 3:
            windowSurfaceObj.blit(hourHand_03, (290, 430))
        elif hour == 4:
            windowSurfaceObj.blit(hourHand_04, (280, 425))
        elif hour == 5:
            windowSurfaceObj.blit(hourHand_05, (280, 425))
        elif hour == 6:
            windowSurfaceObj.blit(hourHand_06, (290, 430))
        elif hour == 7:
            windowSurfaceObj.blit(hourHand_07, (248, 425))
        elif hour == 8:
            windowSurfaceObj.blit(hourHand_08, (232, 420))
        elif hour == 9:
            windowSurfaceObj.blit(hourHand_09, (230, 430))
        elif hour == 10:
            windowSurfaceObj.blit(hourHand_10, (225, 390))
        elif hour == 11:
            windowSurfaceObj.blit(hourHand_11, (248, 372))


        windowSurfaceObj.blit(handCover, (289, 425))
        windowSurfaceObj.blit(menuBackground, (0, 0))
        windowSurfaceObj.blit(menuButton, (400, 300))
        windowSurfaceObj.blit(menuButton2, (400, 400))

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
