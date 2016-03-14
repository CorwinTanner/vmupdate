from .pkgmgr import PkgMgr


class Apt(PkgMgr):
    NAME = 'apt-get'

    def __init__(self, path):
        self.path = path

    def update(self, virtualizer, uuid, username, password):
        exitcode = virtualizer.run(uuid, self.path, username, password, ['update', '-y', '-u', '-q'])

        if exitcode != 0:
            return exitcode

        return virtualizer.run(uuid, self.path, username, password, ['upgrade', '-y', '-u', '-q'])