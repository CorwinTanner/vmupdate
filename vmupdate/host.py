import os
import platform
import time

from config import config
from virtualizers import get_virtualizer, VM_STOPPED
from pkgmgr import get_pkgmgrs, run_pkgmgr
from vm import VM


def upate_all_vms():
    for vm in get_all_vms():
        vm_orig_status = vm.get_status()

        if vm_orig_status == VM_STOPPED:
            vm.start()
            time.sleep(config.general.wait_after_start)

        for pkgmgr, cmds in get_pkgmgrs(vm):
            run_pkgmgr(vm, pkgmgr, cmds)

        if vm_orig_status == VM_STOPPED:
            vm.stop()

    return 0


def get_all_vms():
    vms = []

    virtualizers = find_virtualizers()

    available_ports = iter(get_available_ports(vms))

    for virt_name, virt_path in virtualizers.items():
        virtualizer = get_virtualizer(virt_name, virt_path)

        for vm_name, vm_uuid in virtualizer.list_vms():
            vm = VM(virtualizer, vm_name)

            ssh_info = vm.get_ssh_info()

            if not ssh_info and vm.get_status() == VM_STOPPED:
                vm.enable_ssh(next(available_ports))

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

    min_port = config.network.ssh.host_min_port
    max_port = config.network.ssh.host_max_port

    return [p for p in xrange(min_port, max_port) if p not in used_ports]


def get_used_ports(vms):
    used_ports = set()

    for vm in vms:
        ssh_info = vm.get_ssh_info()

        if ssh_info:
            used_ports.add(ssh_info[1])

    return used_ports
