import logging.config
import pkgutil

import yaml

from configsection import ConfigSection
from credentials import Credentials
from general import General
from machines import Machines
from network import Network
from pkgmgrs import PackageManagers
from shells import Shells
from virtualizers import Virtualizers


class Config(ConfigSection):
    @property
    def general(self):
        return self._general

    @property
    def credentials(self):
        return self._credentials

    @property
    def network(self):
        return self._network

    @property
    def virtualizers(self):
        return self._virtualizers

    @property
    def pkgmgrs(self):
        return self._pkgmgrs

    @property
    def shells(self):
        return self._shells

    @property
    def machines(self):
        return self._machines

    def load(self):
        self._config = yaml.load(pkgutil.get_data('vmupdate', 'data/vmupdate.yaml'))

        self._general = General(self._config['General'])
        self._credentials = Credentials(self._config['Credentials'])
        self._network = Network(self._config['Network'])
        self._virtualizers = Virtualizers(self._config['Virtualizers'])
        self._pkgmgrs = PackageManagers(self._config['Package Managers'])
        self._shells = Shells(self._config['Shells'])
        self._machines = Machines(self._config['Machines'])

        self._logging = yaml.load(pkgutil.get_data('vmupdate', 'data/logging.yaml'))

        logging.config.dictConfig(self._logging)


config = Config()
