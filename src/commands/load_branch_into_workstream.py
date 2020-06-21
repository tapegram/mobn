from src.domain.git import push_origin_upstream, create_branch, checkout, delete_branch, pull
from src.domain.output import output


def load_branch_into_workstream(workstream, branchName):
    return [
        checkout("master"),
        pull(),
        delete_branch(workstream, force=True),

        checkout(branchName),
        create_branch(workstream),
        push_origin_upstream(workstream),
        output("branch {} loaded onto workstream".format(branchName))
    ]
