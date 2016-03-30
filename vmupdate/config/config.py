"""
    Provide a wrapper around configuration.
"""

import logging.config
import os
import pkgutil

import yaml

from vmupdate import BASE_DIR

from .configsection import ConfigSection
from .credentials import Credentials
from .general import General
from .machines import Machines
from .network import Network
from .pkgmgrs import PackageManagers
from .shells import Shells
from .virtualizers import Virtualizers


class Config(ConfigSection):
    """Provide a wrapper for the merged configuration files."""

    @property
    def general(self):
        """
            Return the `General` configuration section.

            :rtype: :class:`~.general.General`
        """

        return self._general

    @property
    def credentials(self):
        """
            Return the `Credentials` configuration section.

            :rtype: :class:`~.credentials.Credentials`
        """

        return self._credentials

    @property
    def network(self):
        """
            Return the `Network` configuration section.

            :rtype: :class:`~.network.Network`
        """

        return self._network

    @property
    def virtualizers(self):
        """
            Return the `Virtualizers` configuration section.

            :rtype: :class:`~.virtualizers.Virtualizers`
        """

        return self._virtualizers

    @property
    def pkgmgrs(self):
        """
            Return the `Package Managers` configuration section.

            :rtype: :class:`~.pkgmgrs.PackageManagers`
        """

        return self._pkgmgrs

    @property
    def shells(self):
        """
            Return the `Shells` configuration section.

            :rtype: :class:`~.shells.Shells`
        """

        return self._shells

    @property
    def machines(self):
        """
            Return the `Machines` configuration section.

            :rtype: :class:`~.machines.Machines`
        """

        return self._machines

    def load(self, config_path=None, log_dir=None):
        """
            Load the configuration files and configure logging.

            :param str config_path: path to a user defined configuration file
            :param str log_dir: path to the directory where log files are to be stored
        """

        default_config = yaml.load(pkgutil.get_data('vmupdate', 'data/vmupdate.yaml'))

        if config_path:
            with open(config_path, 'r') as config_file:
                user_config = yaml.load(config_file)

            self._data = _merge(default_config, user_config)
        else:
            self._data = default_config

        self._general = General(self._data['General'])
        self._credentials = Credentials(self._data['Credentials'])
        self._network = Network(self._data['Network'])
        self._virtualizers = Virtualizers(self._data['Virtualizers'])
        self._pkgmgrs = PackageManagers(self._data['Package Managers'])
        self._shells = Shells(self._data['Shells'])
        self._machines = Machines(self._data['Machines'])

        self._logging = yaml.load(pkgutil.get_data('vmupdate', 'data/logging.yaml'))

        if not log_dir:
            log_dir = BASE_DIR

        self._set_log_filename(log_dir, 'info_file')
        self._set_log_filename(log_dir, 'error_file')

        logging.config.dictConfig(self._logging)

    def _set_log_filename(self, log_dir, handler_name):
        """
            Update the log handler to write to the specified directory.

            :param str log_dir: path to the directory where log files are to be stored
            :param str handler_name: name of the log handler to update
        """

        if handler_name in self._logging['handlers']:
            self._logging['handlers'][handler_name]['filename'] =\
                os.path.join(log_dir, self._logging['handlers'][handler_name]['filename'])


def _merge(a, b):
    """
        Return the merge of two dictionaries.

        :param dict a: dictionary to merge into
        :param dict b: dictionary to merge

        :rtype: dict
    """

    if b is None:
        return a

    if isinstance(a, dict):
        for key in b:
            if key in a:
                a[key] = _merge(a[key], b[key])
            else:
                a[key] = b[key]
    else:
        a = b

    return a


config = Config()
