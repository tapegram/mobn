import os
import json


class GetEnvironmentVariableEffect(object):
    def __init__(self, key):
        self.key = key

    def run(self):
        return os.getenv(self.key)


MOBN_WORKSTREAM_NAME = "MOBN_WORKSTREAM_NAME"


def get_workstream_name():
    return GetEnvironmentVariableEffect(MOBN_WORKSTREAM_NAME)


DEFAULT_CONFIG = dict(
    team_members=[],
    turn=0,
)


class GetConfigEffect(object):
    def __init__(self, path):
        self.path = path

    def run(self):
        if not os.path.exists(self.path):
            return DEFAULT_CONFIG

        with open(self.path) as config_file:
            return json.load(config_file)


def get_config(path_to_config):
    return GetConfigEffect(path_to_config)


class SetConfigEffect(object):
    def __init__(self, path, config):
        self.path = path
        self.config = config

    def run(self):
        with open(self.path, "w+") as config_file:
            json.dump(
                self.config,
                config_file,
                indent=4
            )


def set_config(path_to_config, config):
    return SetConfigEffect(
        path=path_to_config,
        config=config,
    )
