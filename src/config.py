import os
from subprocess import Popen, PIPE


class GetEnvironmentVariableEffect(object):
    def __init__(self, key):
        self.key = key

    def run(self):
        return os.getenv(self.key)


MOBN_WORKSTREAM_NAME = "MOBN_WORKSTREAM_NAME"


def get_workstream_name():
    return GetEnvironmentVariableEffect(MOBN_WORKSTREAM_NAME)
