import os
import platform

from config import config


def find_virtualizers():
    virtualizer = {}

    for name, paths in config.virtualizers[platform.system()].items():
        for path in paths:
            path = os.path.expandvars(path)

            if os.path.isfile(path):
                virtualizer[name] = path

    return virtualizer
