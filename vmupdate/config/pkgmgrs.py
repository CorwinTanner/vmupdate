"""
    Provide a wrapper around the package managers configuration section.
"""

from .configsection import ConfigSection


class PackageManagers(ConfigSection):
    """Provide a wrapper around the package managers configuration section."""

    def __init__(self, data):
        """
            Return an instance of :class:`PackageManagers`.

            This method extends :meth:`~ConfigSection.__init__`.

            :param dict data: the data for the config section

            :rtype:`PackageManagers`
        """

        super(PackageManagers, self).__init__(data)
