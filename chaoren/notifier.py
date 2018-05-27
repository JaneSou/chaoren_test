# -*- coding: utf-8-*-
from __future__ import absolute_import

import atexit
import logging
import sys
import time

from apscheduler.schedulers.background import BackgroundScheduler

from . import app_utils

if sys.version_info < (3, 0):
    import Queue as queue  # Python 2
else:
    import queue  # Python 3


class Notifier(object):

    class NotificationClient(object):

        def __init__(self, gather, timestamp):
            self.gather = gather
            self.timestamp = timestamp

        def run(self):
            self.timestamp = self.gather(self.timestamp)

    def __init__(self, profile, brain):
        self._logger = logging.getLogger(__name__)
        self.q = queue.Queue()
        self.profile = profile
        self.notifiers = []
        self.brain = brain

        sched = BackgroundScheduler(daemon=True)
        sched.start()
        sched.add_job(self.gather, 'interval', seconds=120)
        atexit.register(lambda: sched.shutdown(wait=False))

    def gather(self):
        [client.run() for client in self.notifiers]

    def handleRemenderNotifications(self, lastDate):
        lastDate = time.strftime('%d %b %Y %H:%M:%S')
        due_reminders = app_utils.get_due_reminders()
        for reminder in due_reminders:
            self.q.put(reminder)

        return lastDate

    def getNotification(self):
        """Returns a notification. Note that this function is consuming."""
        try:
            notif = self.q.get(block=False)
            return notif
        except queue.Empty:
            return None

    def getAllNotifications(self):
        """
            Return a list of notifications in chronological order.
            Note that this function is consuming, so consecutive calls
            will yield different results.
        """
        notifs = []

        notif = self.getNotification()
        while notif:
            notifs.append(notif)
            notif = self.getNotification()

        return notifs
