from abc import ABCMeta, abstractmethod


class Virtualizer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list_vms(self):
        pass

    @abstractmethod
    def start_vm(self, id):
        pass

    @abstractmethod
    def run(self, id, path, executable, username, password, args):
        pass
