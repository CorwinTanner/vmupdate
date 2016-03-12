class VM:
    def __init__(self, virtualizer, pkgmgr, uuid, username, password):
        self.virtualizer = virtualizer
        self.pkgmgr = pkgmgr
        self.uuid = uuid
        self.username = username
        self.password = password

    def start(self):
        self.virtualizer.start_vm(self.uuid)

    def stop(self):
        self.virtualizer.stop_vm(self.uuid)

    def get_status(self):
        return self.virtualizer.get_vm_status(self.uuid)

    def update(self):
        return self.pkgmgr.update(self.virtualizer, self.uuid, self.username, self.password)
