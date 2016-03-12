from abc import ABCMeta, abstractmethod


class PkgMgr:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass
