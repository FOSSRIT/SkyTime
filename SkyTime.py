#!/usr/bin/env python

import pygame
from gi.repository import Gtk
import gettext
import os

from random import randint
from pygame import transform, mouse
from button import Button
from badges import badges
from pygame.locals import K_1, K_2, K_3, K_4, K_ESCAPE, K_RETURN,\
    K_LSHIFT, K_RSHIFT, K_BACKSPACE, QUIT, KEYDOWN, K_LEFT, K_RIGHT

from constants import width, height, clock_render_left, clock_render_top, \
    box_render_left, time_render_left, your_time_render_top, HANDS, \
    goal_time_render_top, CLOCK_REWARDS, REWARDS_DICT, BACKGROUND_REWARDS, \
    MENU_OPTIONS, REWARD_OPTIONS


class SkyTime():

    def __init__(self, bundle_id="org.laptop.SkyTime"):

        self.button = Button(0, 0, 100, 100)

        # Declaring Variables
        self.hour = 12
        self.minute = 0
        self.time = ''
        self.goal_time = ''
        self.playing = False
        self.winner = False
        self.gameloop = True
        self.update_hands = False
        self.update_screen = True
        self.play_victory = False
        self.clock_rewards = []
        self.background_rewards = []
        self.increment = 5
        self.waited = 0
        self.display_badge = 0
        self.sun_count = 0
        self.career_suns = 0
        self.mode = 'language'
        self.prev_mode = 'language'
        self.reward_selected = 0
        self.cur_reward_state = 'Clock Faces'
        self.badge_awarded = None
        self.incorrect_count = 0
        self.text_color = (0, 0, 0)

        self.hour_style = 'default'
        self.minute_style = 'default'
        self.center_style = 'default'
        self.background_style = 'default'
        self.clock_style = 'default'
        self.box_style = 'default'
        self.time_box_style = 'white'

        self.badges = badges("SkyTime", bundle_id)

        # The angles for the clock hands
        self.angles = [0, -30, -60, -90, -120, -150, -180,
                       -210, -240, -270, -300, -330]

        # Loads all of the assets
        pygame.font.init()
        self.howToScreen = pygame.image.load('images/HowToScreen.gif')
        self.clockCenter = pygame.image.load('images/clock_center/default.png')
        self.languages = pygame.image.load('images/language.png')
        self.delete = pygame.image.load('images/buttons/delete.png')
        self.victory = pygame.image.load('images/Sun.gif')
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.menuText = pygame.font.Font('freesansbold.ttf', 52)
        self.infoText = pygame.font.Font('freesansbold.ttf', 28)
        self.value = pygame.font.Font('freesansbold.ttf', 28)
        self.helpText = pygame.font.Font('freesansbold.ttf', 28)
        self.challengeText = pygame.font.Font('freesansbold.ttf', 42)
        self.howToPlay = pygame.font.Font('freesansbold.ttf', 65)
        self.enterButton = pygame.font.Font('freesansbold.ttf', 20)
        self.shiftButton = pygame.font.Font('freesansbold.ttf', 16)

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

    def drawScreen(self):

        # Only updates the player's screen if needed
        if self.update_screen:

            # Display the actual game screens (play and challenge)
            if self.playing:

                # Set the background
                background = pygame.image.load(
                    'images/background/{}.png'.format(self.background_style))
                screen = transform.scale(background, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                # Display the instructional box
                instructions = pygame.image.load(
                    'images/instruction/box-{}.png'.format(self.box_style))
                self.windowSurfaceObj.blit(instructions, (0, height * .71))

                # Load time box image
                time_box = pygame.image.load(
                    'images/box/{}.png'.format(self.time_box_style))

                # Load sun counter image
                sun = pygame.image.load('images/sun.png')
                self.windowSurfaceObj.blit(sun, (width * .6, height * .52))

                # Displays the players score
                self.windowSurfaceObj.blit(self.fontObj.render(
                    str(self.sun_count), False, self.text_color),
                    (width * .73, height * .575))

                if self.mode == 'challenge':
                    # Displays your goal time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         goal_time_render_top + (height * .045)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.goal_time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         goal_time_render_top + (height * .09)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Goal Time'), False, self.text_color),
                        (box_render_left, goal_time_render_top))

                else:

                    # Displays your goal time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         goal_time_render_top + (height * .045)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.goal_time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         goal_time_render_top + (height * .09)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Goal Time'), False, self.text_color),
                        (box_render_left, goal_time_render_top))

                # Displays help text
                text = self.challengeText.render(
                    self._('When you think the clock is correct, press'),
                    False, pygame.Color(255, 255, 255))
                fw, fh = text.get_size()
                self.windowSurfaceObj.blit(
                    text, (width * .44 - (fw / 2), height * .79))

                # Display help text at the bottom of the screen
                render_top = height * .92
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
                text = self.infoText.render(
                    self._('Minute Hand'), False, pygame.Color(255, 0, 0))
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
                    text, (width * .885 - (fw / 2), height * .82))

                # Display the shift button text
                text = self.shiftButton.render(
                    self._('shift'), False, pygame.Color(0, 0, 0))
                fw, fh = text.get_size()
                render_top = height * .925
                self.windowSurfaceObj.blit(
                    text, (width * .445 - (fw / 2), render_top))
                self.windowSurfaceObj.blit(
                    text, (width * .9375 - (fw / 2), render_top))

                # Display go back info
                back_info = self.infoText.render(
                    self._('Go Back'), False, self.text_color)
                fw, fh = back_info.get_size()
                self.windowSurfaceObj.blit(
                    back_info,
                    ((width * .8) - (fw / 2), (height * .04) - (fh / 2)))

                button = transform.scale(self.delete, (width/8, height/15))
                self.windowSurfaceObj.blit(button, (width * .85, height * .01))

                erase = self.enterButton.render(
                    self._('erase'), False, pygame.Color(0, 0, 0))
                self.windowSurfaceObj.blit(
                    erase, (width * .885, height * .027))

            # Draw the loading screen
            elif self.mode == 'loading':

                screen = pygame.image.load(
                    'images/background/{}.png'.format(self.background_style))
                screen = transform.scale(screen, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                render_left = width * .33
                render_top = height * .4
                new_game_button = pygame.image.load('images/buttons/1.png')
                iw, ih = new_game_button.get_size()
                self.windowSurfaceObj.blit(
                    new_game_button, (render_left, render_top - (ih / 2)))

                new_game = self.menuText.render(
                    self._('New Game'), False, self.text_color)
                fw, fh = new_game.get_size()
                self.windowSurfaceObj.blit(
                    new_game, (render_left + iw, render_top - (fh / 2)))

                load_game_button = pygame.image.load('images/buttons/2.png')
                self.windowSurfaceObj.blit(
                    load_game_button, (render_left, render_top + ih))

                load_game = self.menuText.render(
                    self._('Load Game'), False, self.text_color)
                self.windowSurfaceObj.blit(
                    load_game, (render_left + iw, render_top + ih + (fh / 2)))

            # Draw the menu screen
            elif self.mode == 'menu':
                render_left = width * .35
                interval = .18
                spacer = .22

                screen = pygame.image.load(
                    'images/background/{}.png'.format(self.background_style))
                screen = transform.scale(screen, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                for i in range(0, 4):

                    # Display 'Play'
                    text = self.menuText.render(
                        self._('Press'), False, self.text_color)
                    fw, fh = text.get_size()
                    self.windowSurfaceObj.blit(
                        text, (render_left - (fw / 2), height * spacer))

                    # Display the button associated with the menu option
                    button = pygame.image.load(
                        'images/buttons/{}.png'.format(i + 1))
                    iw, ih = button.get_size()
                    button_render_left = render_left + (fw / 2)
                    self.windowSurfaceObj.blit(
                        button,
                        (button_render_left, (height * spacer) - (ih * .28)))

                    # Display the menu option name
                    option = self.menuText.render(
                        self._(MENU_OPTIONS[i]), False, self.text_color)
                    fw, fh = option.get_size()
                    self.windowSurfaceObj.blit(
                        option, (button_render_left + iw, (height * spacer)))

                    spacer += interval

                # Display go back info
                back_info = self.infoText.render(
                    self._('Go Back'), False, self.text_color)
                fw, fh = back_info.get_size()
                self.windowSurfaceObj.blit(
                    back_info,
                    ((width * .8) - (fw / 2), (height * .04) - (fh / 2)))

                button = transform.scale(self.delete, (width/8, height/15))
                self.windowSurfaceObj.blit(button, (width * .85, height * .01))

                erase = self.enterButton.render(
                    self._('erase'), False, pygame.Color(0, 0, 0))
                self.windowSurfaceObj.blit(
                    erase, (width * .885, height * .027))

            # Draw the rewards screen
            elif self.mode == 'rewards':

                # Display the screen
                background = pygame.image.load(
                    'images/background/{}.png'.format(self.background_style))
                screen = transform.scale(background, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                # Display the amount of suns the player has
                sun_counter = pygame.image.load(
                    'images/rewards/sun-counter.png')
                iw, ih = sun_counter.get_size()

                your_suns = self.infoText.render(
                    self._('You have {}').format(self.sun_count),
                    False, self.text_color)
                fw, fh = your_suns.get_size()

                render_left = width * .175
                render_top = height * .14

                self.windowSurfaceObj.blit(
                    your_suns,
                    (render_left - (fw / 2),
                     render_top - (fh / 2)))

                self.windowSurfaceObj.blit(
                    sun_counter,
                    (render_left + (fw / 2),
                     render_top - (ih / 2)))

                help_text = self.infoText.render(
                    self._('Press enter to select your design'),
                    False, self.text_color)
                fw, fh = help_text.get_size()

                self.windowSurfaceObj.blit(
                    help_text,
                    ((width * .7) - (fw / 2),
                     (render_top - (fh / 2))))

                spacer = .2
                interval = .3
                counter = 1

                # Draw the different reward titles at the top
                for title in REWARD_OPTIONS:

                    # Check what current state the user is in
                    if title == self.cur_reward_state:
                        color = (255, 0, 0)
                    else:
                        color = self.text_color

                    title_text = self.infoText.render(
                        self._(title), False, color)
                    fw, fh = title_text.get_size()

                    render_left = (width * spacer) - (fw / 2)
                    render_top = height * .05

                    self.windowSurfaceObj.blit(
                        title_text, (render_left, render_top - (fh / 2)))

                    num_tab = pygame.image.load(
                        'images/buttons/{}.png'.format(counter))
                    iw, ih = num_tab.get_size()
                    self.windowSurfaceObj.blit(
                        num_tab, (render_left - iw, render_top - (ih / 2)))

                    spacer += interval
                    counter += 1

                # User is looking at the clock face rewards
                if self.cur_reward_state == 'Clock Faces':
                    rewards = CLOCK_REWARDS
                    cur_state = 'clock'

                # User is looking at the background rewards
                elif self.cur_reward_state == 'Backgrounds':
                    rewards = BACKGROUND_REWARDS
                    cur_state = 'background'

                counter = 0
                column = 0
                row = 0
                render_left = width * .12
                render_top = height * .32

                spacer_column = width * .25
                spacer_row = height * .4

                # Display all the different rewards for this category
                for reward in rewards:

                    # Load the image of the reward and scale it
                    reward_image = pygame.image.load(
                        'images/{}/{}.png'.format(cur_state, reward))
                    reward_image = transform.scale(
                        reward_image, (width/6, height/5))
                    rw, rh = reward_image.get_size()

                    # Check if the user has this reward selected
                    if counter == self.reward_selected:
                        border = pygame.image.load(
                            'images/rewards/selected.png')

                    # Check if the user has earned this reward
                    elif REWARDS_DICT[cur_state][reward]['earned']:
                        border = pygame.image.load(
                            'images/rewards/earned.png')

                    # User has not earned this reward
                    else:
                        border = pygame.image.load(
                            'images/rewards/unearned.png')

                    # Scale the border of the reward
                    border = transform.scale(border, (width/5, height/4))
                    bw, bh = border.get_size()

                    # Load the sun counter image
                    sun = pygame.image.load(
                        'images/rewards/sun-counter.png')
                    sw, sh = sun.get_size()

                    # Display the border
                    self.windowSurfaceObj.blit(
                        border,
                        ((render_left +
                         (column * spacer_column) - (bw / 2)),
                            (render_top + (row * spacer_row) - (bh / 2))))

                    # Display the reward image
                    self.windowSurfaceObj.blit(
                        reward_image,
                        ((render_left +
                         (column * spacer_column) - (rw / 2)),
                            (render_top + (row * spacer_row) - (rh / 2))))

                    # Display the number of suns the reward costs
                    cost = self.value.render(
                        REWARDS_DICT[cur_state][reward]['value'],
                        False, self.text_color)
                    fw, fh = cost.get_size()
                    self.windowSurfaceObj.blit(
                        cost,
                        ((render_left +
                         (column * spacer_column) - (fw / 2)),
                            (render_top +
                             (row * spacer_row) + (bh / 2) + (fh / 2))))

                    # Display the sun icon
                    self.windowSurfaceObj.blit(
                        sun,
                        ((render_left +
                         (column * spacer_column) - (bw / 2)),
                            (render_top +
                             (row * spacer_row) + (bh / 2) - (sh / 9))))

                    if column == 3:
                        column = 0
                        row += 1

                    else:
                        column += 1

                    counter += 1

                # Display go back info
                back_info = self.infoText.render(
                    self._('Go Back'), False, self.text_color)
                fw, fh = back_info.get_size()
                self.windowSurfaceObj.blit(
                    back_info,
                    ((width * .8) - (fw / 2), (height * .04) - (fh / 2)))

                button = transform.scale(self.delete, (width/8, height/15))
                self.windowSurfaceObj.blit(button, (width * .85, height * .01))

                erase = self.enterButton.render(
                    self._('erase'), False, pygame.Color(0, 0, 0))
                self.windowSurfaceObj.blit(
                    erase, (width * .885, height * .027))

            # Draw the vicotry screen
            elif self.mode == 'victory':

                # Display the screen
                screen = transform.scale(self.victory, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

            # Draw the language selection screen
            elif self.mode == 'language':

                # Display the screen
                screen = transform.scale(self.languages, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

            # Draw the how to play screen
            else:

                # Display the screen
                screen = transform.scale(self.howToScreen, (width, height))
                self.windowSurfaceObj.blit(screen, (0, 0))

                text = self.howToPlay.render(
                    self._('How To Play'), False, pygame.Color(255, 255, 0))
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
                    self._('Press this key'),
                    False, pygame.Color(0, 0, 0))

                fw, fh = text.get_size()
                render_left = width * .22 - (fw / 2)
                render_top = height * .63
                self.windowSurfaceObj.blit(text, (render_left, render_top))

                self.windowSurfaceObj.blit(self.helpText.render(
                    self._('to move the'), False,
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
                    self._('to move the'), False,
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

                # Display go back info
                back_info = self.infoText.render(
                    self._('Go Back'), False, self.text_color)
                fw, fh = back_info.get_size()
                self.windowSurfaceObj.blit(
                    back_info,
                    ((width * .8) - (fw / 2), (height * .04) - (fh / 2)))

                button = transform.scale(self.delete, (width/8, height/15))
                self.windowSurfaceObj.blit(button, (width * .85, height * .01))

                erase = self.enterButton.render(
                    self._('erase'), False, pygame.Color(0, 0, 0))
                self.windowSurfaceObj.blit(
                    erase, (width * .885, height * .027))

        # Update the clock hands
        if self.update_hands:

                # Draw the clock
                clock = pygame.image.load(
                    'images/clock/{}.png'.format(self.clock_style))
                self.windowSurfaceObj.blit(
                    clock, (clock_render_left, clock_render_top))

                # Draw the clock hands
                self.windowSurfaceObj.blit(
                    HANDS['minute'][self.minute]['image'],
                    (HANDS['minute'][self.minute]['render_left'],
                     HANDS['minute'][self.minute]['render_top']))

                self.windowSurfaceObj.blit(
                    HANDS['hour'][self.hour]['image'],
                    (HANDS['hour'][self.hour]['render_left'],
                     HANDS['hour'][self.hour]['render_top']))

                # Draw the clock center
                screen = transform.scale(
                    self.clockCenter, (width/22, height/18))
                self.windowSurfaceObj.blit(
                    screen,
                    (clock_render_left + (width * .2275),
                     clock_render_top + (height * .31)))

                # Only update the player's time if not playing challenge mode
                if self.mode == 'play':

                    # Load time box image
                    time_box = pygame.image.load(
                        'images/box/{}.png'.format(self.time_box_style))

                    # Displays your time
                    self.windowSurfaceObj.blit(
                        time_box,
                        (box_render_left,
                         your_time_render_top + (height * .045)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self.time, False, pygame.Color(0, 0, 0)),
                        (time_render_left,
                         your_time_render_top + (height * .09)))
                    self.windowSurfaceObj.blit(self.fontObj.render(
                        self._('Your Time'), False, self.text_color),
                        (box_render_left, your_time_render_top))

    def loadHands(self):

        # Loads in the minute hand and creates an array with all of the angles
        minute_image = pygame.image.load(
            'images/hand/minute-{}.png'.format(self.minute_style))

        hour_image = pygame.image.load(
            'images/hand/hour-{}.png'.format(self.hour_style))

        for i in range(0, len(self.angles)):
            minute_hand = pygame.transform.rotate(minute_image, self.angles[i])
            hour_hand = pygame.transform.rotate(hour_image, self.angles[i])
            HANDS['minute'][i*self.increment]['image'] = minute_hand
            HANDS['hour'][i]['image'] = hour_hand

    def displayBadge(self, image_name):

        # Location of the info text and badge
        render_top = height * .55
        render_left = width * .89

        # Display info text
        info = self.enterButton.render(
            self._("You have earned badge:"),
            False, pygame.Color(0, 0, 0))
        fw, fh = info.get_size()
        self.windowSurfaceObj.blit(
            info, (render_left - (fw / 2), render_top - (fh / 2)))

        # Display badge name
        badge_name = self.enterButton.render(
            self._('{}').format(image_name),
            False, pygame.Color(0, 0, 0))

        fw, fh = badge_name.get_size()
        self.windowSurfaceObj.blit(
            badge_name,
            (render_left - (fw / 2), render_top + (fh / 2)))

        # Load and scale the badge image
        badge_image = pygame.image.load('badges/{}.png'.format(image_name))
        badge_image = transform.scale(
            badge_image, (width/12, height/10))

        # Display the badge earned
        iw, ih = badge_image.get_size()
        self.windowSurfaceObj.blit(
            badge_image, (render_left - (iw / 2), render_top + (ih / 2)))

    def save_game(self):

        path = os.path.join(
            os.path.split(__file__)[0], 'saved.txt')
        with open(path, mode='w') as saved_game:
            for clock_reward in REWARDS_DICT['clock'].values():
                if clock_reward['earned']:
                    saved_game.write(
                        'clock:' + clock_reward['name'] + '\n')
            for bg_reward in REWARDS_DICT[
                    'background'].values():
                if bg_reward['earned']:
                    saved_game.write(
                        'background:' + bg_reward[
                            'name'] + '\n')
            saved_game.write(
                'score:' + str(self.sun_count) + '\n')
            saved_game.write(
                'career:' + str(self.career_suns))

    def run(self):

        # Initializes pygame and the screen Surface object
        self.windowSurfaceObj = pygame.display.get_surface()

        # Generates a new random time
        self.hour = randint(1, 12)
        self.minute = self.random_minute(self.increment)

        self.time = str(self.hour) + ':'
        if self.minute < 10:
            self.time += '0'
        self.time += str(self.minute)
        self.goal_time = self.set_time(self.increment)

        if self.hour == 12:
            self.hour = 0

        # Loop the game until the player quits
        while self.gameloop:

            while Gtk.events_pending():
                Gtk.main_iteration()

            self.drawScreen()
            self.update_screen = False
            self.update_hands = False

            #print(mouse.get_pressed()[0] == 1)
            print(self.button.isClicked(mouse.get_pos()[0], mouse.get_pos()[1], mouse.get_pressed()[0]))

            # Create a timer for displaying a badge recently earned
            if self.badge_awarded is not None and self.playing:
                self.display_badge += 1
                self.displayBadge(self.badge_awarded)

                if self.display_badge > 100:
                    self.badge_awarded = None
                    self.update_screen = True
                    self.update_hands = True
                    self.display_badge = 0

            # Checks if the player won the challenge
            if self.time == self.goal_time and self.winner:
                self.waited += 1

                if self.play_victory:
                    pygame.mixer.music.load('sounds/jenn-yay.wav')
                    pygame.mixer.music.play()
                    self.save_game()
                    self.play_victory = False

                if self.waited > 100:

                    # Generates a new random time
                    self.hour = randint(1, 12)
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
                    self.winner = False
                    self.update_screen = True
                    self.update_hands = True
                    self.playing = True

                    if self.prev_mode == 'play':
                        self.mode = 'play'
                    else:
                        self.mode = 'challenge'

            # Check if the player wants to quit the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    self.gameloop = False

                # Check for input and draw information
                elif event.type == KEYDOWN and self.winner is False:

                    # Check what language the player has selected
                    if self.mode == 'language':

                        # Play the game in English
                        if event.key == K_1:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeEnglish'])
                            self._ = lang.ugettext
                            self.mode = 'loading'
                            self.update_screen = True

                        # Play the game in Spanish
                        elif event.key == K_2:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeSpanish'])
                            self._ = lang.ugettext
                            self.mode = 'loading'
                            self.update_screen = True

                        # Play the game in French
                        elif event.key == K_3:
                            lang = gettext.translation(
                                'org.laptop.SkyTime',
                                'locale/',
                                languages=['SkyTimeFrench'])
                            self._ = lang.ugettext
                            self.infoText = pygame.font.Font(
                                'freesansbold.ttf', 22)
                            self.challengeText = pygame.font.Font(
                                'freesansbold.ttf', 34)
                            self.mode = 'loading'
                            self.update_screen = True

                    # Load a saved game or create a new game
                    elif self.mode == 'loading':
                        path = os.path.join(
                            os.path.split(__file__)[0], 'saved.txt')

                        # User wants to create a new game
                        if event.key == K_1:

                            new_game = open(path, 'w')
                            new_game.close()
                            self.mode = 'menu'
                            self.update_screen = True

                        # User wants to load a game
                        elif event.key == K_2:

                            # Try to load a previously saved game
                            try:
                                with open(path) as saved_game:
                                    for line in saved_game:
                                        line = line.rsplit()[0]
                                        reward = line.split(':')[1]
                                        reward_type = line.split(':')[0]

                                        if reward_type == 'clock':
                                            REWARDS_DICT['number_clocks'] += 1
                                            REWARDS_DICT[reward_type][
                                                reward]['earned'] = True

                                        elif reward_type == 'background':
                                            REWARDS_DICT[
                                                'number_backgrounds'] += 1
                                            REWARDS_DICT[reward_type][
                                                reward]['earned'] = True

                                        elif reward_type == 'score':
                                            self.sun_count = int(reward)

                                        elif reward_type == 'career':
                                            self.career_suns = int(reward)

                            # If a saved game doesn't exist, create a new one
                            except IOError:
                                new_game = open(path, 'w')
                                new_game.close()

                            self.mode = 'menu'
                            self.update_screen = True

                        # Go back to the menu
                        elif event.key == K_BACKSPACE:
                            self.mode = 'language'
                            self.update_screen = True

                    # Check if the player is in the reward screen
                    elif self.mode == 'rewards':

                        # Display the clock face rewards
                        if event.key == K_1:
                            self.cur_reward_state = 'Clock Faces'
                            self.reward_selected = 0
                            self.update_screen = True

                        # Display the background rewards
                        elif event.key == K_2:
                            self.cur_reward_state = 'Backgrounds'
                            self.reward_selected = 0
                            self.update_screen = True

                        # Go back to the menu
                        elif event.key == K_BACKSPACE:
                            self.mode = 'menu'
                            self.cur_reward_state = 'Clock Faces'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                        # The user selected a reward
                        elif event.key == K_RETURN:

                            # Selected a clock face reward
                            if self.cur_reward_state == 'Clock Faces':
                                reward = REWARDS_DICT['clock'][
                                    CLOCK_REWARDS[self.reward_selected]]

                                # Check if the reward has already been awarded
                                if reward['earned']:
                                    self.clock_style = CLOCK_REWARDS[
                                        self.reward_selected]
                                    self.update_screen = True

                                # Check if the user has enough for the reward
                                elif self.sun_count >= int(reward['value']):
                                    self.sun_count -= int(reward['value'])
                                    REWARDS_DICT['number_clocks'] += 1
                                    self.clock_rewards.append(
                                        'clock:' + reward['name'])
                                    reward['earned'] = True
                                    self.clock_style = CLOCK_REWARDS[
                                        self.reward_selected]
                                    self.save_game()
                                    self.update_screen = True

                                # Award badges
                                if REWARDS_DICT['number_clocks'] == 2:
                                    self.badges.award(
                                        '1 O\'clock',
                                        'Earned your first clock')
                                    self.badge_awarded = '1 O\'clock'

                                if REWARDS_DICT['number_backgrounds'] == 2:
                                    self.badges.award(
                                        'New Sky',
                                        'Purchased a new background')
                                    self.badge_awarded = 'New Sky'

                                if REWARDS_DICT['number_clocks'] == 4:
                                    self.badges.award(
                                        '3 O\'clock',
                                        'Earned three different clocks')
                                    self.badge_awarded = '3 O\'clock'

                                if REWARDS_DICT['clock'][
                                        'bluemoon']['earned']:
                                    self.badges.award(
                                        'Once in a Blue Moon',
                                        'Purchased the Blue Moon clock')
                                    self.badge_awarded = 'Once in a Blue Moon'

                                if REWARDS_DICT['number_clocks'] == 8:
                                    self.badges.award(
                                        'Clock Wizard',
                                        'Purchased all of the clocks')
                                    self.badge_awarded = 'Clock Wizard'

                                if REWARDS_DICT['number_backgrounds'] == 8:
                                    self.badges.award(
                                        'Interior Designer',
                                        'Purchased all of the backgrounds')
                                    self.badge_awarded = 'Interior Designer'

                            # Selected a background reward
                            elif self.cur_reward_state == 'Backgrounds':
                                reward = REWARDS_DICT['background'][
                                    BACKGROUND_REWARDS[self.reward_selected]]

                                # Check if the reward has already been awarded
                                if reward['earned']:
                                    self.background_style = BACKGROUND_REWARDS[
                                        self.reward_selected]
                                    self.text_color = REWARDS_DICT[
                                        'background'][self.background_style][
                                        'color']
                                    self.update_screen = True

                                # Check if the user has enough for the reward
                                elif self.sun_count >= int(reward['value']):
                                    self.sun_count -= int(reward['value'])
                                    REWARDS_DICT['number_backgrounds'] += 1
                                    reward['earned'] = True
                                    self.background_rewards.append(
                                        'background:' + reward['name'])
                                    self.background_style = BACKGROUND_REWARDS[
                                        self.reward_selected]
                                    self.text_color = REWARDS_DICT[
                                        'background'][self.background_style][
                                        'color']
                                    self.save_game()
                                    self.update_screen = True

                                # Award badges
                                if REWARDS_DICT['number_backgrounds'] == 2:
                                    self.badges.award(
                                        '1 O\'clock',
                                        'Earned your first clock')
                                    self.badge_awarded = '1 O\'clock'

                                if REWARDS_DICT['number_backgrounds'] == 4:
                                    self.badges.award(
                                        'Sky-Scaper',
                                        'Earned three different backgrounds')
                                    self.badge_awarded = 'Sky-Scaper'

                        # Move cursor to the left
                        elif event.key == K_LEFT:
                            if self.cur_reward_state == 'Clock Faces':
                                if self.reward_selected == 0:
                                    self.reward_selected = len(
                                        CLOCK_REWARDS) - 1
                                else:
                                    self.reward_selected -= 1

                            elif self.cur_reward_state == 'Backgrounds':
                                if self.reward_selected == 0:
                                    self.reward_selected = len(
                                        BACKGROUND_REWARDS) - 1
                                else:
                                    self.reward_selected -= 1

                            self.update_screen = True

                        # Move cursor to the right
                        elif event.key == K_RIGHT:
                            if self.cur_reward_state == 'Clock Faces':
                                if self.reward_selected == (
                                        len(CLOCK_REWARDS) - 1):
                                    self.reward_selected = 0
                                else:
                                    self.reward_selected += 1

                            if self.cur_reward_state == 'Backgrounds':
                                if self.reward_selected == (
                                        len(BACKGROUND_REWARDS) - 1):
                                    self.reward_selected = 0
                                else:
                                    self.reward_selected += 1

                            self.update_screen = True

                    # Check what mode the player has selected
                    elif self.mode == 'menu':
                        # Draw the play screen
                        if event.key == K_1:
                            self.mode = 'play'
                            self.update_screen = True
                            self.update_hands = True
                            self.loadHands()
                            self.playing = True

                        # Draw the challenge screen
                        elif event.key == K_2:
                            self.mode = 'challenge'
                            self.update_screen = True
                            self.update_hands = True
                            self.loadHands()
                            self.playing = True

                        # Draw How To Play
                        elif event.key == K_3:
                            self.mode = 'howtoplay'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                        # Draw Rewards Screen
                        elif event.key == K_4:
                            self.mode = 'rewards'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                        # Go back to language select
                        elif event.key == K_BACKSPACE:
                            self.mode = 'language'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                    elif self.mode == 'howtoplay':

                        # Go back to the menu
                        if event.key == K_BACKSPACE:
                            self.mode = 'menu'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                    # Check if the user is playing the game
                    if self.playing:

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
                            pygame.mixer.music.load('sounds/hour.wav')
                            pygame.mixer.music.play()
                            self.update_hands = True

                        # Increments the minutes by 5
                        if event.key == K_RSHIFT:
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
                            pygame.mixer.music.load('sounds/minute.wav')
                            pygame.mixer.music.play()
                            self.update_hands = True

                        # Go back to the menu
                        elif event.key == K_BACKSPACE:
                            self.mode = 'menu'
                            self.update_screen = True
                            self.update_hands = False
                            self.playing = False

                    # Check if the player has the correct time
                    if event.key == K_RETURN:
                        if self.time == self.goal_time and self.playing:
                            self.prev_mode = self.mode
                            self.playing = False
                            self.winner = True
                            self.play_victory = True
                            self.career_suns += 1
                            self.sun_count += 1

                            # Award badges
                            if self.sun_count == 1:
                                self.badges.award(
                                    'Hair Past a Freckle',
                                    'Completed your first time')
                                self.badge_awarded = 'Hair Past a Freckle'

                                if self.mode == 'challenge':
                                    self.badges.award(
                                        'Challenge Complete',
                                        'Completed your first challenge time')
                                    self.badge_awarded = 'Challenge Complete'

                            if self.sun_count == 5:
                                self.badges.award(
                                    'First Five',
                                    'Obtained your first five suns')
                                self.badge_awarded = 'First Five'

                            if self.sun_count == 100:
                                self.badges.award(
                                    'ChronoKeeper',
                                    'Obtained 100 suns')
                                self.badge_awarded = 'ChronoKeeper'

                            if self.career_suns == 1000:
                                self.badges.award(
                                    'Sunny Bags',
                                    'Obtained 1000 suns')
                                self.badge_awarded = 'Sunny Bags'

                            self.mode = 'victory'
                            self.update_screen = True

                        elif self.playing:
                            if self.incorrect_count == 2:
                                self.badges.award(
                                    'Rainy Day',
                                    'Answered incorrectly 3 times in a row')
                                self.badge_awarded = 'Rainy Day'

                            self.incorrect_count += 1

                    # Quit the game
                    if event.key == K_ESCAPE:
                        path = os.path.join(
                            os.path.split(__file__)[0], 'saved.txt')
                        with open(path, mode='w') as saved_game:
                            for clock_reward in REWARDS_DICT['clock'].values():
                                if clock_reward['earned']:
                                    saved_game.write(
                                        'clock:' + clock_reward['name'] + '\n')
                            for bg_reward in REWARDS_DICT[
                                    'background'].values():
                                if bg_reward['earned']:
                                    saved_game.write(
                                        'background:' + bg_reward[
                                            'name'] + '\n')
                            saved_game.write(
                                'score:' + str(self.sun_count) + '\n')
                            saved_game.write(
                                'career:' + str(self.career_suns))

                        self.gameloop = False

            if self.gameloop:
                pygame.display.update()


# Called after running ./SkyTime.py in the command line
def main():
    pygame.init()
    pygame.display.set_mode((width, height))
    game = SkyTime()
    game.run()

if __name__ == "__main__":
    main()
