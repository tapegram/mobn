def add_to_team(new_member, config):
    new_config = config.copy()
    new_config["team_members"] = new_config["team_members"] + [new_member]
    return new_config
