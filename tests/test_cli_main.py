from unittest.mock import patch

from pytemplate.entrypoints.cli.main import main


def test_add_action(capsys):
    with patch("builtins.input", side_effect=["10", "20", "add"]):
        main()
        assert "30" == capsys.readouterr().out


def test_subtract_action(capsys):
    with patch("builtins.input", side_effect=["20", "10", "subtract"]):
        main()
        assert "10" == capsys.readouterr().out


def test_multiply_action(capsys):
    with patch("builtins.input", side_effect=["10", "2", "multiply"]):
        main()
        assert "20" == capsys.readouterr().out


def test_divide_action(capsys):
    with patch("builtins.input", side_effect=["10", "5", "divide"]):
        main()
        captured = capsys.readouterr()
        assert "2" in captured.out


def test_invalid_action(capsys):
    with patch("builtins.input", side_effect=["4", "5", "invalid"]):
        main()
        assert "Invalid action name" in capsys.readouterr().out
