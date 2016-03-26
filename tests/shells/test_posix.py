import unittest

import mock

from vmupdate.shells import get_shell
from vmupdate.shells.posix import Posix
from vmupdate.channel import Channel, ChannelCommand


class PosixTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_channel = mock.MagicMock(spec=Channel)

        self.mock_cmd = mock.MagicMock(spec=ChannelCommand)
        self.mock_cmd.wait.return_value = 0

        self.mock_channel.run.return_value = self.mock_cmd

    def test_get_shell(self):
        shell = get_shell('Posix', None)

        self.assertIs(type(shell), Posix)

    def test_command_exists(self):
        test_command = 'testcommand'

        shell = Posix(self.mock_channel)

        success = shell.command_exists(test_command)

        self.mock_channel.run.assert_called_once_with(['command', '-v', test_command])
        self.assertTrue(success)

    def test_run_as_elevated(self):
        test_pass = 'testpass'

        self.mock_cmd.stdin = mock.MagicMock()

        shell = Posix(self.mock_channel)

        shell.run_as_elevated('test command', test_pass)

        self.mock_channel.run.assert_called_once_with(['sudo', '-S', 'test', 'command'])
        self.mock_cmd.stdin.write.assert_has_calls([mock.call(test_pass), mock.call('\n')])
        self.mock_cmd.stdin.flush.assert_called_once_with()
