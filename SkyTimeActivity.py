#!/usr/bin/env python

from gettext import gettext as _

import sys
from gi.repository import Gtk

import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

sys.path.append('..')
import sugargame.canvas

import SkyTime


class SkyTimeActivity(sugar3.activity.activity.Activity):

    def __init__(self, handle):
        super(SkyTimeActivity, self).__init__(handle)

        self.paused = False

        # Create the game instance
        self.game = SkyTime.SkyTime(self.get_bundle_id())

        # Build the activity toolbar
        self.build_toolbar()

        # Build the Pygame canvas
        self.canvas = sugargame.canvas.PygameCanvas(self)

        self.set_canvas(self.canvas)
        self.canvas.grab_focus()

        self.canvas.run_pygame(self.game.run)

    def build_toolbar(self):

        # Create the toolbar box
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # Create the activity button
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        # Create the pause/play button
        stop_play = ToolButton('media-playback-stop')
        stop_play.set_tooltip(_("Stop"))
        stop_play.set_accelerator(_('<ctrl>space'))
        stop_play.connect('clicked', self.stop_play_cb)
        stop_play.show()

        toolbar_box.toolbar.insert(stop_play, -1)

        # Create a blank separator and a Stop button
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

    def stop_play_cb(self, button):
        # Pause or unpause the game
        self.paused = not self.paused
        self.game.set_paused(self.paused)

        # Update the button to show the next action
        if self.paused:
            button.set_icon('media-playback-start')
            button.set_tooltip(_("Start"))
        else:
            button.set_icon('media-playback-stop')
            button.set_tooltip(_("Stop"))
