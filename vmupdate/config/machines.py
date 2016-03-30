"""
    Provide a wrapper around the machines configuration section.
"""

from .configsection import ConfigSection


class Machines(ConfigSection):
    """
        Provide a wrapper around the machines configuration section.

        This class wraps a dict of :class:`Machine`.
    """

    def __init__(self, data):
        """
            Return an instance of :class:`Machines`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Machines`
        """

        self._data = {}

        if data:
            for name, machine_data in data.iteritems():
                self._data[name] = Machine(machine_data)


class Machine(ConfigSection):
    """Provide a wrapper around the machine configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Machine`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Machine`
        """

        super(Machine, self).__init__(data)

    @property
    def username(self):
        """
            Return the `username` configuration.

            :rtype: str
        """

        return self.get('Username')

    @property
    def password(self):
        """
            Return the `password` configuration.

            :rtype: str
        """

        return self.get('Password')

    @property
    def use_keyring(self):
        """
            Return the `use keyring` configuration.

            :rtype: bool
        """

        return self.get('Use Keyring')

    @property
    def run_as_elevated(self):
        """
            Return the `run as elevated` configuration.

            :rtype: bool
        """

        return self.get('Run As Elevated')

    @property
    def shell(self):
        """
            Return the `shell` configuration.

            :rtype: str
        """

        return self.get('Shell')
