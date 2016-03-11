import os
import re
import subprocess

from .virtualizer import Virtualizer, VM_UNKNOWN, VM_STOPPED, VM_RUNNING, VM_SUSPENDED, VM_PAUSED


class VirtualBox(Virtualizer):

    def __init__(self, manager_path=None):
        self.manager_path = manager_path

    def list_vms(self):
        cmd = subprocess.Popen([self.manager_path, 'list', 'vms'], stdout=subprocess.PIPE)

        vms = []

        stdoutdata, stderrdata = cmd.communicate()

        if stdoutdata:
            matches = re.finditer(r"""^"(?P<name>[^"]+)"\s+\{(?P<uuid>[^}]+)\}""",
                                  stdoutdata,
                                  flags=re.IGNORECASE | re.MULTILINE)

            if matches:
                for match in matches:
                    vms.append((match.group('uuid'), match.group('name')))

        return vms

    def start_vm(self, uuid):
        cmd = subprocess.Popen([self.manager_path, 'startvm', uuid, '--type', 'headless'])

        return cmd.wait()

    def get_vm_status(self, uuid):
        cmd = subprocess.Popen([self.manager_path, 'showvminfo', uuid], stdout=subprocess.PIPE)

        stdoutdata, stderrdata = cmd.communicate()

        if stdoutdata:
            match = re.search(r"""^State:\s*(?P<state>[a-z\s]*)""", stdoutdata, flags=re.IGNORECASE | re.MULTILINE)

            if match:
                state = match.group('state').strip()

                if state == 'powered off':
                    return VM_STOPPED
                elif state == 'running':
                    return VM_RUNNING
                elif state == 'saved':
                    return VM_SUSPENDED
                elif state == 'paused':
                    return VM_PAUSED

        return VM_UNKNOWN

    def set_vm_status(self, uuid, status):
        raise NotImplementedError()

    def run(self, uuid, path, executable, username, password, args):
        # guestcontrol {UUID} run --username {username} --password {password} --exe {path} -- {executable} {args}
        raise NotImplementedError()
