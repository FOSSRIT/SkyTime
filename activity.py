#!/usr/bin/env python
from sugar3.activity.activity import Activity
from SkyTime import SkyTime


class SkyTimeActivity(Activity):

    def __init__(self, handle):
        print "running activity init", handle
        Activity.__init__(self, handle)
        print "activity running"

        SkyTime()
