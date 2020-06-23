from subprocess import Popen, PIPE


class GitEffect(object):
    def __init__(self, command):
        self.command = command

    def run(self):
        print(self.command)
        process = Popen([self.command], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, errput = process.communicate()
        print(output.decode("utf-8"))
        print(errput.decode("utf-8"))
        return output


def branch():
    return GitEffect("git branch")


def stash():
    return GitEffect("git stash --include-untracked")


def create_branch(name):
    return GitEffect("git checkout -b {}".format(name))


def delete_branch(name, force=False):
    if force:
        return GitEffect("git branch -D {}".format(name))
    else:
        return GitEffect("git branch -d {}".format(name))


def delete_remote_branch(name):
    return GitEffect("git push origin :{}".format(name))


def add_all():
    return GitEffect("git add .")


def add(path):
    return GitEffect("git add {}".format(path))


def commit_all(message="wip"):
    return GitEffect("git commit -m \"{}\"".format(message))


def push_origin_upstream(branch_name):
    return GitEffect("git push -u origin {}".format(branch_name))


def checkout(branch):
    return GitEffect("git checkout {}".format(branch))


def pull():
    return GitEffect("git pull origin")
