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

NUMBERS_HIT_BOX = {
    0: {
        'render_left': width * .245,
        'render_top': height * .165,
        'width': 50,
        'height': 100
    },
    1: {
        'render_left': width * .31,
        'render_top': height * .2,
        'width': 50,
        'height': 100
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

JARGON = {
    '0': {
        '0': ['Twelve o\' clock', 'Noon', 'Midnight'],
        '5': ['Five past twelve', 'Five after twelve'],
        '10': ['Ten past twelve', 'Ten after twelve'],
        '15': ['Quarter past twelve', 'Quarter after twelve'],
        '20': ['Twenty past twelve', 'Twenty after twelve'],
        '25': ['Twenty-fve past twelve', 'Twenty-five after twelve'],
        '30': ['Half past twelve'],
        '35': ['Twenty-five of one', 'Twenty-five before one'],
        '40': ['Twenty of one', 'Twenty before one'],
        '45': ['Quarter of one', 'Quarter before one'],
        '50': ['Ten of one', 'Ten before one'],
        '55': ['Five of one', 'Five before one']
    },
    '1': {
        '0': ['One o\' clock'],
        '5': ['Five past one', 'Five after one'],
        '10': ['Ten past one', 'Ten after one'],
        '15': ['Quarter past one', 'Quarter after one'],
        '20': ['Twenty past one', 'Twenty after one'],
        '25': ['Twenty-fve past one', 'Twenty-five after one'],
        '30': ['Half past one'],
        '35': ['Twenty-five of two', 'Twenty-five before two'],
        '40': ['Twenty of two', 'Twenty before two'],
        '45': ['Quarter of two', 'Quarter before two'],
        '50': ['Ten of two', 'Ten before two'],
        '55': ['Five of two', 'Five before two']
    },
    '2': {
        '0': ['Two o\' clock'],
        '5': ['Five past two', 'Five after two'],
        '10': ['Ten past two', 'Ten after two'],
        '15': ['Quarter past two', 'Quarter after two'],
        '20': ['Twenty past two', 'Twenty after two'],
        '25': ['Twenty-fve past two', 'Twenty-five after two'],
        '30': ['Half past two'],
        '35': ['Twenty-five of three', 'Twenty-five before three'],
        '40': ['Twenty of three', 'Twenty before three'],
        '45': ['Quarter of three', 'Quarter before three'],
        '50': ['Ten of three', 'Ten before three'],
        '55': ['Five of three', 'Five before three']
    },
    '3': {
        '0': ['Three o\' clock'],
        '5': ['Five past three', 'Five after three'],
        '10': ['Ten past three', 'Ten after three'],
        '15': ['Quarter past three', 'Quarter after three'],
        '20': ['Twenty past three', 'Twenty after three'],
        '25': ['Twenty-fve past three', 'Twenty-five after three'],
        '30': ['Half past three'],
        '35': ['Twenty-five of four', 'Twenty-five before four'],
        '40': ['Twenty of four', 'Twenty before four'],
        '45': ['Quarter of four', 'Quarter before four'],
        '50': ['Ten of four', 'Ten before four'],
        '55': ['Five of four', 'Five before four']
    },
    '4': {
        '0': ['Four o\' clock'],
        '5': ['Five past four', 'Five after four'],
        '10': ['Ten past four', 'Ten after four'],
        '15': ['Quarter past four', 'Quarter after four'],
        '20': ['Twenty past four', 'Twenty after four'],
        '25': ['Twenty-fve past four', 'Twenty-five after four'],
        '30': ['Half past four'],
        '35': ['Twenty-five of five', 'Twenty-five before five'],
        '40': ['Twenty of five', 'Twenty before five'],
        '45': ['Quarter of five', 'Quarter before five'],
        '50': ['Ten of five', 'Ten before five'],
        '55': ['Five of five', 'Five before five']
    },
    '5': {
        '0': ['Five o\' clock'],
        '5': ['Five past five', 'Five after five'],
        '10': ['Ten past five', 'Ten after five'],
        '15': ['Quarter past five', 'Quarter after five'],
        '20': ['Twenty past five', 'Twenty after five'],
        '25': ['Twenty-fve past five', 'Twenty-five after five'],
        '30': ['Half past five'],
        '35': ['Twenty-five of six', 'Twenty-five before six'],
        '40': ['Twenty of six', 'Twenty before six'],
        '45': ['Quarter of six', 'Quarter before six'],
        '50': ['Ten of six', 'Ten before six'],
        '55': ['Five of six', 'Five before six']
    },
    '6': {
        '0': ['Six o\' clock'],
        '5': ['Five past six', 'Five after six'],
        '10': ['Ten past six', 'Ten after six'],
        '15': ['Quarter past six', 'Quarter after six'],
        '20': ['Twenty past six', 'Twenty after six'],
        '25': ['Twenty-fve past six', 'Twenty-five after six'],
        '30': ['Half past six'],
        '35': ['Twenty-five of seven', 'Twenty-five before seven'],
        '40': ['Twenty of seven', 'Twenty before seven'],
        '45': ['Quarter of seven', 'Quarter before seven'],
        '50': ['Ten of seven', 'Ten before seven'],
        '55': ['Five of seven', 'Five before seven']
    },
    '7': {
        '0': ['Seven o\' clock'],
        '5': ['Five past seven', 'Five after seven'],
        '10': ['Ten past seven', 'Ten after seven'],
        '15': ['Quarter past seven', 'Quarter after seven'],
        '20': ['Twenty past seven', 'Twenty after seven'],
        '25': ['Twenty-fve past seven', 'Twenty-five after seven'],
        '30': ['Half past seven'],
        '35': ['Twenty-five of eight', 'Twenty-five before eight'],
        '40': ['Twenty of eight', 'Twenty before eight'],
        '45': ['Quarter of eight', 'Quarter before eight'],
        '50': ['Ten of eight', 'Ten before eight'],
        '55': ['Five of eight', 'Five before eight']
    },
    '8': {
        '0': ['Eight o\' clock'],
        '5': ['Five past eight', 'Five after eight'],
        '10': ['Ten past eight', 'Ten after eight'],
        '15': ['Quarter past eight', 'Quarter after eight'],
        '20': ['Twenty past eight', 'Twenty after eight'],
        '25': ['Twenty-fve past eight', 'Twenty-five after eight'],
        '30': ['Half past eight'],
        '35': ['Twenty-five of nine', 'Twenty-five before nine'],
        '40': ['Twenty of nine', 'Twenty before nine'],
        '45': ['Quarter of nine', 'Quarter before nine'],
        '50': ['Ten of nine', 'Ten before nine'],
        '55': ['Five of nine', 'Five before nine']
    },
    '9': {
        '0': ['Nine o\' clock'],
        '5': ['Five past nine', 'Five after nine'],
        '10': ['Ten past nine', 'Ten after nine'],
        '15': ['Quarter past nine', 'Quarter after nine'],
        '20': ['Twenty past nine', 'Twenty after nine'],
        '25': ['Twenty-fve past nine', 'Twenty-five after nine'],
        '30': ['Half past nine'],
        '35': ['Twenty-five of ten', 'Twenty-five before ten'],
        '40': ['Twenty of ten', 'Twenty before ten'],
        '45': ['Quarter of ten', 'Quarter before ten'],
        '50': ['Ten of ten', 'Ten before ten'],
        '55': ['Five of ten', 'Five before ten']
    },
    '10': {
        '0': ['Ten o\' clock'],
        '5': ['Five past ten', 'Five after ten'],
        '10': ['Ten past ten', 'Ten after ten'],
        '15': ['Quarter ten', 'Quarter after ten'],
        '20': ['Twenty past ten', 'Twenty after ten'],
        '25': ['Twenty-fve past ten', 'Twenty-five after ten'],
        '30': ['Half past ten'],
        '35': ['Twenty-five of eleven', 'Twenty-five before eleven'],
        '40': ['Twenty of eleven', 'Twenty before eleven'],
        '45': ['Quarter of eleven', 'Quarter before eleven'],
        '50': ['Ten of eleven', 'Ten before eleven'],
        '55': ['Five of eleven', 'Five before eleven']
    },
    '11': {
        '0': ['Eleven o\' clock'],
        '5': ['Five past eleven', 'Five after eleven'],
        '10': ['Ten past eleven', 'Ten after eleven'],
        '15': ['Quarter eleven', 'Quarter after eleven'],
        '20': ['Twenty past eleven', 'Twenty after eleven'],
        '25': ['Twenty-fve past eleven', 'Twenty-five after eleven'],
        '30': ['Half past eleven'],
        '35': ['Twenty-five of twelve', 'Twenty-five before twelve'],
        '40': ['Twenty of twelve', 'Twenty before twelve'],
        '45': ['Quarter of twelve', 'Quarter before twelve'],
        '50': ['Ten of twelve', 'Ten before twelve'],
        '55': ['Five of twelve', 'Five before twelve']
    }
}
