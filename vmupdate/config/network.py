"""
    Provide a wrapper around the network configuration section.
"""

from .configsection import ConfigSection


class Network(ConfigSection):
    """Provide a wrapper around the network configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Network`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Network`
        """

        super(Network, self).__init__(data)

        self._ssh = Ssh(self._data['SSH'])

    @property
    def ssh(self):
        """
            Return the `SSH` configuration section.

            :rtype: :class:`Ssh`
        """

        return self._ssh


class Ssh(ConfigSection):
    """Provide a wrapper around the SSH configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Ssh`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Ssh`
        """

        super(Ssh, self).__init__(data)

    @property
    def guest_port(self):
        """
            Return the guest port configuration.

            :rtype: int
        """

        return self['Guest']['Port']

    @property
    def host_min_port(self):
        """
            Return the host port minimum configuration.

            :rtype: int
        """

        return self['Host']['Ports']['Min']

    @property
    def host_max_port(self):
        """
            Return the host port maximum configuration, else 65,535.

            :rtype: int
        """

        return self['Host']['Ports'].get('Max', 65535)
