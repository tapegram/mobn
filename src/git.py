from subprocess import Popen, PIPE


def branch():
    process = Popen(['git branch'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
    return output

def create_branch(name):
    process = Popen(['git checkout -b {}'.format(name)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def delete_branch(name):
    process = Popen(['git branch -D {}'.format(name)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
    return output

def add_all():
    process = Popen(['git add .'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def commit_all(message="wip"):
    process = Popen(['git commit -m {}'.format(message)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def push_all():
    process = Popen(['git push origin'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def push_origin_upstream(branch_name):
    process = Popen(['git push -u origin {}'.format(branch_name)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def checkout(branch):
    process = Popen(['git checkout {}'.format(branch)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()

def pull():
    process = Popen(['git pull origin'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
