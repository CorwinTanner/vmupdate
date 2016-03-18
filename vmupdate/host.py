import os
import platform

from config import config
from virtualizers import get_virtualizer, VM_STOPPED
from vm import VM


def get_all_vms():
    vms = []

    guest_ssh_port = config.network['SSH']['Guest']['Port']

    virtualizers = find_virtualizers()

    available_ports = iter(get_available_ports(vms))

    for virt_name, virt_path in virtualizers.items():
        virtualizer = get_virtualizer(virt_name, virt_path)

        for vm_name, vm_uuid in virtualizer.list_vms():
            vm = VM(virtualizer, vm_name)

            ssh_info = vm.get_ssh_info(guest_ssh_port)

            if not ssh_info and vm.get_status() == VM_STOPPED:
                vm.enable_ssh(next(available_ports), guest_ssh_port)

            vms.append(vm)

    return vms


def find_virtualizers():
    virtualizer = {}

    for name, paths in config.virtualizers[platform.system()].items():
        for path in paths:
            path = os.path.expandvars(path)

            if os.path.isfile(path):
                virtualizer[name] = path

    return virtualizer


def get_available_ports(vms):
    used_ports = get_used_ports(vms)

    min_port, max_port = get_port_range()

    return [p for p in xrange(min_port, max_port) if p not in used_ports]


def get_used_ports(vms):
    used_ports = set()

    guest_ssh_port = config.network['SSH']['Guest']['Port']

    for vm in vms:
        ssh_info = vm.get_ssh_info(guest_ssh_port)

        if ssh_info:
            used_ports.add(ssh_info[1])

    return used_ports

def get_port_range():
    min_port = config.network['SSH']['Host']['Ports']['Min']
    max_port = config.network['SSH']['Host']['Ports'].get('Max', 65535)

    return min_port, max_port
