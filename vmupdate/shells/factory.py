"""
    Provide a method for instantiating shells by name.
"""

import sys

from .posix import Posix


def get_shell(name, channel):
    """
        Return an instance of a shell.

        The shell should extend :class:`~.shell.Shell`.

        :param str name: name of the shell class to instantiate
        :param channel: channel instance to pass to the constructor
        :type channel: :class:`~vmupdate.channel.Channel`
    """

    shell_class = getattr(sys.modules[__name__], name)

    return shell_class(channel)
