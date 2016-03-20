import logging

from config import config
from credentials import get_credentials, get_run_as_elevated

log = logging.getLogger(__name__)


def get_pkgmgrs(vm):
    pkgmgrs = []
    vm_os = vm.get_os()

    log.info('Querying package managers for %s with OS %s', vm.uid, vm_os)

    if vm_os in config.pkgmgrs:
        with vm.connect() as shell:
            for pkgmgr, cmds in config.pkgmgrs[vm_os].items():
                log.debug('Checking if %s exists on %s', pkgmgr, vm.uid)
                if shell.command_exists(pkgmgr):
                    pkgmgrs.append((pkgmgr, cmds))

    return pkgmgrs


def run_pkgmgr(vm, pkgmgr, cmds):
    log.info('Updating %s on %s', pkgmgr, vm.uid)

    with vm.connect() as shell:
        for cmd in cmds:
            stdin, stdout, stderr = run_pkgmgr_cmd(vm, shell, pkgmgr, cmd)

            exitcode = stdout.channel.recv_exit_status()

            if exitcode != 0:
                return exitcode

    return 0


def run_pkgmgr_cmd(vm, shell, pkgmgr, cmd):
    shell_cmd = ' '.join([pkgmgr, cmd])

    log.debug('Running %s on %s', shell_cmd, vm.uid)

    if get_run_as_elevated(vm.uid):
        username, password = get_credentials(vm.uid)

        return shell.run_as_elevated(shell_cmd, password)

    return shell.run(shell_cmd)
