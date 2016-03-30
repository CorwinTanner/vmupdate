"""
    Provide a wrapper around the virtualizers configuration section.
"""

from .configsection import ConfigSection


class Virtualizers(ConfigSection):
    """Provide a wrapper around the virtualizers configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Virtualizers`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Virtualizers`
        """

        super(Virtualizers, self).__init__(data)
