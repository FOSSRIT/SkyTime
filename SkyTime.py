#!/usr/bin/env python

import pygame
import gettext

from random import randint
from pygame import transform
from badges import badges
from pygame.locals import K_1, K_2, K_3, K_4, K_ESCAPE, K_RETURN,\
    K_LSHIFT, K_RSHIFT, K_BACKSPACE, QUIT, KEYDOWN, K_LEFT, K_RIGHT
from constants import width, height, clock_render_left, clock_render_top, \
    box_render_left, time_render_left, your_time_render_top, HANDS, \
    goal_time_render_top, CLOCK_REWARDS, REWARDS_DICT, BACKGROUND_REWARDS, \
    MENU_OPTIONS, REWARD_OPTIONS

# Declaring Variables
hour = 12
minute = 0
time = ''
goal_time = ''
playing = False
winner = False
gameloop = True
update_hands = False
update_screen = True
increment = 5
waited = 0
display_badge = 0
mode = 'language'
prev_mode = 'language'
reward_selected = 0
cur_reward_state = 'Clock Faces'
badge_awarded = None
sun_count = 0
incorrect_count = 0
text_color = (0, 0, 0)

hour_style = 'default'
minute_style = 'default'
center_style = 'default'
background_style = 'default'
clock_style = 'default'
box_style = 'default'
time_box_style = 'white'

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


def drawScreen(mode):

    # Only updates the player's screen if needed
    if update_screen:

        # Display the actual game screens (play and challenge)
        if playing:

            # Set the background
            background = pygame.image.load(
                'images/background/{}.png'.format(background_style))
            screen = transform.scale(background, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

            # Display the instructional box
            instructions = pygame.image.load(
                'images/instruction/box-{}.png'.format(box_style))
            windowSurfaceObj.blit(instructions, (0, height * .71))

            # Load time box image
            time_box = pygame.image.load(
                'images/box/{}.png'.format(time_box_style))

            # Load sun counter image
            sun = pygame.image.load('images/sun.png')
            windowSurfaceObj.blit(sun, (width * .6, height * .52))

            # Displays the players score
            windowSurfaceObj.blit(fontObj.render(
                str(sun_count), False, text_color),
                (width * .73, height * .575))

            if mode == 'challenge':
                # Displays your goal time
                windowSurfaceObj.blit(time_box,
                                     (box_render_left,
                                      goal_time_render_top + (height * .025)))
                windowSurfaceObj.blit(fontObj.render(
                    goal_time, False, text_color),
                    (time_render_left, goal_time_render_top + (height * .09)))
                windowSurfaceObj.blit(fontObj.render(
                    _('Goal Time'), False, text_color),
                    (box_render_left, goal_time_render_top))

            else:

                # Displays your goal time
                windowSurfaceObj.blit(time_box,
                                     (box_render_left,
                                      goal_time_render_top + (height * .025)))
                windowSurfaceObj.blit(fontObj.render(
                    goal_time, False, pygame.Color(0, 0, 0)),
                    (time_render_left, goal_time_render_top + (height * .09)))
                windowSurfaceObj.blit(fontObj.render(
                    _('Goal Time'), False, text_color),
                    (box_render_left, goal_time_render_top))

            # Displays help text
            text = challengeText.render(
                _('When you think the clock is correct, press'),
                False, pygame.Color(255, 255, 255))
            fw, fh = text.get_size()
            windowSurfaceObj.blit(text, (width * .44 - (fw / 2), height * .79))

            # Display help text at the bottom of the screen
            render_top = height * .92
            text = infoText.render(
                _('Hour Hand'), False, pygame.Color(0, 255, 0))
            text2 = infoText.render(
                _('= press'), False, pygame.Color(255, 255, 255))
            fw, fh = text.get_size()
            fw2, fh2 = text.get_size()
            windowSurfaceObj.blit(
                text, (width * .30 - ((fw + fw2) / 2), render_top))
            windowSurfaceObj.blit(
                text2, (width * .31 + (fw / 2) - (fw2 / 2), render_top))
            text = infoText.render(
                _('Minute Hand'), False, pygame.Color(255, 0, 0))
            text2 = infoText.render(
                _('= press'), False, pygame.Color(255, 255, 255))
            fw, fh = text.get_size()
            fw2, fh2 = text2.get_size()
            windowSurfaceObj.blit(
                text, (width * .75 - ((fw + fw2) / 2), render_top))
            windowSurfaceObj.blit(
                text2, (width * .76 + (fw / 2) - (fw2 / 2), render_top))

            # Display the enter button text
            text = enterButton.render(_('enter'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            windowSurfaceObj.blit(
                text, (width * .885 - (fw / 2), height * .82))

            # Display the shift button text
            text = shiftButton.render(_('shift'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            render_top = height * .925
            windowSurfaceObj.blit(text, (width * .445 - (fw / 2), render_top))
            windowSurfaceObj.blit(text, (width * .9375 - (fw / 2), render_top))

            # Display go back info
            back_info = infoText.render(_('Go Back'), False, text_color)
            fw, fh = back_info.get_size()
            windowSurfaceObj.blit(
                back_info,
                ((width * .85) - (fw / 2), (height * .025) - (fh / 2)))

        # Draw the menu screen
        elif mode == 'menu':
            render_left = width * .35
            interval = .18
            spacer = .22

            screen = pygame.image.load(
                'images/background/{}.png'.format(background_style))
            screen = transform.scale(screen, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

            for i in range(0, 4):

                # Display 'Play'
                text = menuText.render(_('Press'), False, text_color)
                fw, fh = text.get_size()
                windowSurfaceObj.blit(
                    text, (render_left - (fw / 2), height * spacer))

                # Display the button associated with the menu option
                button = pygame.image.load(
                    'images/buttons/{}.png'.format(i + 1))
                iw, ih = button.get_size()
                button_render_left = render_left + (fw / 2)
                windowSurfaceObj.blit(
                    button,
                    (button_render_left, (height * spacer) - (ih * .28)))

                # Display the menu option name
                option = menuText.render(_(MENU_OPTIONS[i]), False, text_color)
                fw, fh = option.get_size()
                windowSurfaceObj.blit(
                    option, (button_render_left + iw, (height * spacer)))

                spacer += interval

            # Display go back info
            back_info = infoText.render(_('Go Back'), False, text_color)
            fw, fh = back_info.get_size()
            windowSurfaceObj.blit(
                back_info,
                ((width * .85) - (fw / 2), (height * .025) - (fh / 2)))

        # Draw the rewards screen
        elif mode == 'rewards':

            # Display the screen
            background = pygame.image.load(
                'images/background/{}.png'.format(background_style))
            screen = transform.scale(background, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

            spacer = .2
            interval = .3
            counter = 1

            # Draw the different reward titles at the top
            for title in REWARD_OPTIONS:

                # Check what current state the user is in
                if title == cur_reward_state:
                    color = (255, 0, 0)
                else:
                    color = text_color

                title_text = infoText.render(_(title), False, color)
                fw, fh = title_text.get_size()

                render_left = (width * spacer) - (fw / 2)
                render_top = height * .09

                windowSurfaceObj.blit(
                    title_text, (render_left, render_top - (fh / 2)))

                num_tab = pygame.image.load(
                    'images/buttons/{}.png'.format(counter))
                iw, ih = num_tab.get_size()
                windowSurfaceObj.blit(
                    num_tab, (render_left - iw, render_top - (ih / 2)))

                spacer += interval
                counter += 1

            # User is looking at the clock face rewards
            if cur_reward_state == 'Clock Faces':
                rewards = CLOCK_REWARDS
                cur_state = 'clock'

            # User is looking at the background rewards
            elif cur_reward_state == 'Backgrounds':
                rewards = BACKGROUND_REWARDS
                cur_state = 'background'

            else:
                rewards = CLOCK_REWARDS
                cur_state = 'clock'

            counter = 0
            column = 0
            row = 0
            render_left = width * .12
            render_top = height * .32

            spacer_column = width * .25
            spacer_row = height * .4

            # Display all the different rewards for this category
            for reward in rewards:

                # Make sure this rewards exists
                if reward is not None:

                    # Load the image of the reward and scale it
                    reward_image = pygame.image.load(
                        'images/{}/{}.png'.format(cur_state, reward))
                    reward_image = transform.scale(
                        reward_image, (width/6, height/5))
                    rw, rh = reward_image.get_size()

                    # Check if the user has this reward selected
                    if counter == reward_selected:
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
                    windowSurfaceObj.blit(
                        border,
                        ((render_left + (column * spacer_column) - (bw / 2)),
                        (render_top + (row * spacer_row) - (bh / 2))))

                    # Display the reward image
                    windowSurfaceObj.blit(
                        reward_image,
                        ((render_left + (column * spacer_column) - (rw / 2)),
                        (render_top + (row * spacer_row) - (rh / 2))))

                    # Display the number of suns the reward costs
                    cost = infoText.render(
                        REWARDS_DICT[cur_state][reward]['value'],
                        False, text_color)
                    fw, fh = cost.get_size()
                    windowSurfaceObj.blit(
                        cost,
                        ((render_left + (column * spacer_column) - (fw / 2)),
                        (render_top +
                            (row * spacer_row) + (bh / 2) + (fh / 2))))

                    # Display the sun icon
                    windowSurfaceObj.blit(
                        sun,
                        ((render_left + (column * spacer_column) - (bw / 2)),
                        (render_top +
                            (row * spacer_row) + (bh / 2) - (sh / 9))))

                    if column == 3:
                        column = 0
                        row += 1

                    else:
                        column += 1

                    counter += 1

                # Temporary place holder for a reward that doesn't exist
                else:

                    # Check if the user has this reward selected
                    if counter == reward_selected:
                        border = pygame.image.load(
                            'images/rewards/selected.png')

                    else:
                        border = pygame.image.load(
                            'images/rewards/unearned.png')

                    border = transform.scale(border, (width/5, height/4))
                    bw, bh = border.get_size()

                    # Display the border
                    windowSurfaceObj.blit(
                        border,
                        ((render_left + (column * spacer_column) - (bw / 2)),
                        (render_top + (row * spacer_row) - (bh / 2))))

                    if column == 3:
                        column = 0
                        row += 1

                    else:
                        column += 1

                    counter += 1

            # Display go back info
            back_info = infoText.render(_('Go Back'), False, text_color)
            fw, fh = back_info.get_size()
            windowSurfaceObj.blit(
                back_info,
                ((width * .85) - (fw / 2), (height * .025) - (fh / 2)))

        # Draw the vicotry screen
        elif mode == 'victory':

            # Display the screen
            screen = transform.scale(victory, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

        # Draw the language selection screen
        elif mode == 'language':

            # Display the screen
            screen = transform.scale(Languages, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

        # Draw the how to play screen
        else:

            # Display the screen
            screen = transform.scale(HowToScreen, (width, height))
            windowSurfaceObj.blit(screen, (0, 0))

            text = howToPlay.render(
                _('How To Play'), False, pygame.Color(255, 255, 0))
            fw, fh = text.get_size()
            windowSurfaceObj.blit(
                text, ((width * .52) - (fw / 2), height * .05))

            text = fontObj.render(
                _('When you think it is correct, press'),
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

            text = helpText.render(
                _('Press this key'), False, pygame.Color(0, 0, 0))
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
            windowSurfaceObj.blit(
                text, (width * .78 - (fw / 2), height * .915))

            text = shiftButton.render(_('shift'), False, pygame.Color(0, 0, 0))
            fw, fh = text.get_size()
            render_top = height * .43

            windowSurfaceObj.blit(text, (width * .205 - (fw / 2), render_top))
            windowSurfaceObj.blit(text, (width * .755 - (fw / 2), render_top))

            # Display go back info
            back_info = infoText.render(_('Go Back'), False, text_color)
            fw, fh = back_info.get_size()
            windowSurfaceObj.blit(
                back_info,
                ((width * .85) - (fw / 2), (height * .025) - (fh / 2)))

    # Update the clock hands
    if update_hands:

            # Draw the clock
            clock = pygame.image.load(
                'images/clock/{}.png'.format(clock_style))
            windowSurfaceObj.blit(clock,
                                 (clock_render_left, clock_render_top))

            # Draw the clock hands
            windowSurfaceObj.blit(
                HANDS['minute'][minute]['image'],
                (HANDS['minute'][minute]['render_left'],
                 HANDS['minute'][minute]['render_top']))

            windowSurfaceObj.blit(
                HANDS['hour'][hour]['image'],
                (HANDS['hour'][hour]['render_left'],
                 HANDS['hour'][hour]['render_top']))

            # Draw the clock center
            screen = transform.scale(ClockCenter, (width/22, height/18))
            windowSurfaceObj.blit(screen,
                                  (clock_render_left + (width * .2275),
                                   clock_render_top + (height * .31)))

            # Only update the player's time if not playing challenge mode
            if mode == 'play':

                # Load time box image
                time_box = pygame.image.load(
                    'images/box/{}.png'.format(time_box_style))

                # Displays your time
                windowSurfaceObj.blit(time_box,
                                     (box_render_left,
                                      your_time_render_top + (height * .025)))
                windowSurfaceObj.blit(fontObj.render(
                    time, False, pygame.Color(0, 0, 0)),
                    (time_render_left,
                     your_time_render_top + (height * .09)))
                windowSurfaceObj.blit(fontObj.render(
                    _('Your Time'), False, text_color),
                    (box_render_left, your_time_render_top))


def loadHands():

    # Loads in the minute hand and creates an array with all of the angles
    minute_image = pygame.image.load(
        'images/hand/minute-{}.png'.format(minute_style))

    hour_image = pygame.image.load(
        'images/hand/hour-{}.png'.format(hour_style))

    for i in range(0, len(angles)):
        minute_hand = pygame.transform.rotate(minute_image, angles[i])
        hour_hand = pygame.transform.rotate(hour_image, angles[i])
        HANDS['minute'][i*increment]['image'] = minute_hand
        HANDS['hour'][i]['image'] = hour_hand


def displayBadge(image_name):

    # Location of the info text and badge
    render_top = height * .55
    render_left = width * .89

    # Display info text
    info = enterButton.render(
        _("You have earned badge:"),
        False, pygame.Color(0, 0, 0))
    fw, fh = info.get_size()
    windowSurfaceObj.blit(
        info, (render_left - (fw / 2), render_top - (fh / 2)))

    # Display badge name
    badge_name = enterButton.render(
        _('{}').format(image_name),
        False, pygame.Color(0, 0, 0))

    fw, fh = badge_name.get_size()
    windowSurfaceObj.blit(
        badge_name,
        (render_left - (fw / 2), render_top + (fh / 2)))

    # Load and scale the badge image
    badge_image = pygame.image.load('badges/{}.png'.format(image_name))
    badge_image = transform.scale(badge_image, (width/12, height/10))

    # Display the badge earned
    iw, ih = badge_image.get_size()
    windowSurfaceObj.blit(
        badge_image, (render_left - (iw / 2), render_top + (ih / 2)))

# Generates a new random time
hour = randint(1, 12)
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
angles = [0, -30, -60, -90, -120, -150, -180,
          -210, -240, -270, -300, -330]

# Loads all of the assets
MenuScreen = pygame.image.load('images/MenuScreen.gif')
HowToScreen = pygame.image.load('images/HowToScreen.gif')
ClockCenter = pygame.image.load(
    'images/clock_center/{}.png'.format(center_style))
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
    update_screen = False
    update_hands = False

    # Create a timer for displaying a badge recently earned
    if badge_awarded is not None and playing:
        display_badge += 1
        displayBadge(badge_awarded)

        if display_badge > 200:
            badge_awarded = None
            update_screen = True
            update_hands = True
            display_badge = 0

    # Checks if the player won the challenge
    if time == goal_time and winner:
        waited += 1

        if waited > 100:

            # Generates a new random time
            hour = randint(1, 12)
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
            update_screen = True
            update_hands = True
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

                # Play the game in English
                if event.key == K_1:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeEnglish'])
                    _ = lang.ugettext
                    mode = 'menu'
                    update_screen = True

                # Play the game in Spanish
                elif event.key == K_2:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeSpanish'])
                    _ = lang.ugettext
                    mode = 'menu'
                    update_screen = True

                # Play the game in French
                elif event.key == K_3:
                    lang = gettext.translation(
                        'org.laptop.SkyTime',
                        'locale/',
                        languages=['SkyTimeFrench'])
                    _ = lang.ugettext
                    infoText = pygame.font.Font('freesansbold.ttf', 22)
                    challengeText = pygame.font.Font('freesansbold.ttf', 34)
                    mode = 'menu'
                    update_screen = True

            # Check if the player is in the reward screen
            elif mode == 'rewards':

                # Display the clock face rewards
                if event.key == K_1:
                    cur_reward_state = 'Clock Faces'
                    reward_selected = 0
                    update_screen = True

                # Display the background rewards
                elif event.key == K_2:
                    cur_reward_state = 'Backgrounds'
                    reward_selected = 0
                    update_screen = True

                # Display the hand rewards
                elif event.key == K_3:
                    cur_reward_state = 'Hands'
                    reward_selected = 0
                    update_screen = True

                # Go back to the menu
                elif event.key == K_BACKSPACE:
                    mode = 'menu'
                    cur_reward_state = 'Clock Faces'
                    update_screen = True
                    update_hands = False
                    playing = False

                # The user selected a reward
                elif event.key == K_RETURN:

                    # Selected a clock face reward
                    if cur_reward_state == 'Clock Faces':
                        reward = REWARDS_DICT['clock'][
                            CLOCK_REWARDS[reward_selected]]

                        # Check if the user has already earned this reward
                        if reward['earned']:
                            clock_style = CLOCK_REWARDS[reward_selected]
                            update_screen = True

                        # Check if the user has enough for the reward
                        elif sun_count >= int(reward['value']):
                            sun_count -= int(reward['value'])
                            reward['earned'] = True
                            clock_style = CLOCK_REWARDS[reward_selected]
                            update_screen = True

                    # Selected a background reward
                    elif cur_reward_state == 'Backgrounds':
                        reward = REWARDS_DICT['background'][
                            BACKGROUND_REWARDS[reward_selected]]

                        # Check if the use has already earned this reward
                        if reward['earned']:
                            background_style = BACKGROUND_REWARDS[
                                reward_selected]
                            text_color = REWARDS_DICT['background'][
                                background_style]['color']
                            update_screen = True

                        # Check if the user has enough for the reward
                        elif sun_count >= int(reward['value']):
                            sun_count -= int(reward['value'])
                            reward['earned'] = True
                            background_style = BACKGROUND_REWARDS[
                                reward_selected]
                            text_color = REWARDS_DICT['background'][
                                background_style]['color']
                            update_screen = True

                # Move cursor to the left
                elif event.key == K_LEFT:
                    if cur_reward_state == 'Clock Faces':
                        if reward_selected == 0:
                            reward_selected = len(CLOCK_REWARDS) - 1
                        else:
                            reward_selected -= 1

                    elif cur_reward_state == 'Backgrounds':
                        if reward_selected == 0:
                            reward_selected = len(BACKGROUND_REWARDS) - 1
                        else:
                            reward_selected -= 1

                    update_screen = True

                # Move cursor to the right
                elif event.key == K_RIGHT:
                    if cur_reward_state == 'Clock Faces':
                        if reward_selected == (len(CLOCK_REWARDS) - 1):
                            reward_selected = 0
                        else:
                            reward_selected += 1

                    if cur_reward_state == 'Backgrounds':
                        if reward_selected == (len(BACKGROUND_REWARDS) - 1):
                            reward_selected = 0
                        else:
                            reward_selected += 1

                    update_screen = True

            # Check what mode the player has selected
            elif mode == 'menu':
                # Draw the play screen
                if event.key == K_1:
                    mode = 'play'
                    update_screen = True
                    update_hands = True
                    loadHands()
                    playing = True

                # Draw the challenge screen
                elif event.key == K_2:
                    mode = 'challenge'
                    update_screen = True
                    update_hands = True
                    loadHands()
                    playing = True

                # Draw How To Play
                elif event.key == K_3:
                    mode = 'howtoplay'
                    update_screen = True
                    update_hands = False
                    playing = False

                # Draw Rewards Screen
                elif event.key == K_4:
                    mode = 'rewards'
                    update_screen = True
                    update_hands = False
                    playing = False

                # Go back to language select
                elif event.key == K_BACKSPACE:
                    mode = 'language'
                    update_screen = True
                    update_hands = False
                    playing = False

            elif mode == 'howtoplay':

                # Go back to the menu
                if event.key == K_BACKSPACE:
                    mode = 'menu'
                    update_screen = True
                    update_hands = False
                    playing = False

            # Check if the user is playing the game
            if playing:

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
                    update_hands = True

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
                    update_hands = True

                # Go back to the menu
                elif event.key == K_BACKSPACE:
                    mode = 'menu'
                    update_screen = True
                    update_hands = False
                    playing = False

            # Check if the player has the correct time
            if event.key == K_RETURN:
                if time == goal_time and playing:
                    prev_mode = mode
                    playing = False
                    winner = True
                    sun_count += 1

                    # Award badges
                    if sun_count == 1:
                        badges.award('Hair Past a Freckle',
                                     'Completed your first time')
                        badge_awarded = 'Hair Past a Freckle'

                        if mode == 'challenge':
                            badges.award('Challenge Complete',
                                         'Completed your first challenge time')
                            badge_awarded = 'Challenge Complete'

                    if sun_count == 5:
                        badges.award('First Five',
                                     'Obtained your first five suns')
                        badge_awarded = 'First Five'

                    if sun_count == 100:
                        badges.award('ChronoKeeper',
                                     'Obtained 100 suns')
                        badge_awarded = 'ChronoKeeper'

                    mode = 'victory'
                    update_screen = True

                elif playing:
                    if incorrect_count == 2:
                        badges.award('Rainy Day',
                                     'Answered incorrectly 3 times in a row')
                        badge_awarded = 'Rainy Day'

                    incorrect_count += 1

            # Quit the game
            if event.key == K_ESCAPE:
                gameloop = False

    if gameloop:
        pygame.display.update()
