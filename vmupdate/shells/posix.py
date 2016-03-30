"""
    Provide class to wrap a POSIX shell.
"""

import shlex

from .shell import Shell


class Posix(Shell):
    """
        Represent a POSIX shell that communicates through a channel.

        :ivar channel: channel used for virtual machine communication
        :vartype channel: :class:`~vmupdate.channel.Channel`
    """

    def __init__(self, channel):
        """
            Return an instance of :class:`Posix`.

            :param channel: channel used for virtual machine communication
            :type channel: :class:`~vmupdate.channel.Channel`

            :rtype:`Posix`
        """

        self.channel = channel

    def command_exists(self, command):
        """
            Return whether the ``command`` exists in the shell.

            :param str command: name of the command

            :rtype: bool
        """

        cmd = self.run(['command', '-v', command])

        return cmd.wait() == 0

    def run_as_elevated(self, args, password):
        """
            Run command against the virtual machine as an elevated user.

            :param args: the command to be run
            :param str password: password to be used for elevated authentication
            :type args: str or list

            :rtype: :class:`~vmupdate.channel.ChannelCommand`
        """

        if isinstance(args, basestring):
            args = shlex.split(args)

        elevated_args = ['sudo', '-S']
        elevated_args.extend(args)

        cmd = self.run(elevated_args)

        cmd.stdin.write(password)
        cmd.stdin.write('\n')
        cmd.stdin.flush()

        return cmd
