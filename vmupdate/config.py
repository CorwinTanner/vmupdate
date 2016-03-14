import pkgutil
import yaml


def load_config():
    return yaml.load(pkgutil.get_data('vmupdate', 'config/vmupdate.yaml'))
