class VM:
    def __init__(self, virtualizer, uid):
        self.virtualizer = virtualizer
        self.uid = uid

    def start(self):
        self.virtualizer.start_vm(self.uid)

    def stop(self):
        self.virtualizer.stop_vm(self.uid)

    def get_status(self):
        return self.virtualizer.get_vm_status(self.uid)

    def get_ssh_info(self, ssh_port):
        return self.virtualizer.get_ssh_info(self.uid, ssh_port)

    def enable_ssh(self, host_ip, host_port, guest_port):
        return self.virtualizer.enable_ssh(self.uid, host_ip, host_port, guest_port)

    def update(self, username, password):
        # return self.pkgmgr.update(self.virtualizer, self.uid, username, password)
        raise NotImplementedError()
