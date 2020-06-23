import random


def shuffle_order(config):
    new_config = config.copy()
    # Shuffle is in place for some reason
    random.shuffle(new_config["team_members"])
    return new_config
