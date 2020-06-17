from subprocess import Popen, PIPE, STDOUT

def branch():
    process = Popen(['git branch'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
    print(str(output.decode("utf-8")))

def create_branch(name):
    process = Popen(['git checkout -b {}'.format(name)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
    print(str(output.decode("utf-8")))

def say(phrase):
    process = Popen(['say {}'.format(phrase)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
    output, _ = process.communicate()
    print(str(output.decode("utf-8")))


if __name__ == '__main__':
    say("huhuhuhuhuhuhuhuh")
#
# def push(self):
#     """git push"""
#     if self.git_exec:
#         process = Popen([self.git_exec, ' git push'], stdin=PIPE, stdout=PIPE, stderr=STDOUT, )
#     else:
#         process = Popen(['git push'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, )
#     output, _ = process.communicate()
#     return str("Push completed.{}".format(str(output.decode("utf-8"))))
