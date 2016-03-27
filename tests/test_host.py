import unittest

import mock

from vmupdate.config import config
from vmupdate.host import update_all_vms

from tests.constants import *
from tests.context import get_data_path
from tests.mocks import get_mock_virtualizer, get_mock_ssh_client


class HostTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config.load(get_data_path('testconfig.yaml'))

    @mock.patch('vmupdate.channel.SSHClient', new_callable=get_mock_ssh_client)
    @mock.patch('vmupdate.host.get_virtualizer', autospec=True)
    @mock.patch('os.path.isfile', autospec=True)
    @mock.patch('platform.system', autospec=True)
    def test_update_all_vms(self, mock_system, mock_isfile, mock_get_virtualizer, mock_ssh):
        mock_system.return_value = TEST_OS
        mock_isfile.return_value = True
        mock_get_virtualizer.return_value = get_mock_virtualizer()

        exitcode = update_all_vms()

        # TODO: add more asserts

        self.assertEqual(exitcode, 0)
