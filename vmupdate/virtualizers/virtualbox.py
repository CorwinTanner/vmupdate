import os
import re
import subprocess

from .virtualizer import Virtualizer


class VirtualBox(Virtualizer):

    def __init__(self, manager_path=None):
        self.manager_path = manager_path

    def list_vms(self):
        cmd = subprocess.Popen([self.manager_path, 'list', 'vms'], stdout=subprocess.PIPE)

        vms = []

        stdout, stderr = cmd.communicate()

        if stdout:
            matches = re.finditer(r"""^"(?P<name>[^"]+)"\s+\{(?P<id>[^}]+)\}""", stdout, flags=re.IGNORECASE | re.MULTILINE)

            if matches:
                for match in matches:
                    vms.append((match.group('id'),
                                match.group('name')))

        return vms

    def start_vm(self, id):
        # startvm {UUID} --type headless
        # must wait for startup
        raise NotImplementedError()

    def run(self, id, path, executable, username, password, args):
        # guestcontrol {UUID} run --username {username} --password {password} --exe {path} -- {executable} {args}
        raise NotImplementedError()
