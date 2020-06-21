def set_team(team_members, config):
    new_config = config.copy()
    new_config["team_members"] = team_members
    return new_config
