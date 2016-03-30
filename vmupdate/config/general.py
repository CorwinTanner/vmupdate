"""
    Provide a wrapper around the general configuration section.
"""

from .configsection import ConfigSection


class General(ConfigSection):
    """Provide a wrapper around the general configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`General`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`General`
        """

        super(General, self).__init__(data)

    @property
    def wait_after_start(self):
        """
            Return the `Wait After Start` configuration.

            :rtype: int
        """

        return self['Wait After Start']

    @property
    def wait_before_stop(self):
        """
            Return the `Wait Before Stop` configuration.

            :rtype: int
        """

        return self['Wait Before Stop']
