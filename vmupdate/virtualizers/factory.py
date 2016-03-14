import sys

from virtualbox import VirtualBox


def get_virtualizer(name, path):
    v_class = getattr(sys.modules[__name__], name)

    return v_class(path)
