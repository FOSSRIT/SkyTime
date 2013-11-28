width = 1200
height = 850

clock_render_left = width * .015
clock_render_top = height * .01

box_render_left = width * .55
time_render_left = box_render_left + (width * .185)
your_time_render_top = height * .05
goal_time_render_top = height * .285

REWARD_OPTIONS = ['Clock Faces', 'Backgrounds']

MENU_OPTIONS = ['Play', 'Challenge', 'How To Play', 'Rewards']

CLOCK_REWARDS = ['default', 'green', 'moon', 'purple',
                 'watermelon', 'spikeysun', 'earth', 'bluemoon']

BACKGROUND_REWARDS = ['default', 'night-cloudy', 'night-clear',
                      'rainbow', 'sunset', 'rain', 'galaxy', 'northern-lights']

REWARDS_DICT = {
    'clock': {
        'default': {
            'name': 'default',
            'earned': True,
            'value': '0',
            'color': (0, 0, 0)
        },
        'green': {
            'name': 'green',
            'earned': False,
            'value': '15',
            'color': (0, 0, 0)
        },
        'moon': {
            'name': 'moon',
            'earned': False,
            'value': '30',
            'color': (0, 0, 0)
        },
        'purple': {
            'name': 'purple',
            'earned': False,
            'value': '75',
            'color': (0, 0, 0)
        },
        'watermelon': {
            'name': 'watermelon',
            'earned': False,
            'value': '120',
            'color': (0, 0, 0)
        },
        'spikeysun': {
            'name': 'spikeysun',
            'earned': False,
            'value': '175',
            'color': (0, 0, 0)
        },
        'bluemoon': {
            'name': 'bluemoon',
            'earned': False,
            'value': '300',
            'color': (0, 0, 0)
        },
        'earth': {
            'name': 'earth',
            'earned': False,
            'value': '225',
            'color': (0, 0, 0)
        }
    },
    'background': {
        'default': {
            'name': 'default',
            'earned': True,
            'value': '0',
            'color': (0, 0, 0)
        },
        'night-cloudy': {
            'name': 'night-cloudy',
            'earned': False,
            'value': '15',
            'color': (255, 255, 255)
        },
        'night-clear': {
            'name': 'night-clear',
            'earned': False,
            'value': '30',
            'color': (255, 255, 255)
        },
        'rainbow': {
            'name': 'rainbow',
            'earned': False,
            'value': '75',
            'color': (0, 0, 0)
        },
        'sunset': {
            'name': 'sunset',
            'earned': False,
            'value': '125',
            'color': (0, 0, 0)
        },
        'rain': {
            'name': 'rain',
            'earned': False,
            'value': '175',
            'color': (0, 0, 0)
        },
        'northern-lights': {
            'name': 'northern-lights',
            'earned': False,
            'value': '300',
            'color': (255, 255, 255)
        },
        'galaxy': {
            'name': 'galaxy',
            'earned': False,
            'value': '225',
            'color': (255, 255, 255)
        }
    },
    'score': '0',
    'number_clocks': 0,
    'number_backgrounds': 0
}

HANDS = {
    'minute': {
        0: {
            'image': None,
            'render_left': clock_render_left + (width * .23),
            'render_top': clock_render_top + (height * .13)
        },
        5: {
            'image': None,
            'render_left': clock_render_left + (width * .23),
            'render_top': clock_render_top + (height * .145)
        },
        10: {
            'image': None,
            'render_left': clock_render_left + (width * .23),
            'render_top': clock_render_top + (height * .215)
        },
        15: {
            'image': None,
            'render_left': clock_render_left + (width * .24),
            'render_top': clock_render_top + (height * .31)
        },
        20: {
            'image': None,
            'render_left': clock_render_left + (width * .2425),
            'render_top': clock_render_top + (height * .31)
        },
        25: {
            'image': None,
            'render_left': clock_render_left + (width * .225),
            'render_top': clock_render_top + (height * .305)
        },
        30: {
            'image': None,
            'render_left': clock_render_left + (width * .23),
            'render_top': clock_render_top + (height * .33)
        },
        35: {
            'image': None,
            'render_left': clock_render_left + (width * .162),
            'render_top': clock_render_top + (height * .32)
        },
        40: {
            'image': None,
            'render_left': clock_render_left + (width * .12),
            'render_top': clock_render_top + (height * .3)
        },
        45: {
            'image': None,
            'render_left': clock_render_left + (width * .105),
            'render_top': clock_render_top + (height * .313)
        },
        50: {
            'image': None,
            'render_left': clock_render_left + (width * .12),
            'render_top': clock_render_top + (height * .213)
        },
        55: {
            'image': None,
            'render_left': clock_render_left + (width * .16),
            'render_top': clock_render_top + (height * .15)
        }
    },
    'hour': {
        0: {
            'image': None,
            'render_left': clock_render_left + (width * .2325),
            'render_top': clock_render_top + (height * .19)
        },
        1: {
            'image': None,
            'render_left': clock_render_left + (width * .24),
            'render_top': clock_render_top + (height * .2)
        },
        2: {
            'image': None,
            'render_left': clock_render_left + (width * .245),
            'render_top': clock_render_top + (height * .25)
        },
        3: {
            'image': None,
            'render_left': clock_render_left + (width * .26),
            'render_top': clock_render_top + (height * .3135)
        },
        4: {
            'image': None,
            'render_left': clock_render_left + (width * .245),
            'render_top': clock_render_top + (height * .325)
        },
        5: {
            'image': None,
            'render_left': clock_render_left + (width * .235),
            'render_top': clock_render_top + (height * .325)
        },
        6: {
            'image': None,
            'render_left': clock_render_left + (width * .23),
            'render_top': clock_render_top + (height * .34)
        },
        7: {
            'image': None,
            'render_left': clock_render_left + (width * .185),
            'render_top': clock_render_top + (height * .33)
        },
        8: {
            'image': None,
            'render_left': clock_render_left + (width * .145),
            'render_top': clock_render_top + (height * .31)
        },
        9: {
            'image': None,
            'render_left': clock_render_left + (width * .145),
            'render_top': clock_render_top + (height * .31)
        },
        10: {
            'image': None,
            'render_left': clock_render_left + (width * .15),
            'render_top': clock_render_top + (height * .235)
        },
        11: {
            'image': None,
            'render_left': clock_render_left + (width * .18),
            'render_top': clock_render_top + (height * .2)
        }
    }
}

NUMBERS = {
    0: {
        'render_left': width * .235,
        'render_top': height * .06
    },
    1: {
        'render_left': width * .325,
        'render_top': height * .1
    },
    2: {
        'render_left': width * .38,
        'render_top': height * .19
    },
    3: {
        'render_left': width * .41,
        'render_top': height * .31
    },
    4: {
        'render_left': width * .385,
        'render_top': height * .44
    },
    5: {
        'render_left': width * .325,
        'render_top': height * .53
    },
    6: {
        'render_left': width * .235,
        'render_top': height * .57
    },
    7: {
        'render_left': width * .14,
        'render_top': height * .53
    },
    8: {
        'render_left': width * .075,
        'render_top': height * .44
    },
    9: {
        'render_left': width * .05,
        'render_top': height * .31
    },
    10: {
        'render_left': width * .075,
        'render_top': height * .19
    },
    11: {
        'render_left': width * .14,
        'render_top': height * .1
    }
}
