width = 1200
height = 875

clock_render_left = width * .015
clock_render_top = height * .01

box_render_left = width * .55
time_render_left = box_render_left + (width * .185)
your_time_render_top = height * .05
goal_time_render_top = height * .285

CLOCK_REWARDS = ['default', 'green', 'moon', None,
                 'watermelon', None, None, 'bluemoon']

BACKGROUND_REWARDS = ['default', 'night1', 'night2', 'night3',
                      None, None, None, None]

REWARDS_DICT = {
    'clock': {
        'default': {
            'earned': True,
            'value': '0',
            'color': (0, 0, 0)
        },
        'green': {
            'earned': False,
            'value': '15',
            'color': (0, 0, 0)
        },
        'moon': {
            'earned': False,
            'value': '30',
            'color': (0, 0, 0)
        },
        'watermelon': {
            'earned': False,
            'value': '120',
            'color': (0, 0, 0)
        },
        'bluemoon': {
            'earned': False,
            'value': '300',
            'color': (0, 0, 0)
        },
        None: {
            'earned': False,
            'value': '10000',
            'color': (0, 0, 0)
        }
    },
    'background': {
        'default': {
            'earned': True,
            'value': '0',
            'color': (0, 0, 0)
        },
        'night1': {
            'earned': False,
            'value': '15',
            'color': (255, 255, 255)
        },
        'night2': {
            'earned': False,
            'value': '30',
            'color': (255, 255, 255)
        },
        'night3': {
            'earned': False,
            'value': '120',
            'color': (255, 255, 255)
        },
        None: {
            'earned': False,
            'value': '10000',
            'color': (0, 0, 0)
        }
    }

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
            'render_left': clock_render_left + (width * .25),
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
