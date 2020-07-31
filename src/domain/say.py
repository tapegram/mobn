from subprocess import Popen, PIPE, STDOUT

import os
print()

class VoiceEffect(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def run(self):
        voice = os.environ['MOBN_VOICE'] or "Daniel"
        process = Popen(["say -v {} {}".format(voice, self.phrase)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
        output, _ = process.communicate()
        return output


def say(phrase):
    return VoiceEffect(phrase)
