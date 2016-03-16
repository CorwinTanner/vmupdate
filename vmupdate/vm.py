import platform

from channel import Channel
from config import config
from credentials import get_credentials
from shells import get_shell


class VM:
    def __init__(self, virtualizer, uid):
        self.virtualizer = virtualizer
        self.uid = uid

    def start(self):
        self.virtualizer.start_vm(self.uid)

    def stop(self):
        self.virtualizer.stop_vm(self.uid)

    def get_status(self):
        return self.virtualizer.get_vm_status(self.uid)

    def get_os(self):
        return self.virtualizer.get_vm_os(self.uid)

    def get_ssh_info(self, ssh_port):
        return self.virtualizer.get_ssh_info(self.uid, ssh_port)

    def enable_ssh(self, host_port, guest_port):
        return self.virtualizer.enable_ssh(self.uid, host_port, guest_port)

    def connect(self, ssh_port):
        ip, port = self.get_ssh_info(ssh_port)

        channel = Channel(ip, port)

        username, password = get_credentials(self.uid)

        channel.connect(username, password)

        return get_shell(self.get_shell_name(), channel)

    def get_shell_name(self):
        if self.uid in config.machines and 'Shell' in config.machines[self.uid]:
            return config.machines[self.uid]['Shell']

        return config.shells.get(self.virtualizer.get_vm_os(self.uid))
