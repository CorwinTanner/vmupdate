from abc import ABCMeta, abstractmethod


class Virtualizer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list_vms(self):
        pass

    @abstractmethod
    def start_vm(self, uid):
        pass

    @abstractmethod
    def stop_vm(self, uid):
        pass

    @abstractmethod
    def get_vm_status(self, uid):
        pass

    @abstractmethod
    def get_vm_os(self, uid):
        pass

    @abstractmethod
    def run(self, uid, executable, username, password, args=None):
        pass
