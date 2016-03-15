from paramiko import SSHClient, AutoAddPolicy


class Channel:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.ssh = SSHClient()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ssh.close()

    def connect(self, username, password):
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(self.ip, port=self.port, username=username, password=password)

    def run(self, command):
        return self.ssh.exec_command(command)
