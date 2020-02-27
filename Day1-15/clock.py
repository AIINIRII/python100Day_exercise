from time import sleep


class Clock(object):
    """"Number Clock"""

    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def now(self):
        return "%02d:%02d:%02d" % \
               (self._hours, self._minutes, self._seconds)

    def run(self):
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1
            if self._minutes == 60:
                self._minutes = 0
                self._hours += 1
                if self._hours == 24:
                    self._hours = 0


if __name__ == '__main__':
    clock = Clock()
    while True:
        sleep(0.1)
        clock.run()
        print(clock.now())
