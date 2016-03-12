from abc import ABCMeta, abstractmethod


class Virtualizer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list_vms(self):
        pass

    @abstractmethod
    def start_vm(self, uuid):
        pass

    @abstractmethod
    def stop_vm(self, uuid):
        pass

    @abstractmethod
    def get_vm_status(self, uuid):
        pass

    @abstractmethod
    def get_vm_os(self, uuid):
        pass

    @abstractmethod
    def run(self, uuid, executable, username, password, args=None):
        pass
