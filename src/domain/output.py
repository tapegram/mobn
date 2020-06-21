class OutputEffect(object):
    def __init__(self, message):
        self.message = message

    def run(self):
        print(self.message)


def output(message):
    return OutputEffect(message)
