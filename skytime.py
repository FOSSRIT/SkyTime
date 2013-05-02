import pygame, sys
from pygame.locals import *
from random import randint

#Generates a random goal time with minutes of increment distance
def set_time (distance):
	goal = str(randint(1,12)) + ':'
	gmin = randint(0, 60) * distance
	gmin = gmin % 60
	if gmin < 10:
		goal += '0'
	goal += str(gmin)
	return goal


time_keeper = pygame.time.Clock()
fps = 30

hour = 0;
minute = 0;
time = '12:00'
increment = 5

delay = 2 #How long the victory sun stays up
waited = 0 #How many frames the victory sun has been up
goal_time = '12:00'
challenge = False

#--initiate the program / make the surface
pygame.init()
windowSurfaceObj = pygame.display.set_mode((1200, 900))

#--Load Assests -------- (menus/images/fonts/etc)
MenuScreen = pygame.image.load('MenuScreen.gif')
PlayScreen = pygame.image.load('PlayScreen.gif')
HowToScreen = pygame.image.load('HowToScreen.gif')
ChallengeScreen = pygame.image.load('ChallengeScreen.gif')
ClockCenter = pygame.image.load('ClockCenter.png')
victory = pygame.image.load('Sun.gif')
fontObj = pygame.font.Font('freesansbold.ttf', 32)
#^^^^^^^^^^^^^^Load Assets^^^^^^^^^^^^^^^^^^^^

#--------Hand Rotation-------------------
angles =  [-30, -60, -90, -120, -150, -180, -210, -240, -270, -300, -330]#angles for clock hands

minuteHand = [pygame.image.load('MinHand.png')]
for angle in angles:
	minuteHand.append(pygame.transform.rotate(minuteHand[0], angle))

hourHand = [pygame.image.load('HourHand.png')]
for angle in angles:
	hourHand.append(pygame.transform.rotate(hourHand[0], angle))
#^^^^^^^^^^^^^Hand Rotation^^^^^^^^^^^^^^^




while True:
	windowSurfaceObj.blit(ChallengeScreen, (0, 0))
	windowSurfaceObj.blit(PlayScreen, (0, 0))
	windowSurfaceObj.blit(fontObj.render(time,False, pygame.Color(0, 0, 0)), (800, 325))
	if challenge:
		windowSurfaceObj.blit(fontObj.render(goal_time,False, pygame.Color(0, 0, 0)), (800, 525))

	if time == goal_time and challenge:
		waited += 1
		windowSurfaceObj.blit(victory, (0,0))
		if waited % (delay * fps) == 0:
			minute = 0
			hour = 0
			time = '12:00'
			goal_time = set_time(increment)
	else: 
		if minute == 0:
			windowSurfaceObj.blit(minuteHand[0], (288, 271))
		elif minute == 5:
			windowSurfaceObj.blit(minuteHand[1], (290, 290))
		elif minute == 10:
			windowSurfaceObj.blit(minuteHand[2], (300, 340))
		elif minute == 15:
			windowSurfaceObj.blit(minuteHand[3], (311, 430))
		elif minute == 20:
			windowSurfaceObj.blit(minuteHand[4], (295, 435))
		elif minute == 25:
			windowSurfaceObj.blit(minuteHand[5], (295, 445))
		elif minute == 30:
			windowSurfaceObj.blit(minuteHand[6], (288, 454))
		elif minute == 35:
			windowSurfaceObj.blit(minuteHand[7], (200, 445))
		elif minute == 40:
			windowSurfaceObj.blit(minuteHand[8], (145, 435))
		elif minute == 45:
			windowSurfaceObj.blit(minuteHand[9], (128, 430))
		elif minute == 50:
			windowSurfaceObj.blit(minuteHand[10], (145, 340))
		elif minute == 55:
			windowSurfaceObj.blit(minuteHand[11], (205, 290))

		if hour == 0:
			windowSurfaceObj.blit(hourHand[0], (288, 338))
		elif hour == 1:
			windowSurfaceObj.blit(hourHand[1], (293, 344))
		elif hour == 2:
			windowSurfaceObj.blit(hourHand[2], (308, 376))
		elif hour == 3:
			windowSurfaceObj.blit(hourHand[3], (311, 430))
		elif hour == 4:
			windowSurfaceObj.blit(hourHand[4], (293, 436))
		elif hour == 5:
			windowSurfaceObj.blit(hourHand[5], (293, 444))
		elif hour == 6:
			windowSurfaceObj.blit(hourHand[6], (288, 454))
		elif hour == 7:
			windowSurfaceObj.blit(hourHand[7], (233, 444))
		elif hour == 8:
			windowSurfaceObj.blit(hourHand[8], (200, 434))
		elif hour == 9:
			windowSurfaceObj.blit(hourHand[9], (195, 430))
		elif hour == 10:
			windowSurfaceObj.blit(hourHand[10], (205, 375))
		elif hour == 11:
			windowSurfaceObj.blit(hourHand[11], (235, 344))


		windowSurfaceObj.blit(ClockCenter, (281, 424))
		windowSurfaceObj.blit(HowToScreen, (0, 0))
		windowSurfaceObj.blit(MenuScreen, (0, 0))
		
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_1:#Go to PlayScreen (make all other screens invisible)
				MenuScreen.set_alpha(0)
				ChallengeScreen.set_alpha(0)
				HowToScreen.set_alpha(0)
				PlayScreen.set_alpha(300)
				challenge = False
			if event.key == K_2:#Go to ChallengeScreen (make all other screens invisible)
				MenuScreen.set_alpha(0)
				PlayScreen.set_alpha(0)
				HowToScreen.set_alpha(0)
				ChallengeScreen.set_alpha(300)
				challenge = True
			if event.key == K_3:#Go to How To Play (make all other screens invisible)
				MenuScreen.set_alpha(0)
				ChallengeScreen.set_alpha(0)
				PlayScreen.set_alpha(0)
				HowToScreen.set_alpha(300)
				challenge = False
			if event.key == K_BACKSPACE:#Go Back To Menu (make all other screens invisible)
				PlayScreen.set_alpha(0)
				ChallengeScreen.set_alpha(0)
				HowToScreen.set_alpha(0)
				MenuScreen.set_alpha(300)
				challenge = False

			# - increments hours by 1 
			if event.key == K_LSHIFT and (time != goal_time or not challenge):
				hour += 1;
				if hour == 12:
					hour = 0
					time = '12:'
				else:
					time = str(hour) + ':'
				if minute < 10:
					time += '0'
				time += str(minute)

			# - increments minutes by increment
			if event.key == K_RSHIFT and (time != goal_time or not challenge): 
				minute += increment;
				if hour == 0:
					time = '12:'
				else:
					time = str(hour) + ':'
				if minute == 60:
					minute = 0
				if minute < 10:
					time += '0'
				time += str(minute)
			if event.key == K_ESCAPE: # - Quit app
				pygame.quit()
				sys.exit()

	pygame.display.update()
	time_keeper.tick(fps)
