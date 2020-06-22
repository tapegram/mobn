from src.domain.git import (
    add_all,
    checkout,
    commit_all,
    create_branch,
    delete_branch,
    delete_remote_branch,
    pull,
    push_origin_upstream,
)
from src.domain.output import output


def finish(workstream, branchName):
    return [
        output("pushing everything..."),
        add_all(),
        commit_all(),
        push_origin_upstream(workstream),

        # Create PR
        output("putting it all on {}".format(branchName)),
        create_branch(branchName),
        push_origin_upstream(branchName),

        # todo, create a PR here

        # cleanup
        output("cleaning up..."),
        checkout("master"),
        delete_branch(workstream, force=True),
        delete_remote_branch(workstream),
        pull(),

        output("ready to open PR!"),
    ]
