def increment_turn(config):
    new_config = config.copy()

    if len(new_config["team_members"]) == 0:
        return new_config

    new_config["turn"] = (new_config.get("turn", 0) + 1) % len(new_config["team_members"])
    return new_config
