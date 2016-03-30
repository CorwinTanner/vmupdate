"""
    Provide a method for instantiating virtualizers by name.
"""

import sys

from .virtualbox import VirtualBox


def get_virtualizer(name, path):
    """
        Return an instance of a virtualizer.

        The virtualizer should extend :class:`~.virtualizer.Virtualizer`.

        :param str name: name of the virtualizer class to instantiate
        :param str path: path of the virtualizer to pass to the constructor
    """

    virtualizer_class = getattr(sys.modules[__name__], name)

    return virtualizer_class(path)
