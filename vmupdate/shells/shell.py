"""
    Provide an abstract base class for shells.
"""

from abc import ABCMeta, abstractmethod


class Shell(object):
    """
        Abstract virtual machine shell that communicates through a channel.

        This class must be inherited and cannot be used directly.

        :ivar channel: channel used for virtual machine communication
        :vartype channel: :class:`~vmupdate.channel.Channel`
    """

    __metaclass__ = ABCMeta

    def __enter__(self):
        """
            Return instance of :class:`Shell`.

            :rtype:`Shell`
        """

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close channel and release resources."""

        self.close()

    def run(self, args):
        """
            Run command against the virtual machine.

            :param args: the command to be run
            :type args: str or list

            :rtype: :class:`~vmupdate.channel.ChannelCommand`
        """

        return self.channel.run(args)

    def close(self):
        """Close channel and release resources."""

        if self.channel:
            self.channel.close()

    @abstractmethod
    def command_exists(self, command):
        """
            Return whether the ``command`` exists in the shell.

            This is a shell-specific command and must be overridden.

            :param str command: name of the command

            :rtype: bool
        """

        pass

    @abstractmethod
    def run_as_elevated(self, args, password):
        """
            Run command against the virtual machine as an elevated user.

            This is a shell-specific command and must be overridden.

            :param args: the command to be run
            :param str password: password to be used for elevated authentication
            :type args: str or list

            :rtype: :class:`~vmupdate.channel.ChannelCommand`
        """

        pass
