"""
    Provide an abstract base class for virtualizers.
"""

from abc import ABCMeta, abstractmethod


class Virtualizer(object):
    """
        Abstract virtualizer control.

        This class must be inherited and cannot be used directly.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def list_vms(self):
        """
            Return all virtual machines.

            This is a virtualizer-specific command and must be overridden.

            :return: list of tuple (name, id)
            :rtype: list(str, str)
        """

        pass

    @abstractmethod
    def start_vm(self, uid):
        """
            Start the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            :param str uid: identifier of the machine

            :return: exitcode
            :rtype: int
        """

        pass

    @abstractmethod
    def stop_vm(self, uid):
        """
            Stop the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            :param str uid: identifier of the machine

            :return: exitcode
            :rtype: int
        """

        pass

    @abstractmethod
    def get_vm_status(self, uid):
        """
            Return the status of the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            Possible values can be found in :mod:`.virtualizers.constants`.

            :param str uid: identifier of the machine

            :rtype: str
        """

        pass

    @abstractmethod
    def get_vm_os(self, uid):
        """
            Return the operating system of the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            Possible values can be found in :mod:`.virtualizers.constants`.

            :param str uid: identifier of the machine

            :rtype: str
        """

        pass

    @abstractmethod
    def get_ssh_info(self, uid, ssh_port):
        """
            Return the SSH connection information for the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            :param str uid: identifier of the machine

            :return: tuple of (hostname, port)
            :rtype: (str, int)
        """

        pass

    @abstractmethod
    def enable_ssh(self, uid, host_port, guest_port):
        """
            Enable SSH port forwarding for the virtual machine.

            This is a virtualizer-specific command and must be overridden.

            :param str uid: identifier of the machine
            :param int host_port: the post on the host to forward to the guest
            :param int guest_port: SSH port of the guest

            :return: exitcode
            :rtype: int
        """

        pass
