"""
    Provide a wrapper around the shells configuration section.
"""

from .configsection import ConfigSection


class Shells(ConfigSection):
    """Provide a wrapper around the shells configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Shells`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Shells`
        """

        super(Shells, self).__init__(data)
