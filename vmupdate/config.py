import pkgutil
import yaml


class Config:
    def __init__(self):
        self._config = None

    def load(self):
        self._config = yaml.load(pkgutil.get_data('vmupdate', 'config/vmupdate.yaml'))

    def __getitem__(self, key):
        return self._config[key]


config = Config()
