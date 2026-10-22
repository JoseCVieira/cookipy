from tests.helpers import Bake

PYTHON_VERSION = "3.11"


def test_whenPythonIsSet_expectItIsTheOnlyLine(bake: Bake) -> None:
    project = bake(__python=PYTHON_VERSION)

    lines = (project / ".python-version").read_text().splitlines()

    assert lines == [PYTHON_VERSION]
