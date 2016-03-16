from .shell import Shell


class Posix(Shell):
    def __init__(self, channel):
        self.channel = channel

    def command_exists(self, command):
        stdin, stdout, stderr = self.channel.run(['command', '-v', command])

        return stdout.channel.recv_exit_status() == 0
