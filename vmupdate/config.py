import pkgutil

import yaml


class Config:
    def __init__(self):
        self._config = None

    def __getitem__(self, key):
        return self._config[key]

    @property
    def general(self):
        return self._config['General'] or {}

    @property
    def machines(self):
        return self._config['Machines'] or {}

    @property
    def virtualizers(self):
        return self._config['Virtualizers'] or {}

    def load(self):
        self._config = yaml.load(pkgutil.get_data('vmupdate', 'config/vmupdate.yaml'))


config = Config()
