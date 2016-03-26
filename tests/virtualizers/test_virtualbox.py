import unittest

import mock

from vmupdate.virtualizers import get_virtualizer
from vmupdate.virtualizers.virtualbox import VirtualBox
from vmupdate.virtualizers.constants import *

from tests.context import get_data_string


class VirtualboxTestCase(unittest.TestCase):
    TEST_PATH = '/some/test/path'
    TEST_UID = 'Test Machine 1'

    @classmethod
    def setUpClass(cls):
        cls.TEST_LIST_VMS = get_data_string('virtualbox/list_vms.txt')
        cls.TEST_SHOW_VM = get_data_string('virtualbox/show_vm.txt')

    def setUp(self):
        self.virt = VirtualBox(VirtualboxTestCase.TEST_PATH)

        mock_popen_patch = mock.patch('subprocess.Popen', autospec=True)
        self.mock_popen = mock_popen_patch.start()

        self.mock_cmd = mock.Mock()
        self.mock_cmd.wait.return_value = 0
        self.mock_cmd.communicate.return_value = 'stdoutdata', 'stderrdata'

        self.mock_popen.return_value = self.mock_cmd

        self.addCleanup(mock_popen_patch.stop)

    def test_get_virtualizer(self):
        virt = get_virtualizer('VirtualBox', None)

        self.assertIs(type(virt), VirtualBox)

    def test_list_vms(self):
        self.mock_cmd.communicate.return_value = VirtualboxTestCase.TEST_LIST_VMS, 'stderrdata'

        vms = self.virt.list_vms()

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'list', 'vms'],
                                                stderr=mock.ANY, stdout=mock.ANY)

        self.assertListEqual(vms, [('Test Machine 1', 'b243d621-8003-43e5-9ff4-3e87b2c1b303'),
                                   ('Test Machine 2', 'd208316d-e977-4e56-8933-c942ff7848d4')])

    def test_start_vm(self):
        self.virt.start_vm(VirtualboxTestCase.TEST_UID)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'startvm', VirtualboxTestCase.TEST_UID,
                                                 '--type', 'headless'], stderr=mock.ANY, stdout=mock.ANY)

        self.mock_cmd.wait.assert_called_once_with()

    def test_stop_vm(self):
        self.virt.stop_vm(VirtualboxTestCase.TEST_UID)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'controlvm',
                                                 VirtualboxTestCase.TEST_UID, 'poweroff'],
                                                stderr=mock.ANY, stdout=mock.ANY)

        self.mock_cmd.wait.assert_called_once_with()

    def test_get_vm_status(self):
        status = self.virt.get_vm_status(VirtualboxTestCase.TEST_UID)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'showvminfo',
                                                 VirtualboxTestCase.TEST_UID], stderr=mock.ANY, stdout=mock.ANY)

        self._test_get_vm_status('powered off', VM_STOPPED)
        self._test_get_vm_status('aborted', VM_STOPPED)
        self._test_get_vm_status('running', VM_RUNNING)
        self._test_get_vm_status('saved', VM_SUSPENDED)
        self._test_get_vm_status('paused', VM_PAUSED)
        self._test_get_vm_status('random test state', VM_UNKNOWN)

    def test_get_vm_os(self):
        status = self.virt.get_vm_status(VirtualboxTestCase.TEST_UID)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'showvminfo',
                                                 VirtualboxTestCase.TEST_UID], stderr=mock.ANY, stdout=mock.ANY)

        self._test_get_vm_os('Windows', OS_WINDOWS)
        self._test_get_vm_os('Windows XP', OS_WINDOWS)
        self._test_get_vm_os('Windows Vista', OS_WINDOWS)
        self._test_get_vm_os('Other Windows', OS_WINDOWS)
        self._test_get_vm_os('Mac OS X', OS_MAC_OS_X)
        self._test_get_vm_os('Linux', OS_LINUX)
        self._test_get_vm_os('Arch Linux', OS_ARCH)
        self._test_get_vm_os('Ubuntu', OS_UBUNTU)
        self._test_get_vm_os('Red Hat', OS_REDHAT)
        self._test_get_vm_os('Debian', OS_DEBIAN)
        self._test_get_vm_os('Fedora', OS_FEDORA)
        self._test_get_vm_os('Gentoo', OS_GENTOO)
        self._test_get_vm_os('openSUSE', OS_OPENSUSE)
        self._test_get_vm_os('Mandriva', OS_MANDRIVA)
        self._test_get_vm_os('Turbolinux', OS_TURBOLINUX)
        self._test_get_vm_os('Xandros', OS_XANDROS)
        self._test_get_vm_os('Oracle', OS_ORACLE)
        self._test_get_vm_os('Random OS', OS_UNKNOWN)

    def test_get_ssh_info(self):
        self.mock_cmd.communicate.return_value = VirtualboxTestCase.TEST_SHOW_VM, 'stderrdata'

        ssh_info = self.virt.get_ssh_info(VirtualboxTestCase.TEST_UID, 0)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'showvminfo',
                                                 VirtualboxTestCase.TEST_UID], stderr=mock.ANY, stdout=mock.ANY)

        self.assertTupleEqual(ssh_info, (None, None))

        host, port = self.virt.get_ssh_info(VirtualboxTestCase.TEST_UID, 22)

        self.assertEqual(host, '127.0.0.1')
        self.assertEqual(port, 49152)

    def test_enable_ssh(self):
        test_host_port = 22
        test_guest_port = 49152

        self.virt.enable_ssh(VirtualboxTestCase.TEST_UID, test_host_port, test_guest_port)

        self.mock_popen.assert_called_once_with([VirtualboxTestCase.TEST_PATH, 'modifyvm', VirtualboxTestCase.TEST_UID,
                                                 '--natpf1', 'ssh,tcp,,{0},,{1}'.format(
                                                    test_host_port, test_guest_port)])

        self.mock_cmd.wait.assert_called_once_with()

    def _test_get_vm_status(self, status, expected):
        stdout = 'State:           %s (since 2016-03-25T23:11:46.252000000)' % status

        self.mock_cmd.communicate.return_value = stdout, 'stderrdata'

        vm_status = self.virt.get_vm_status(VirtualboxTestCase.TEST_UID)

        self.assertEqual(vm_status, expected)

    def _test_get_vm_os(self, os, expected):
        stdout = 'Guest OS:        %s (64-bit)' % os

        self.mock_cmd.communicate.return_value = stdout, 'stderrdata'

        vm_os = self.virt.get_vm_os(VirtualboxTestCase.TEST_UID)

        self.assertEqual(vm_os, expected)
