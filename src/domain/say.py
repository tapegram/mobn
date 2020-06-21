from subprocess import Popen, PIPE, STDOUT


class VoiceEffect(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def run(self):
        process = Popen(["say {}".format(self.phrase)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
        output, _ = process.communicate()
        return output


def say(phrase):
    return VoiceEffect(phrase)
