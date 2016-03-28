import unittest

import mock

from vmupdate.cli import main, parse_args, unhandled_exception_handler


class CliTestCase(unittest.TestCase):
    @mock.patch('vmupdate.cli.update_all_vms', autospec=True)
    @mock.patch('vmupdate.cli.parse_args', autospec=True)
    def test_main(self, mock_parse_args, mock_update_all_vms):
        mock_parse_args.return_value = parse_args([])

        mock_update_all_vms.return_value = 0

        main()

        mock_update_all_vms.assert_called_once_with()

    def test_unhandled_exception_handler(self):
        unhandled_exception_handler(None, None, None)
