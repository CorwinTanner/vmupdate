import unittest

import mock

from vmupdate.channel import Channel


class ChannelTestCase(unittest.TestCase):
    TEST_HOST = 'testhost'
    TEST_PORT = 0
    TEST_USERNAME = 'testuser'
    TEST_PASSWORD = 'testpass'

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_connect(self, mock_ssh):
        channel = Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT)

        channel.connect(ChannelTestCase.TEST_USERNAME, ChannelTestCase.TEST_PASSWORD)

        mock_ssh.return_value.connect.assert_called_once_with(hostname=ChannelTestCase.TEST_HOST,
                                                              port=ChannelTestCase.TEST_PORT,
                                                              username=ChannelTestCase.TEST_USERNAME,
                                                              password=ChannelTestCase.TEST_PASSWORD)

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_close(self, mock_ssh):
        with Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT):
            pass

        mock_ssh.return_value.close.assert_called_once_with()

    @mock.patch('vmupdate.channel.SSHClient', autospec=True)
    def test_run(self, mock_ssh):
        mock_ssh.return_value.exec_command.return_value = 'testin', 'testout', 'testerr'

        channel = Channel(ChannelTestCase.TEST_HOST, ChannelTestCase.TEST_PORT)

        cmd = channel.run(['some', 'test', 'command'])

        mock_ssh.return_value.exec_command.assert_called_once_with('some test command')

        self.assertEqual(cmd.stdin, 'testin')
        self.assertEqual(cmd.stdout, 'testout')
        self.assertEqual(cmd.stderr, 'testerr')
