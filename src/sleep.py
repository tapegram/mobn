import time

class SleepEffect(object):
    def __init__(self, length):
        self.length = length

    def run(self):
        time.sleep(self.length)


def sleep(length):
    return SleepEffect(length)
