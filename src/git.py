from subprocess import Popen, PIPE


class GitEffect(object):
    def __init__(self, command):
        self.command = command

    def run(self):
        print(self.command)
        process = Popen([self.command], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
        output, _ = process.communicate()
        print(output.decode("utf-8"))
        return output


def branch():
    return GitEffect("git branch")


def create_branch(name):
    return GitEffect("git checkout -b {}".format(name))


def delete_branch(name):
    return GitEffect("git branch -d {}".format(name))


def add_all():
    return GitEffect("git add .")


def commit_all(message="wip"):
    return GitEffect("git commit -m \"{}\"".format(message))


def push_origin_upstream(branch_name):
    return GitEffect("git push -u origin {}".format(branch_name))


def checkout(branch):
    return GitEffect("git checkout {}".format(branch))


def pull():
    return GitEffect("git pull origin")
