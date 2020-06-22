from src.domain.git import create_branch, checkout, pull, delete_branch, delete_remote_branch


def new(workstream):
    return [
        checkout("master"),
        pull(),
        delete_branch(workstream, force=True),
        delete_remote_branch(workstream),
        create_branch(workstream),
    ]
