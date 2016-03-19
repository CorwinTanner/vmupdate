from config import config
from credentials import get_credentials, get_run_as_elevated


def get_pkgmgrs(vm):
    pkgmgrs = []
    vm_os = vm.get_os()

    if vm_os in config.pkgmgrs:
        with vm.connect() as shell:
            for pkgmgr, cmds in config.pkgmgrs[vm_os].items():
                if shell.command_exists(pkgmgr):
                    pkgmgrs.append((pkgmgr, cmds))

    return pkgmgrs


def run_pkgmgr(vm, pkgmgr, cmds):
    with vm.connect() as shell:
        for cmd in cmds:
            stdin, stdout, stderr = run_pkgmgr_cmd(vm, shell, pkgmgr, cmd)

            exitcode = stdout.channel.recv_exit_status()

            if exitcode != 0:
                return exitcode

    return 0


def run_pkgmgr_cmd(vm, shell, pkgmgr, cmd):
    shell_cmd = ' '.join([pkgmgr, cmd])

    if get_run_as_elevated(vm.uid):
        username, password = get_credentials(vm.uid)

        return shell.run_as_elevated(shell_cmd, password)

    return shell.run(shell_cmd)
