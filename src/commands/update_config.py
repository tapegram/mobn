from src.domain.git import add, commit, push_origin_upstream


def update_config(workstream, config_path):
    return [
        add(config_path),
        commit(config_path, "updating config"),
        push_origin_upstream(workstream)
    ]
