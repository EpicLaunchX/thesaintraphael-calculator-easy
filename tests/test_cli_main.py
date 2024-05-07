from unittest import mock

from pytemplate.entrypoints.cli.main import main


class TestCalcFunctions:
    def test_add_action(self, capsys):
        with mock.patch("builtins.input", side_effect=["45", "35", "add"]):
            main()
            captured = capsys.readouterr()
            assert "80" in captured.out

    def test_subtract_action(self, capsys):
        with mock.patch("builtins.input", side_effect=["45", "35", "subtract"]):
            main()
            captured = capsys.readouterr()
            assert "10" in captured.out

    def test_multiply_action(self, capsys):
        with mock.patch("builtins.input", side_effect=["4", "5", "multiply"]):
            main()
            captured = capsys.readouterr()
            assert "20" in captured.out

    def test_divide_action(self, capsys):
        with mock.patch("builtins.input", side_effect=["20", "5", "divide"]):
            main()
            captured = capsys.readouterr()
            assert "4" in captured.out

    def test_invalid_action(self, capsys):
        with mock.patch("builtins.input", side_effect=["20", "5", "invalid"]):
            main()
            captured = capsys.readouterr()
            assert "Invalid action name" in captured.out
