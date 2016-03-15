from abc import ABCMeta, abstractmethod


class Shell:
    __metaclass__ = ABCMeta

    @abstractmethod
    def command_exists(self, command):
        pass
