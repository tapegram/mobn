from subprocess import Popen, PIPE


class GitEffect(object):
    def __init__(self, command):
        self.command = command

    def run(self):
        process = Popen([self.command], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
        output, _ = process.communicate()
        return output


def branch():
    return GitEffect("git branch")


def create_branch(name):
    return GitEffect("git checkout -b {}".format(name))


def delete_branch(name):
    return GitEffect("git branch -D {}".format(name))


def add_all():
    return GitEffect("git add .")


def commit_all(message="wip"):
    return GitEffect("git comit -m {}".format(message))


def push_all():
    return GitEffect("git push origin")


def push_origin_upstream(branch_name):
    return GitEffect("git push -u origin {}".format(branch_name))


def checkout(branch):
    return GitEffect("git checkout {}".format(branch))


def pull():
    return GitEffect("git pull origin")
