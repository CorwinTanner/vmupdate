import sys
import time

from config import config
from host import get_all_vms
from pkgmgr import get_pkgmgrs, run_pkgmgr
from virtualizers import VM_STOPPED


def main():
    config.load()

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


if __name__ == '__main__':
    sys.exit(main())
