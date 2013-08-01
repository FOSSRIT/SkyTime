#!/usr/bin/env python

import pygame
from pygame.locals import K_1, K_2, K_3, K_ESCAPE, K_RETURN,\
    K_LSHIFT, K_RSHIFT, K_BACKSPACE, QUIT, KEYDOWN
from random import randint
from pygame import transform
from badges import badges

import gettext

# Declaring Variables
hour = 12
minute = 0
time = ''
goal_time = ''
playing = False
winner = False
gameloop = True
windowSurfaceObj = None
fontObj = None
ClockCenter = None
minuteHand = []
hourHand = []
increment = 5
waited = 0
width = 1200
height = 875
mode = 'language'
prev_mode = 'language'
score = ''
score_count = 0
incorrect_count = 0

hour_style = 'default'
minute_style = 'default'
center_style = 'default'
background_style = 'default'
clock_style = 'default'
box_style = 'default'
time_box_style = 'white'

clock_render_left = width * .015
clock_render_top = height * .01

box_render_left = width * .55
time_render_left = box_render_left + (width * .185)
your_time_render_top = height * .05
goal_time_render_top = height * .285

badges = badges("SkyTime", "org.laptop.SkyTime")


# Generates a random goal time with minutes of increment distance
def set_time(distance):
    goal = str(randint(1, 12)) + ':'
    gmin = randint(0, 60) * distance
    gmin = gmin % 60
    if gmin < 10:
        goal += '0'
    goal += str(gmin)
    return goal


# Generates a random minute
def random_minute(distance):
    return (randint(0, 60) * distance) % 60


# Generates a random hour
def random_hour():
    return randint(1, 12)


def drawScreen(mode):

    # Display the actual game screens (play and challenge)
    if playing:

        # Set the background
        background = pygame.image.load(
            'images/background/{}.png'.format(background_style))
        screen = transform.scale(background, (width, height))
        windowSurfaceObj.blit(screen, (0, 0))

        # Draw the clock
        clock = pygame.image.load(
            'images/clock/clock-{}.png'.format(clock_style))
        windowSurfaceObj.blit(clock,
                             (clock_render_left, clock_render_top))

        # Display the instructional box
        instructions = pygame.image.load(
            'images/instruction/box-{}.png'.format(box_style))
        windowSurfaceObj.blit(instructions, (0, height * .685))

        # Load time box image
        time_box = pygame.image.load(
            'images/box/{}.png'.format(time_box_style))

        # If in challenge mode, only display the goal time
        if mode == 'challenge':
            # Displays your goal time
            windowSurfaceObj.blit(time_box,
                                 (box_render_left,
                                  goal_time_render_top + (height * .025)))
            windowSurfaceObj.blit(fontObj.render(
                goal_time, False, pygame.Color(0, 0, 0)),
                (time_render_left, goal_time_render_top + (height * .09)))
            windowSurfaceObj.blit(fontObj.render(
                _('Goal Time'), False, pygame.Color(0, 0, 0)),
                (box_render_left, goal_time_render_top))

        # Otherwise, display your current time and goal time
        else:

            # Displays your time
            windowSurfaceObj.blit(time_box,
                                 (box_render_left,
                                  your_time_render_top + (height * .025)))
            windowSurfaceObj.blit(fontObj.render(
                time, False, pygame.Color(0, 0, 0)),
                (time_render_left,
                 your_time_render_top + (height * .09)))
            windowSurfaceObj.blit(fontObj.render(
                _('Your Time'), False, pygame.Color(0, 0, 0)),
                (box_render_left, your_time_render_top))

            # Displays your goal time
            windowSurfaceObj.blit(time_box,
                                 (box_render_left,
                                  goal_time_render_top + (height * .025)))
            windowSurfaceObj.blit(fontObj.render(
                goal_time, False, pygame.Color(0, 0, 0)),
                (time_render_left, goal_time_render_top + (height * .09)))
            windowSurfaceObj.blit(fontObj.render(
                _('Goal Time'), False, pygame.Color(0, 0, 0)),
                (box_render_left, goal_time_render_top))

        # Displays the players score
        windowSurfaceObj.blit(fontObj.render(
            score, False, pygame.Color(0, 0, 0)),
            (width * .69, height * .56))

        # Displays help text
        text = challengeText.render(
            _('When you think the clock is correct, press'),
            False, pygame.Color(255, 255, 255))
        fw, fh = text.get_size()
        windowSurfaceObj.blit(text, (width * .44 - (fw / 2), height * .76))

        # Display help text at the bottom of the screen
        render_top = height * .895
        text = infoText.render(_('Hour Hand'), False, pygame.Color(0, 255, 0))
        text2 = infoText.render(
            _('= press'), False, pygame.Color(255, 255, 255))
        fw, fh = text.get_size()
        fw2, fh2 = text.get_size()
        windowSurfaceObj.blit(text, (width * .30 - ((fw + fw2) / 2),
                                     render_top))
        windowSurfaceObj.blit(text2, (width * .31 + (fw / 2) - (fw2 / 2),
                                      render_top))
        text = infoText.render(_('Minute Hand'), False,
                               pygame.Color(255, 0, 0))
        text2 = infoText.render(
            _('= press'), False, pygame.Color(255, 255, 255))
        fw, fh = text.get_size()
        fw2, fh2 = text2.get_size()
        windowSurfaceObj.blit(text, (width * .75 - ((fw + fw2) / 2),
                              render_top))
        windowSurfaceObj.blit(text2, (width * .76 + (fw / 2) - (fw2 / 2),
                              render_top))

        # Display the enter button text
        text = enterButton.render(_('enter'), False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        windowSurfaceObj.blit(text, (width * .885 - (fw / 2), height * .79))

        # Display the shift button text
        text = shiftButton.render(_('shift'), False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        render_top = height * .9
        windowSurfaceObj.blit(text, (width * .445 - (fw / 2), render_top))
        windowSurfaceObj.blit(text, (width * .9375 - (fw / 2), render_top))

        # Draw the clock hands
        drawHands()

    # Draw the menu screen
    elif mode == 'menu':
        render_left = width * .27
        interval = .18
        spacer = .33

        screen = transform.scale(MenuScreen, (width, height))
        windowSurfaceObj.blit(screen, (0, 0))
        for i in range(0, 3):
            text = menuText.render(_('Press'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            windowSurfaceObj.blit(text,
                                 (render_left - (fw / 2), height * spacer))
            spacer += interval

        render_left = width * .48
        spacer = .33
        windowSurfaceObj.blit(menuText.render(
            _('Play'), False, pygame.Color(0, 0, 0)),
            (render_left, height * spacer))
        windowSurfaceObj.blit(menuText.render(
            _('Challenge'), False, pygame.Color(0, 0, 0)),
            (render_left, height * (spacer + interval)))
        windowSurfaceObj.blit(menuText.render(
            _('How To Play'), False, pygame.Color(0, 0, 0)),
            (render_left, height * (spacer + (interval * 2))))

    # Draw the vicotry screen
    elif mode == 'victory':
        windowSurfaceObj.blit(victory, (0, 0))

    # Draw the language selection screen
    elif mode == 'language':
        screen = transform.scale(Languages, (width, height))
        windowSurfaceObj.blit(screen, (0, 0))

    # Draw the how to play screen
    else:
        screen = transform.scale(HowToScreen, (width, height))
        windowSurfaceObj.blit(screen, (0, 0))

        text = howToPlay.render(_('How To Play'),
                                False, pygame.Color(255, 255, 0))
        fw, fh = text.get_size()
        windowSurfaceObj.blit(text, ((width * .52) - (fw / 2), height * .05))

        text = fontObj.render(_('When you think it is correct, press'),
                              False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        windowSurfaceObj.blit(text, (width * .42 - (fw / 2), height * .89))

        text = helpText.render(_('Press this key'),
                               False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        render_left = width * .22 - (fw / 2)
        render_top = height * .63
        windowSurfaceObj.blit(text, (render_left, render_top))

        windowSurfaceObj.blit(helpText.render(
            _('to move the'), False,
            pygame.Color(0, 0, 0)),
            (render_left, render_top + fh))
        windowSurfaceObj.blit(helpText.render(
            _('hour hand'), False,
            pygame.Color(0, 0, 0)),
            (render_left, render_top + (fh * 2)))

        text = helpText.render(_('Press this key'),
                               False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        render_left = width * .78 - (fw / 2)
        windowSurfaceObj.blit(text, (render_left, render_top))

        windowSurfaceObj.blit(helpText.render(
            _('to move the'), False,
            pygame.Color(0, 0, 0)),
            (render_left, render_top + fh))
        windowSurfaceObj.blit(helpText.render(
            _('minute hand'), False,
            pygame.Color(0, 0, 0)),
            (render_left, render_top + (fh * 2)))

        text = enterButton.render(_('enter'), False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        windowSurfaceObj.blit(text, (width * .78 - (fw / 2), height * .915))

        text = shiftButton.render(_('shift'), False, pygame.Color(0, 0, 0))
        fw, fh = text.get_size()
        render_top = height * .43

        windowSurfaceObj.blit(text, (width * .205 - (fw / 2), render_top))
        windowSurfaceObj.blit(text, (width * .755 - (fw / 2), render_top))


def drawHands():

    # Checks the current time and draws the hands accordingly
    if minute == 0:
        windowSurfaceObj.blit(minuteHand[0],
                             (clock_render_left + (width * .23),
                              clock_render_top + (height * .13)))
    elif minute == 5:
        windowSurfaceObj.blit(minuteHand[1],
                             (clock_render_left + (width * .23),
                              clock_render_top + (height * .145)))
    elif minute == 10:
        windowSurfaceObj.blit(minuteHand[2],
                             (clock_render_left + (width * .23),
                              clock_render_top + (height * .215)))
    elif minute == 15:
        windowSurfaceObj.blit(minuteHand[3],
                             (clock_render_left + (width * .25),
                              clock_render_top + (height * .31)))
    elif minute == 20:
        windowSurfaceObj.blit(minuteHand[4],
                             (clock_render_left + (width * .2425),
                              clock_render_top + (height * .31)))
    elif minute == 25:
        windowSurfaceObj.blit(minuteHand[5],
                             (clock_render_left + (width * .225),
                              clock_render_top + (height * .305)))
    elif minute == 30:
        windowSurfaceObj.blit(minuteHand[6],
                             (clock_render_left + (width * .23),
                              clock_render_top + (height * .33)))
    elif minute == 35:
        windowSurfaceObj.blit(minuteHand[7],
                             (clock_render_left + (width * .162),
                              clock_render_top + (height * .32)))
    elif minute == 40:
        windowSurfaceObj.blit(minuteHand[8],
                             (clock_render_left + (width * .12),
                              clock_render_top + (height * .3)))
    elif minute == 45:
        windowSurfaceObj.blit(minuteHand[9],
                             (clock_render_left + (width * .105),
                              clock_render_top + (height * .315)))
    elif minute == 50:
        windowSurfaceObj.blit(minuteHand[10],
                             (clock_render_left + (width * .12),
                              clock_render_top + (height * .215)))
    elif minute == 55:
        windowSurfaceObj.blit(minuteHand[11],
                              (clock_render_left + (width * .16),
                               clock_render_top + (height * .15)))

    if hour == 0:
        windowSurfaceObj.blit(hourHand[0],
                             (clock_render_left + (width * .2325),
                              clock_render_top + (height * .19)))
    elif hour == 1:
        windowSurfaceObj.blit(hourHand[1],
                             (clock_render_left + (width * .24),
                              clock_render_top + (height * .2)))
    elif hour == 2:
        windowSurfaceObj.blit(hourHand[2],
                             (clock_render_left + (width * .245),
                              clock_render_top + (height * .25)))
    elif hour == 3:
        windowSurfaceObj.blit(hourHand[3],
                             (clock_render_left + (width * .26),
                              clock_render_top + (height * .3135)))
    elif hour == 4:
        windowSurfaceObj.blit(hourHand[4],
                             (clock_render_left + (width * .245),
                              clock_render_top + (height * .325)))
    elif hour == 5:
        windowSurfaceObj.blit(hourHand[5],
                              (clock_render_left + (width * .235),
                               clock_render_top + (height * .325)))
    elif hour == 6:
        windowSurfaceObj.blit(hourHand[6],
                             (clock_render_left + (width * .23),
                              clock_render_top + (height * .34)))
    elif hour == 7:
        windowSurfaceObj.blit(hourHand[7],
                             (clock_render_left + (width * .185),
                              clock_render_top + (height * .33)))
    elif hour == 8:
        windowSurfaceObj.blit(hourHand[8],
                             (clock_render_left + (width * .145),
                              clock_render_top + (height * .31)))
    elif hour == 9:
        windowSurfaceObj.blit(hourHand[9],
                             (clock_render_left + (width * .145),
                              clock_render_top + (height * .31)))
    elif hour == 10:
        windowSurfaceObj.blit(hourHand[10],
                             (clock_render_left + (width * .15),
                              clock_render_top + (height * .235)))
    elif hour == 11:
        windowSurfaceObj.blit(hourHand[11],
                             (clock_render_left + (width * .18),
                              clock_render_top + (height * .2)))

    screen = transform.scale(ClockCenter, (width/22, height/18))
    windowSurfaceObj.blit(screen,
                         (clock_render_left + (width * .2275),
                          clock_render_top + (height * .31)))
                         #(width * .24, height * .3))

    return(0)


def loadMinuteHands():
    # Loads in the minute hand and creates an array with all of the angles
    minutes = [pygame.image.load('images/hand/minute-{}.png'.format(
        minute_style))]
    for angle in angles:
        minutes.append(pygame.transform.rotate(minutes[0], angle))

    return minutes


def loadHourHands():
    # Loads in the hour hand and creates an array with all the angles
    hours = [pygame.image.load('images/hand/hour-{}.png'.format(
        hour_style))]
    for angle in angles:
        hours.append(pygame.transform.rotate(hours[0], angle))

    return hours


# Generates a new random time
hour = random_hour()
minute = random_minute(increment)

time = str(hour) + ':'
if minute < 10:
    time += '0'
time += str(minute)
goal_time = set_time(increment)

if hour == 12:
    hour = 0

# Initializes pygame and the screen Surface object
pygame.init()
windowSurfaceObj = pygame.display.set_mode(
    (width, height))

# The angles for the clock hands
angles = [-30, -60, -90, -120, -150, -180,
          -210, -240, -270, -300, -330]

# Loads all of the assets
MenuScreen = pygame.image.load('images/MenuScreen.gif')
HowToScreen = pygame.image.load('images/HowToScreen.gif')
ClockCenter = pygame.image.load('images/clock/center-{}.png'.format(
    center_style))
Languages = pygame.image.load('images/language.gif')
victory = pygame.image.load('images/Sun.gif')
fontObj = pygame.font.Font('freesansbold.ttf', 32)
menuText = pygame.font.Font('freesansbold.ttf', 52)
infoText = pygame.font.Font('freesansbold.ttf', 28)
helpText = pygame.font.Font('freesansbold.ttf', 28)
challengeText = pygame.font.Font('freesansbold.ttf', 42)
howToPlay = pygame.font.Font('freesansbold.ttf', 65)
enterButton = pygame.font.Font('freesansbold.ttf', 20)
shiftButton = pygame.font.Font('freesansbold.ttf', 16)

# Loop the game until the player quits
while gameloop:

    drawScreen(mode)
    score = str(score_count)

    # Checks if the player won the challenge
    if time == goal_time and winner:
        waited += 1

        if waited > 100:

            # Generates a new random time
            hour = random_hour()
            minute = random_minute(increment)

            time = str(hour) + ':'
            if minute < 10:
                time += '0'
            time += str(minute)
            goal_time = set_time(increment)

            if hour == 12:
                hour = 0

            waited = 0
            incorrect_count = 0
            winner = False
            playing = True

            if prev_mode == 'play':
                mode = 'play'
            else:
                mode = 'challenge'

    # Check if the player wants to quit the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Check for input and draw information
        elif event.type == KEYDOWN and winner is False:

            # Check what language the player has selected
            if mode == 'language':
                if event.key == K_1:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeEnglish'])
                    _ = lang.ugettext
                    mode = 'menu'

                elif event.key == K_2:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeSpanish'])
                    _ = lang.ugettext
                    mode = 'menu'

                elif event.key == K_3:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeFrench'])
                    _ = lang.ugettext
                    infoText = pygame.font.Font('freesansbold.ttf', 22)
                    challengeText = pygame.font.Font('freesansbold.ttf', 34)
                    mode = 'menu'

            # Check what mode the player has selected
            elif mode == 'menu':
                # Draw the play screen
                if event.key == K_1:
                    mode = 'play'
                    minuteHand = loadMinuteHands()
                    hourHand = loadHourHands()
                    playing = True

                # Draw the challenge screen
                elif event.key == K_2:
                    mode = 'challenge'
                    minuteHand = loadMinuteHands()
                    hourHand = loadHourHands()
                    playing = True

                # Draw How To Play
                elif event.key == K_3:
                    mode = 'howtoplay'
                    playing = False

                # Go back to language select
                elif event.key == K_BACKSPACE:
                    mode = 'language'
                    playing = False

            # Go back to the menu
            elif event.key == K_BACKSPACE:
                mode = 'menu'
                playing = False

            # Increments the hour by 1
            if event.key == K_LSHIFT:
                hour += 1
                if hour > 11:
                    hour = 0
                    time = '12:'
                else:
                    time = str(hour) + ':'
                if minute < 10:
                    time += '0'

                time += str(minute)

            # Increments the minutes by 5
            if event.key == K_RSHIFT:
                minute += increment
                if hour == 0:
                    time = '12:'
                else:
                    time = str(hour) + ':'
                if minute == 60:
                    minute = 0
                if minute < 10:
                    time += '0'

                time += str(minute)

            # Check if the player has the correct time
            if event.key == K_RETURN:
                if time == goal_time and playing:
                    prev_mode = mode
                    playing = False
                    winner = True
                    score_count += 1

                    # Award badges
                    if score_count == 1:
                        badges.award('Hair Past a Freckle',
                                     'Completed your first time')
                        if mode == 'challenge':
                            badges.award('Challenge Complete',
                                         'Completed your first challenge time')
                    if score_count == 5:
                        badges.award('First Five',
                                     'Obtained your first five suns')
                    if score_count == 100:
                        badges.award('ChronoKeeper',
                                     'Obtained 100 suns')

                    mode = 'victory'

                elif playing:
                    if incorrect_count == 3:
                        badges.award('Rainy Day',
                                     'Answered incorrectly 3 times in a row')
                    incorrect_count += 1

            # Quit the game
            if event.key == K_ESCAPE:
                gameloop = False

    if gameloop:
        pygame.display.update()
