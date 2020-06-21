def select_next_mobber(config):
    team = config["team_members"]
    next_mobber = None
    if team:
        next_mobber = team[config["turn"]]
    return next_mobber
