from src.domain.git import create_branch


def new(workstream):
    return [
        create_branch(workstream),
    ]
