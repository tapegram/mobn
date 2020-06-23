def remove_from_team(member, config):
    new_config = config.copy()
    new_config["team_members"] = [m for m in new_config["team_members"] if m != member]
    return new_config
