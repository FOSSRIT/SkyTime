#!/usr/bin/env python

from sugar.activity import activity

import pygame
import gettext
from random import randint
from pygame import transform
from badges import badges
from pygame.locals import K_1, K_2, K_3, K_ESCAPE, K_RETURN, \
    K_LSHIFT, K_RSHIFT, K_BACKSPACE, QUIT, KEYDOWN
from constants import width, height, clock_render_left, clock_render_top, \
    box_render_left, time_render_left, your_time_render_top, HANDS, \
    goal_time_render_top


class SkyTimeActivity(activity.Activity):

    # Declaring Variables
    hour = 12
    minute = 0
    time = ''
    goal_time = ''
    challenge = False
    winner = False
    gameloop = True
    update_screen = True
    update_hands = False
    windowSurfaceObj = None
    fontObj = None
    increment = 5
    waited = 0
    mode = 'language'
    playing = False
    score_count = 0
    incorrect_count = 0

    hour_style = 'default'
    minute_style = 'default'
    center_style = 'default'
    background_style = 'default'
    clock_style = 'default'
    box_style = 'default'
    time_box_style = 'white'

    # Generates a random goal time with minutes of increment distance
    def set_time(self, distance):
        goal = str(randint(1, 12)) + ':'
        gmin = randint(0, 60) * distance
        gmin = gmin % 60
        if gmin < 10:
            goal += '0'
        goal += str(gmin)
        return goal

    # Generates a random minute
    def random_minute(self, distance):
        return (randint(0, 60) * distance) % 60

    # Generates a random hour
    def random_hour(self):
        return randint(1, 12)

    def drawScreen(self, mode):

        if self.update_screen:

            #Draw the normal play screen
            if self.playing:

                # Set the background
                background = pygame.image.load(
                    'images/background/{}.png'.format(self.background_style))
                screen = transform.scale(background, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                # Display the instructional box
                instructions = pygame.image.load(
                    'images/instruction/box-{}.png'.format(self.box_style))
                self.windowSurfaceObj.blit(instructions, (0, height * .685))

                # Load time box image
                time_box = pygame.image.load(
                    'images/box/{}.png'.format(self.time_box_style))

                # If in challenge mode, only display the goal time
                if mode == 'challenge':
                    # Displays your goal time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         goal_time_render_top + (height * .025)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.goal_time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         goal_time_render_top + (height * .09)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Goal Time'), False, pygame.Color(0, 0, 0)),
                        (box_render_left, goal_time_render_top))

                # Otherwise, display your current time and goal time
                else:

                    # Displays your current time
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Your Time'), False, pygame.Color(0, 0, 0)),
                        (box_render_left, your_time_render_top))

                    # Displays your goal time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         goal_time_render_top + (height * .025)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.goal_time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         goal_time_render_top + (height * .09)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Goal Time'), False, pygame.Color(0, 0, 0)),
                        (box_render_left, goal_time_render_top))

                # Displays the players score
                self.windowSurfaceObj.blit(self.fontObj.render(
                    str(self.score_count), False, pygame.Color(0, 0, 0)),
                    (width * .69, height * .56))

                # Displays help text
                text = self.challengeText.render(
                    self._('When you think the clock is correct, press'),
                    False, pygame.Color(255, 255, 255))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .44 - (fw / 2), height * .76))

                # Display help text at the bottom of the screen
                render_top = height * .895
                text = self.infoText.render(
                    self._('Hour Hand'), False, pygame.Color(0, 255, 0))
                text2 = self.infoText.render(
                    self._('= press'), False, pygame.Color(255, 255, 255))
                fw, fh = text.get_size()
                fw2, fh2 = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .30 - ((fw + fw2) / 2), render_top))
                self.windowSurfaceObj.blit(
                    text2, (width * .31 + (fw / 2) - (fw2 / 2), render_top))
                text = self.infoText.render(self._('Minute Hand'), False,
                                            pygame.Color(255, 0, 0))
                text2 = self.infoText.render(
                    self._('= press'), False, pygame.Color(255, 255, 255))
                fw, fh = text.get_size()
                fw2, fh2 = text2.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .75 - ((fw + fw2) / 2), render_top))
                self.windowSurfaceObj.blit(
                    text2, (width * .76 + (fw / 2) - (fw2 / 2), render_top))

                # Display the enter button text
                text = self.enterButton.render(
                    self._('enter'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .885 - (fw / 2), height * .79))

                # Display the shift button text
                text = self.shiftButton.render(
                    self._('shift'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                render_top = height * .9
                self.windowSurfaceObj.blit(
                    text, (width * .445 - (fw / 2), render_top))
                self.windowSurfaceObj.blit(
                    text, (width * .9375 - (fw / 2), render_top))

            # Draw the vicotry screen
            elif mode == 'victory':
                self.windowSurfaceObj.blit(self.victory, (0, 0))

            # Draw the menu screen
            elif mode == 'menu':
                render_left = width * .27
                interval = .18
                spacer = .33

                screen = transform.scale(
                    self.MenuScreen, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))
                for i in range(0, 3):
                    text = self.menuText.render(
                        self._('Press'), False, pygame.Color(0, 0, 0))
                    fw, fh = text.get_size()
                    self.windowSurfaceObj.blit(
                        text, (render_left - (fw / 2), height * spacer))
                    spacer += interval

                render_left = width * .48
                spacer = .33
                self.windowSurfaceObj.blit(self.menuText.render(
                    self._('Play'), False, pygame.Color(0, 0, 0)),
                    (render_left, height * spacer))
                self.windowSurfaceObj.blit(self.menuText.render(
                    self._('Challenge').decode('utf8'),
                    False, pygame.Color(0, 0, 0)),
                    (render_left, height * (spacer + interval)))
                self.windowSurfaceObj.blit(self.menuText.render(
                    self._('How To Play').decode('utf8'),
                    False, pygame.Color(0, 0, 0)),
                    (render_left, height * (spacer + (interval * 2))))

            # Draw the language selection screen
            elif self.mode == 'language':
                screen = transform.scale(
                    self.Languages, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

            # Draw the how to play screen
            else:
                screen = transform.scale(
                    self.HowToScreen, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                text = self.howToPlay.render(
                    self._('How To Play').decode('utf8'),
                    False, pygame.Color(255, 255, 0))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, ((width * .52) - (fw / 2), height * .05))

                text = self.fontObj.render(
                    self._('When you think it is correct, press'),
                    False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .42 - (fw / 2), height * .89))

                text = self.helpText.render(
                    self._('Press this key'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                render_left = width * .22 - (fw / 2)
                render_top = height * .63
                self.windowSurfaceObj.blit(text, (render_left, render_top))

                self.windowSurfaceObj.blit(self.helpText.render(
                    self._('to move the').decode('utf8'), False,
                    pygame.Color(0, 0, 0)),
                    (render_left, render_top + fh))
                self.windowSurfaceObj.blit(self.helpText.render(
                    self._('hour hand'), False,
                    pygame.Color(0, 0, 0)),
                    (render_left, render_top + (fh * 2)))

                text = self.helpText.render(
                    self._('Press this key'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                render_left = width * .78 - (fw / 2)
                self.windowSurfaceObj.blit(text, (render_left, render_top))

                self.windowSurfaceObj.blit(self.helpText.render(
                    self._('to move the').decode('utf8'), False,
                    pygame.Color(0, 0, 0)),
                    (render_left, render_top + fh))
                self.windowSurfaceObj.blit(self.helpText.render(
                    self._('minute hand'), False,
                    pygame.Color(0, 0, 0)),
                    (render_left, render_top + (fh * 2)))

                text = self.enterButton.render(
                    self._('enter'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .78 - (fw / 2), height * .915))

                text = self.shiftButton.render(
                    self._('shift'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                render_top = height * .43

                self.windowSurfaceObj.blit(
                    text, (width * .205 - (fw / 2), render_top))
                self.windowSurfaceObj.blit(
                    text, (width * .755 - (fw / 2), render_top))

        if self.update_hands:

                # Draw the clock
                clock = pygame.image.load(
                    'images/clock/clock-{}.png'.format(self.clock_style))
                self.windowSurfaceObj.blit(
                    clock, (clock_render_left, clock_render_top))

                # Draw the minute hand on the clock
                self.windowSurfaceObj.blit(
                    HANDS['minute'][self.minute]['image'],
                    (HANDS['minute'][self.minute]['render_left'],
                     HANDS['minute'][self.minute]['render_top']))

                # Draw the hour hand on the clock
                self.windowSurfaceObj.blit(
                    HANDS['hour'][self.hour]['image'],
                    (HANDS['hour'][self.hour]['render_left'],
                     HANDS['hour'][self.hour]['render_top']))

                # Draw the clock center
                screen = transform.scale(
                    self.ClockCenter, (width/22, height/18))
                self.windowSurfaceObj.blit(
                    screen,
                    (clock_render_left + (width * .2275),
                     clock_render_top + (height * .31)))

                if self.mode == 'play':

                    # Load time box image
                    time_box = pygame.image.load(
                        'images/box/{}.png'.format(self.time_box_style))

                    # Displays your time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         your_time_render_top + (height * .025)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         your_time_render_top + (height * .09)))

    def loadHands(self):
        angles = [0, -30, -60, -90, -120, -150, -180,
                  -210, -240, -270, -300, -330]

        minute_image = pygame.image.load(
            'images/hand/minute-{}.png'.format(self.minute_style))

        hour_image = pygame.image.load(
            'images/hand/hour-{}.png'.format(self.hour_style))

        for i in range(0, len(angles)):
            minute_hand = pygame.transform.rotate(minute_image, angles[i])
            hour_hand = pygame.transform.rotate(hour_image, angles[i])
            HANDS['minute'][i*self.increment]['image'] = minute_hand
            HANDS['hour'][i]['image'] = hour_hand

    def __init__(self, handle):

        print "running activity init", handle
        activity.Activity.__init__(self, handle)
        print "activity running"

        self.badges = badges(__name__, 'org.laptop.SkyTime')

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # Generates the first random time for challenge mode
        self.hour = self.random_hour()
        self.minute = self.random_minute(self.increment)
        self.time = str(self.hour) + ':'
        if self.minute < 10:
            self.time += '0'
        self.time += str(self.minute)
        if self.hour == 12:
            self.hour = 0

        # How many frames the victory sun has been up
        self.goal_time = self.set_time(self.increment)

        # Initializes pygame and the screen Surface object
        pygame.init()
        self.windowSurfaceObj = pygame.display.set_mode(
            (width, height))

        # Loads all of the assets
        self.MenuScreen = pygame.image.load('images/MenuScreen.gif')
        self.HowToScreen = pygame.image.load('images/HowToScreen.gif')
        self.ClockCenter = pygame.image.load(
            'images/clock/center-{}.png'.format(self.center_style))
        self.Languages = pygame.image.load('images/language.gif')
        self.victory = pygame.image.load('images/Sun.gif')
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.shiftButton = pygame.font.Font('freesansbold.ttf', 16)
        self.enterButton = pygame.font.Font('freesansbold.ttf', 20)
        self.howToPlay = pygame.font.Font('freesansbold.ttf', 65)
        self.challengeText = pygame.font.Font('freesansbold.ttf', 42)
        self.helpText = pygame.font.Font('freesansbold.ttf', 28)
        self.infoText = pygame.font.Font('freesansbold.ttf', 28)
        self.menuText = pygame.font.Font('freesansbold.ttf', 52)

        # Draws the menu screen to start with
        self.windowSurfaceObj.blit(self.MenuScreen, (0, 0))

        # Loop the game until the player quits
        while self.gameloop:

            self.drawScreen(self.mode)
            self.update_screen = False
            self.update_hands = False

            # Checks if the player won the challenge
            if self.time == self.goal_time and self.winner:
                self.waited += 1

                if self.waited > 40:

                    # Generates a new random time
                    self.hour = self.random_hour()
                    self.minute = self.random_minute(self.increment)

                    self.time = str(self.hour) + ':'
                    if self.minute < 10:
                        self.time += '0'
                    self.time += str(self.minute)
                    self.goal_time = self.set_time(self.increment)

                    if self.hour == 12:
                        self.hour = 0

                    self.waited = 0
                    self.incorrect_count = 0
                    self.update_screen = True
                    self.update_hands = True
                    self.playing = True
                    self.winner = False

                    if self.prev_mode == 'play':
                        self.mode = 'play'
                    else:
                        self.mode = 'challenge'

            # Check if the player wants to quit the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                # Check for input and draw information
                elif event.type == KEYDOWN and self.winner is False:

                    if self.mode == 'language':
                        if event.key == K_1:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeEnglish'])
                            self._ = lang.ugettext
                            self.mode = 'menu'
                            self.update_screen = True

                        if event.key == K_2:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeSpanish'])
                            self._ = lang.ugettext
                            self.mode = 'menu'
                            self.update_screen = True

                        if event.key == K_3:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeFrench'])
                            self._ = lang.ugettext
                            self.infoText = pygame.font.Font(
                                'freesansbold', 22)
                            self.challengeText = pygame.font.Font(
                                'freesansbold', 34)
                            self.mode = 'menu'
                            self.update_screen = True

                    # Check what mode the player has selected
                    elif self.mode == 'menu':
                        # Draw the play screen
                        if event.key == K_1:
                            self.mode = 'play'
                            self.loadHands()
                            self.playing = True
                            self.update_screen = True
                            self.update_hands = True

                        # Draw the challenge screen
                        elif event.key == K_2:
                            self.mode = 'challenge'
                            self.loadHands()
                            self.playing = True
                            self.update_screen = True
                            self.update_hands = True

                        # Draw How To Play
                        elif event.key == K_3:
                            self.mode = 'howtoplay'
                            self.playing = False
                            self.update_screen = True
                            self.update_hands = False

                        # Go back to language select
                        elif event.key == K_BACKSPACE:
                            self.mode = 'language'
                            self.playing = False
                            self.update_screen = True
                            self.update_hands = False

                    # Go back to the menu
                    elif event.key == K_BACKSPACE:
                        self.mode = 'menu'
                        self.playing = False
                        self.update_screen = True
                        self.update_hands = False

                    # Increments the hour by 1
                    if event.key == K_LSHIFT:
                        self.hour += 1
                        if self.hour > 11:
                            self.hour = 0
                            self.time = '12:'
                        else:
                            self.time = str(self.hour) + ':'
                        if self.minute < 10:
                            self.time += '0'

                        self.time += str(self.minute)
                        self.update_hands = True

                    # Increments the minutes by 5
                    elif event.key == K_RSHIFT:
                        self.minute += self.increment
                        if self.hour == 0:
                            self.time = '12:'
                        else:
                            self.time = str(self.hour) + ':'
                        if self.minute == 60:
                            self.minute = 0
                        if self.minute < 10:
                            self.time += '0'

                        self.time += str(self.minute)
                        self.update_hands = True

                    # Check if the player has the correct time
                    elif event.key == K_RETURN:
                        if self.time == self.goal_time and self.playing:
                            self.prev_mode = self.mode
                            self.mode = 'victory'
                            self.playing = False
                            self.winner = True
                            self.update_screen = True
                            self.update_hands = False
                            self.score_count += 1

                            #Award badges
                            if self.score_count == 1:
                                self.badges.award('Hair Past a Freckle',
                                                  'Completed your first time')
                                if self.mode == 'challenge':
                                    self.badges.award(
                                        'Challenge Complete',
                                        'Completed your first challenge time')
                            if self.score_count == 5:
                                self.badges.award(
                                    'First Five',
                                    'Obtained your first five suns')
                            if self.score_count == 100:
                                self.badges.award('ChronoKeeper',
                                                  'Obtained 100 suns')

                        elif self.playing:
                            if self.incorrect_count == 3:
                                self.badges.award(
                                    'Rainy Day',
                                    'Answered incorrectly 3 times in a row')
                                self.incorrect_count += 1

                    # Quit the game
                    elif event.key == K_ESCAPE:
                        self.gameloop = False
                        pygame.quit()

            if self.gameloop:
                pygame.display.update()
