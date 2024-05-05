import pytest

from pytemplate.entrypoints.cli.main import main


@pytest.fixture
def mock_inputs(monkeypatch):
    def _mock_inputs(inputs):
        input_generator = (i for i in inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    return _mock_inputs


def test_addition(mock_inputs, capsys):
    inputs = ["2", "3", "add"]
    expected = "5"
    mock_inputs(inputs)
    main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_subtraction(mock_inputs, capsys):
    inputs = ["5", "3", "subtract"]
    expected = "2"
    mock_inputs(inputs)
    main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_multiplication(mock_inputs, capsys):
    inputs = ["4", "2", "multiply"]
    expected = "8"
    mock_inputs(inputs)
    main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_division(mock_inputs, capsys):
    inputs = ["8", "4", "divide"]
    expected = "2"
    mock_inputs(inputs)
    main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_invalid_action(mock_inputs, capsys):
    inputs = ["8", "4", "invide_action_name"]
    expected = "Invalid action name"
    mock_inputs(inputs)
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
