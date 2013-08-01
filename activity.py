#!/usr/bin/env python

from sugar.activity import activity

from pygame.locals import K_1, K_2, K_3, K_ESCAPE, K_RETURN, \
    K_LSHIFT, K_RSHIFT, K_BACKSPACE, QUIT, KEYDOWN
import pygame
import gettext
from random import randint
from pygame import transform
from badges import badges


class SkyTimeActivity(activity.Activity):

    # Declaring Variables
    hour = 12
    minute = 0
    time = ''
    goal_time = ''
    challenge = False
    winner = False
    gameloop = True
    windowSurfaceObj = None
    fontObj = None
    PlayScreen = None
    ChallengeScreen = None
    ClockCenter = None
    minuteHand = []
    hourHand = []
    increment = 5
    waited = 0
    width = 1200
    height = 900
    mode = 'language'
    playing = False
    score = ''
    score_count = 0

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

        #Draw the normal play screen
        if self.playing:
            if self.mode == 'challenge':
                screen = transform.scale(
                    self.PlayScreen, (self.width, self.height))
                self.windowSurfaceObj.blit(screen, (0, 0))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self.goal_time, False, pygame.Color(0, 0, 0)),
                    (self.width * .71, self.height * .34))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self._('Goal Time'), False, pygame.Color(0, 0, 0)),
                    (self.width * .55, self.height * .25))

            else:
                screen = transform.scale(
                    self.ChallengeScreen, (self.width, self.height))
                self.windowSurfaceObj.blit(screen, (0, 0))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self.time, False, pygame.Color(0, 0, 0)),
                    (self.width * .71, self.height * .34))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self._('Your Time'), False, pygame.Color(0, 0, 0)),
                    (self.width * .55, self.height * .25))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self.goal_time, False, pygame.Color(0, 0, 0)),
                    (self.width * .71, self.height * .525))
                self.windowSurfaceObj.blit(self.fontObj.render(
                    self._('Goal Time').decode('utf8'),
                    False, pygame.Color(0, 0, 0)),
                    (self.width * .55, self.height * .435))

            # Draw the player's score
            self.windowSurfaceObj.blit(self.fontObj.render(
                self.score, False, pygame.Color(0, 0, 0)),
                (self.width * .69, self.height * .70))

            # Draw help text
            text = self.challengeText.render(
                self._('When you think the clock is correct, press'),
                False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            self.windowSurfaceObj.blit(
                text, (self.width * .44 - (fw / 2), self.height * .11))

            # Draw minute and hour hand help text at bottom of screen
            render_top = self.height * .92
            text = self.infoText.render(
                self._('Hour Hand'), False, pygame.Color(0, 255, 0))
            text2 = self.infoText.render(
                self._('= press'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            fw2, fh2 = text.get_size()
            self.windowSurfaceObj.blit(
                text, (self.width * .30 - ((fw + fw2) / 2), render_top))
            self.windowSurfaceObj.blit(
                text2, (self.width * .31 + (fw / 2) - (fw2 / 2), render_top))
            text = self.infoText.render(
                self._('Minute Hand'), False, pygame.Color(255, 0, 0))
            text2 = self.infoText.render(
                self._('= press'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            fw2, fh2 = text2.get_size()
            self.windowSurfaceObj.blit(
                text, (self.width * .75 - ((fw + fw2) / 2), render_top))
            self.windowSurfaceObj.blit(
                text2, (self.width * .76 + (fw / 2) - (fw2 / 2), render_top))

            # Draw shift button text
            text = self.shiftButton.render(
                self._('shift'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            render_top = self.height * .93
            self.windowSurfaceObj.blit(
                text, (self.width * .445 - (fw / 2), render_top))
            self.windowSurfaceObj.blit(
                text, (self.width * .9375 - (fw / 2), render_top))

            # Draw enter button text
            text = self.enterButton.render(
                self._('enter'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            self.windowSurfaceObj.blit(
                text, (self.width * .875 - (fw / 2), self.height * .145))

            # Draw the clock hands
            self.drawHands()

        # Draw the vicotry screen
        elif mode == 'victory':
            self.windowSurfaceObj.blit(self.victory, (0, 0))

        # Draw the menu screen
        elif mode == 'menu':
            render_left = self.width * .27
            interval = .18
            spacer = .33

            screen = transform.scale(
                self.MenuScreen, (self.width, self.height))
            self.windowSurfaceObj.blit(screen, (0, 0))
            for i in range(0, 3):
                text = self.menuText.render(
                    self._('Press'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (render_left - (fw / 2), self.height * spacer))
                spacer += interval

            render_left = self.width * .48
            spacer = .33
            self.windowSurfaceObj.blit(self.menuText.render(
                self._('Play'), False, pygame.Color(0, 0, 0)),
                (render_left, self.height * spacer))
            self.windowSurfaceObj.blit(self.menuText.render(
                self._('Challenge').decode('utf8'),
                False, pygame.Color(0, 0, 0)),
                (render_left, self.height * (spacer + interval)))
            self.windowSurfaceObj.blit(self.menuText.render(
                self._('How To Play').decode('utf8'),
                False, pygame.Color(0, 0, 0)),
                (render_left, self.height * (spacer + (interval * 2))))

        # Draw the language selection screen
        elif mode == 'language':
            screen = transform.scale(
                self.Languages, (self.width, self.height))
            self.windowSurfaceObj.blit(screen, (0, 0))

        # Draw the how to play screen
        else:
            screen = transform.scale(
                self.HowToScreen, (self.width, self.height))
            self.windowSurfaceObj.blit(screen, (0, 0))

            text = self.howToPlay.render(
                self._('How To Play').decode('utf8'),
                False, pygame.Color(255, 255, 0))
            fw, fh = text.get_size()
            self.windowSurfaceObj.blit(
                text, ((self.width * .52) - (fw / 2), self.height * .05))

            text = self.fontObj.render(
                self._('When you think it is correct, press'),
                False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            self.windowSurfaceObj.blit(
                text, (self.width * .42 - (fw / 2), self.height * .89))

            text = self.helpText.render(
                self._('Press this key'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            render_left = self.width * .22 - (fw / 2)
            render_top = self.height * .63
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
            render_left = self.width * .78 - (fw / 2)
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
                text, (self.width * .78 - (fw / 2), self.height * .915))

            text = self.shiftButton.render(
                self._('shift'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            render_top = self.height * .43

            self.windowSurfaceObj.blit(
                text, (self.width * .205 - (fw / 2), render_top))
            self.windowSurfaceObj.blit(
                text, (self.width * .755 - (fw / 2), render_top))

    def drawHands(self):

        # Checks the current time and draws the hands accordingly
        if self.minute == 0:
            self.windowSurfaceObj.blit(
                self.minuteHand[0], (self.width * .245, self.height * .33))
        elif self.minute == 5:
            self.windowSurfaceObj.blit(
                self.minuteHand[1], (self.width * .245, self.height * .34))
        elif self.minute == 10:
            self.windowSurfaceObj.blit(
                self.minuteHand[2], (self.width * .245, self.height * .41))
        elif self.minute == 15:
            self.windowSurfaceObj.blit(
                self.minuteHand[3], (self.width * .265, self.height * .505))
        elif self.minute == 20:
            self.windowSurfaceObj.blit(
                self.minuteHand[4], (self.width * .26, self.height * .505))
        elif self.minute == 25:
            self.windowSurfaceObj.blit(
                self.minuteHand[5], (self.width * .245, self.height * .505))
        elif self.minute == 30:
            self.windowSurfaceObj.blit(
                self.minuteHand[6], (self.width * .245, self.height * .515))
        elif self.minute == 35:
            self.windowSurfaceObj.blit(
                self.minuteHand[7], (self.width * .175, self.height * .5))
        elif self.minute == 40:
            self.windowSurfaceObj.blit(
                self.minuteHand[8], (self.width * .12, self.height * .5))
        elif self.minute == 45:
            self.windowSurfaceObj.blit(
                self.minuteHand[9], (self.width * .105, self.height * .51))
        elif self.minute == 50:
            self.windowSurfaceObj.blit(
                self.minuteHand[10], (self.width * .135, self.height * .405))
        elif self.minute == 55:
            self.windowSurfaceObj.blit(
                self.minuteHand[11], (self.width * .175, self.height * .35))

        if self.hour == 0:
            self.windowSurfaceObj.blit(
                self.hourHand[0], (self.width * .245, self.height * .39))
        elif self.hour == 1:
            self.windowSurfaceObj.blit(
                self.hourHand[1], (self.width * .25, self.height * .395))
        elif self.hour == 2:
            self.windowSurfaceObj.blit(
                self.hourHand[2], (self.width * .26, self.height * .435))
        elif self.hour == 3:
            self.windowSurfaceObj.blit(
                self.hourHand[3], (self.width * .27, self.height * .505))
        elif self.hour == 4:
            self.windowSurfaceObj.blit(
                self.hourHand[4], (self.width * .265, self.height * .515))
        elif self.hour == 5:
            self.windowSurfaceObj.blit(
                self.hourHand[5], (self.width * .255, self.height * .525))
        elif self.hour == 6:
            self.windowSurfaceObj.blit(
                self.hourHand[6], (self.width * .245, self.height * .53))
        elif self.hour == 7:
            self.windowSurfaceObj.blit(
                self.hourHand[7], (self.width * .195, self.height * .515))
        elif self.hour == 8:
            self.windowSurfaceObj.blit(
                self.hourHand[8], (self.width * .165, self.height * .5))
        elif self.hour == 9:
            self.windowSurfaceObj.blit(
                self.hourHand[9], (self.width * .165, self.height * .505))
        elif self.hour == 10:
            self.windowSurfaceObj.blit(
                self.hourHand[10], (self.width * .17, self.height * .435))
        elif self.hour == 11:
            self.windowSurfaceObj.blit(
                self.hourHand[11], (self.width * .2, self.height * .4))

        screen = transform.scale(self.ClockCenter,
                                (self.width / 22, self.height / 18))
        self.windowSurfaceObj.blit(screen,
                                  (self.width * .24, self.height * .5))
        return(0)

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
            (self.width, self.height))

        # Loads all of the assets
        self.MenuScreen = pygame.image.load('images/MenuScreen.gif')
        self.PlayScreen = pygame.image.load('images/PlayScreen.gif')
        self.HowToScreen = pygame.image.load('images/HowToScreen.gif')
        self.ChallengeScreen = pygame.image.load('images/ChallengeScreen.gif')
        self.ClockCenter = pygame.image.load('images/ClockCenter.png')
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

        # The angles for the clock hands
        angles = [-30, -60, -90, -120, -150, -180,
                  -210, -240, -270, -300, -330]

        # Loads in the minute hand and creates an array with all of the angles
        self.minuteHand = [pygame.image.load('images/MinHand.png')]
        for angle in angles:
            self.minuteHand.append(
                pygame.transform.rotate(self.minuteHand[0], angle))

        # Loads in the hour hand and creates an array with all the angles
        self.hourHand = [pygame.image.load('images/HourHand.png')]
        for angle in angles:
            self.hourHand.append(
                pygame.transform.rotate(self.hourHand[0], angle))

        # Draws the menu screen to start with
        self.windowSurfaceObj.blit(self.MenuScreen, (0, 0))

        # Loop the game until the player quits
        while self.gameloop:

            self.drawScreen(self.mode)
            self.score = str(self.score_count)

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

                        if event.key == K_2:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeSpanish'])
                            self._ = lang.ugettext
                            self.mode = 'menu'

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

                    elif self.mode == 'menu':
                        # Draw the PlayScreen
                        if event.key == K_1:
                            self.mode = 'play'
                            self.playing = True

                        # Draw the ChallengeScreen
                        elif event.key == K_2:
                            self.mode = 'challenge'
                            self.playing = True

                        # Draw How To Play
                        elif event.key == K_3:
                            self.mode = 'howtoplay'
                            self.playing = False

                        # Go back to language select
                        elif event.key == K_BACKSPACE:
                            self.mode = 'language'
                            self.playing = False

                    # Go back to the menu
                    elif event.key == K_BACKSPACE:
                        self.mode = 'menu'
                        self.playing = False

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

                    # Check if the player has the correct time
                    elif event.key == K_RETURN:
                        if self.time == self.goal_time and self.playing:
                            self.prev_mode = self.mode
                            self.mode = 'victory'
                            self.playing = False
                            self.winner = True
                            self.score_count += 1

                    # Quit the game
                    elif event.key == K_ESCAPE:
                        self.gameloop = False
                        pygame.quit()

            if self.gameloop:
                pygame.display.update()
