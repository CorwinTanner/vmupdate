"""
    Provide a base class for configuration sections.
"""

class ConfigSection(object):
    """
        Provide a base class for configuration sections.

        This class wraps a :class:`dict`.
    """

    def __init__(self, data=None):
        """
            Return an instance of :class:`ConfigSection`.

            :param dict data: the data for the config section

            :rtype:`ConfigSection`
        """

        self._data = data or {}

    def __getitem__(self, key):
        """Return the value for ``key``, else ``None``."""

        return self._data.get(key)

    def __contains__(self, key):
        """Return ``True`` if the config section contains ``key``, else ``False``."""

        return key in self._data

    def __iter__(self):
        """Return an iterator over the keys of the config section."""

        return iter(self._data)

    def __len__(self):
        """Return the number of items in the config section."""

        return len(self._data)

    def get(self, key, default=None):
        """Return the value for ``key``, else ``default``."""

        return self._data.get(key, default)

    def items(self):
        """Return a copy of the config section's list of (key, value) pairs."""

        return self._data.items()

    def iteritems(self):
        """Return an iterator over the config section's (key, value) pairs."""

        return self._data.iteritems()

    def iterkeys(self):
        """Return an iterator over the config section's keys."""

        return self._data.iterkeys()

    def itervalues(self):
        """Return an iterator over the config section's values."""

        return self._data.itervalues()

    def keys(self):
        """Return a copy of the config section's list of keys."""

        return self._data.keys()

    def values(self):
        """Return a copy of the config section's list of values."""

        return self._data.values()
