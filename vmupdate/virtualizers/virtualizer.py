from abc import ABCMeta, abstractmethod

VM_UNKNOWN = -1
VM_STOPPED = 0
VM_RUNNING = 1
VM_SUSPENDED = 2
VM_PAUSED = 3


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
    def run(self, uuid, executable, username, password, args=None):
        pass
