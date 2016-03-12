import pkgutil
import yaml


def load_config(config_path=None):
    config = yaml.load(pkgutil.get_data('vmupdate', 'config/vmupdate.yaml'))

    if config_path:
        with open(config_path, 'r') as config_file:
            config.extend(yaml.load(config_file))

    return config
