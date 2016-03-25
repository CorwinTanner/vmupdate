import unittest

import mock

from vmupdate.channel import Channel, ChannelCommand


class ChannelTestCase(unittest.TestCase):
    TEST_HOST = 'testhost'
    TEST_PORT = 0

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_connect(self, mock_ssh):
        test_user = 'testuser'
        test_pass = 'testpass'

        channel = Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT)

        channel.connect(test_user, test_pass)

        mock_ssh.return_value.connect.assert_called_once_with(ChannelTestCase.TEST_HOST,
                                                              port=ChannelTestCase.TEST_PORT,
                                                              username=test_user,
                                                              password=test_pass)

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_close(self, mock_ssh):
        with Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT):
            pass

        mock_ssh.return_value.close.assert_called_once_with()

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_run(self, mock_ssh):
        test_stdin = 'testin'
        test_stdout = 'testout'
        test_stderr = 'testerr'

        mock_ssh.return_value.exec_command.return_value = (test_stdin, test_stdout, test_stderr)

        channel = Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT)

        cmd = channel.run(['some', 'test', 'command'])

        mock_ssh.return_value.exec_command.assert_called_once_with('some test command')

        self.assertEqual(cmd.stdin, test_stdin)
        self.assertEqual(cmd.stdout, test_stdout)
        self.assertEqual(cmd.stderr, test_stderr)


class ChannelCommandTestCase(unittest.TestCase):
    def test_wait(self):
        test_exitcode = -1

        mock_stdin = mock.MagicMock()
        mock_stdout = mock.MagicMock()
        mock_stderr = mock.MagicMock()

        mock_stdout.channel.recv_exit_status.return_value = test_exitcode
        mock_stdout.__iter__ = mock.Mock(return_value=iter(['stdoutline1']))
        mock_stderr.__iter__ = mock.Mock(return_value=iter(['stderrline1']))

        cmd = ChannelCommand(mock_stdin, mock_stdout, mock_stderr)

        self.assertEqual(cmd.wait(), test_exitcode)

        mock_stdout.__iter__.assert_called_once_with()
        mock_stderr.__iter__.assert_called_once_with()
