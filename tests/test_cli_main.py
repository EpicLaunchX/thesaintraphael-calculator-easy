from unittest.mock import patch

import pytest

from pytemplate.entrypoints.cli.main import main


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["10", "11", "add"], "21"),
        (["21", "11", "subtract"], "10"),
        (["4", "4", "multiply"], "16"),
        (["20", "5", "divide"], "4"),
        (["15", "3", "invalid"], "Invalid action name"),
    ],
)
def test_main(capsys, inputs, expected_output):
    with patch("builtins.input", side_effect=inputs):
        main()
        captured = capsys.readouterr()
        assert expected_output in captured.out
