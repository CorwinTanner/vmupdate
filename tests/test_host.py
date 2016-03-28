import mock

from vmupdate.config import config
from vmupdate.host import update_all_vms
from vmupdate.virtualizers import VM_STOPPED

from tests.case import TestCase
from tests.constants import *
from tests.context import get_data_path
from tests.mocks import get_mock_virtualizer, get_mock_ssh_client


class HostTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        config.load(get_data_path('testconfig.yaml'))

    def setUp(self):
        self.mock_ssh = self.add_mock('vmupdate.channel.SSHClient', new_callable=get_mock_ssh_client)
        self.mock_get_virtualizer = self.add_mock('vmupdate.host.get_virtualizer', autospec=True)
        self.mock_isfile = self.add_mock('os.path.isfile', autospec=True)
        self.mock_system = self.add_mock('platform.system', autospec=True)
        self.mock_sleep = self.add_mock('time.sleep', autospec=True)

    def test_update_all_vms(self):
        self.mock_system.return_value = TEST_OS
        self.mock_isfile.return_value = True
        self.mock_get_virtualizer.return_value = get_mock_virtualizer()

        exitcode = update_all_vms()

        self.assertEqual(exitcode, 0)

        self.mock_ssh.return_value.exec_command.assert_any_call('sudo -S testpkgmgr update')
        self.mock_ssh.return_value.exec_command.assert_any_call('sudo -S testpkgmgr upgrade')
        self.mock_ssh.return_value.exec_command.assert_any_call('testpkgmgr update')
        self.mock_ssh.return_value.exec_command.assert_any_call('testpkgmgr upgrade')

    def test_update_all_vms_start(self):
        self.mock_system.return_value = TEST_OS
        self.mock_isfile.return_value = True
        self.mock_get_virtualizer.return_value = get_mock_virtualizer()
        self.mock_get_virtualizer.return_value.get_vm_status.return_value = VM_STOPPED

        exitcode = update_all_vms()

        self.assertEqual(exitcode, 0)

        self.mock_get_virtualizer.return_value.start_vm.assert_any_call(mock.ANY)
        self.mock_get_virtualizer.return_value.stop_vm.assert_any_call(mock.ANY)
