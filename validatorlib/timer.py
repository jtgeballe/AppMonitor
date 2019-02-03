"""The RepeatTimer type executes code on a calculated cadence."""
from threading import Timer


class RepeatTimer:

    def __init__(self, interval, function):
        self.__interval = interval
        self.__function = function
        self.__timer = self._create_timer()

    def _run(self):
        """Execute this code every time the timer expires."""
        self.__function()
        self.__timer = self._create_timer()
        self.__timer.start()

    def _create_timer(self):
        """Calculate the new time interval and set the timer."""
        next_interval = self.__interval()
        return Timer(next_interval, self._run)

    def start(self):
        self.__timer.start()

    def cancel(self):
        self.__timer.cancel()
