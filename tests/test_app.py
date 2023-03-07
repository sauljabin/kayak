from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from kayak import VERSION
from kayak.app import main


class TestApp(TestCase):
    def test_print_version(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(VERSION, result.output)

    def test_missing_server(self):
        runner = CliRunner()
        result = runner.invoke(main)
        self.assertEqual(result.exit_code, 1)
        self.assertIn("Missing argument 'SERVER'", result.output)

    def test_missing_pass(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--user", "user"])
        self.assertEqual(result.exit_code, 1)
        self.assertIn("Please provide an --user and --password", result.output)

    def test_missing_user(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--password", "password"])
        self.assertEqual(result.exit_code, 1)
        self.assertIn("Please provide an --user and --password", result.output)

    @patch("kayak.app.Tui")
    def test_run_tui(self, mock_class_tui):
        runner = CliRunner()
        runner.invoke(main, ["--user", "user", "--password", "password", "server"])
        mock_class_tui.assert_called_once_with("server", "user", "password")
        mock_class_tui.return_value.run.assert_called_once_with()
