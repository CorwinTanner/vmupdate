"""
    Provide a wrapper around the credentials configuration section.
"""

from .configsection import ConfigSection


class Credentials(ConfigSection):
    """Provide a wrapper around the credentials configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`Credentials`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`Credentials`
        """

        super(Credentials, self).__init__(data)

    @property
    def username(self):
        """
            Return the `Username` configuration.

            :rtype: str
        """

        return self.get('Username')

    @property
    def password(self):
        """
            Return the `Password` configuration.

            :rtype: str
        """

        return self.get('Password')

    @property
    def use_keyring(self):
        """
            Return the `Use Keyring` configuration.

            :rtype: bool
        """

        return self.get('Use Keyring', False)

    @property
    def run_as_elevated(self):
        """
            Return the `Run As Elevated` configuration.

            :rtype: bool
        """

        return self.get('Run As Elevated', False)
