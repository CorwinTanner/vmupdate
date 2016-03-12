from .pkgmgr import PkgMgr


class Apt(PkgMgr):

    def __init__(self, virt):
        self.virt = virt

    def update(self):
        raise NotImplementedError()
