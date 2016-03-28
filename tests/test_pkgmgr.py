import unittest

import mock

from vmupdate.config import config
from vmupdate.errors import UpdateError
from vmupdate.pkgmgr import get_pkgmgrs, run_pkgmgr
from vmupdate.vm import VM

from tests.constants import *
from tests.context import get_data_path
from tests.mocks import get_mock_virtualizer, get_mock_ssh_client


class PkgMgrTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config.load(get_data_path('testconfig.yaml'))

    def setUp(self):
        patch_ssh = mock.patch('vmupdate.channel.SSHClient', new_callable=get_mock_ssh_client)

        self.addCleanup(patch_ssh.stop)

        self.mock_ssh = patch_ssh.start()
        self.mock_virt = get_mock_virtualizer()

    def test_get_pkgmgrs(self):
        vm = VM(self.mock_virt, 'Test Machine 1')

        pkgmgrs = get_pkgmgrs(vm)

        self.assertEqual(pkgmgrs, [('testpkgmgr', ['update', 'upgrade'])])

    def test_run_pkgmgr(self):
        vm = VM(self.mock_virt, 'Test Machine 4')

        run_pkgmgr(vm, TEST_PKGMGR, config.pkgmgrs[TEST_OS][TEST_PKGMGR])

        self.mock_ssh.return_value.exec_command.assert_has_calls([mock.call('testpkgmgr update'),
                                                             mock.call('testpkgmgr upgrade')])

    def test_run_pkgmgr_as_elevated(self):
        vm = VM(self.mock_virt, 'Test Machine 1')

        run_pkgmgr(vm, TEST_PKGMGR, config.pkgmgrs[TEST_OS][TEST_PKGMGR])

        self.mock_ssh.return_value.exec_command.assert_has_calls([mock.call('sudo -S testpkgmgr update'),
                                                             mock.call('sudo -S testpkgmgr upgrade')])

    def test_run_pkgmgr_update_error(self):
        mock_stdout = self.mock_ssh.return_value.exec_command.return_value[1]

        mock_stdout.channel.recv_exit_status.return_value = -1

        vm = VM(self.mock_virt, 'Test Machine 4')

        self.assertRaises(UpdateError, run_pkgmgr, vm, TEST_PKGMGR, config.pkgmgrs[TEST_OS][TEST_PKGMGR])
