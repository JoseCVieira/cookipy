import subprocess

import pytest

from tests.helpers import Bake, case_id, matrix


@pytest.mark.build
@pytest.mark.parametrize("context", matrix(), ids=case_id)
def test_whenAnyParametersAreChosen_expectMakeBuildPasses(
    bake: Bake, context: dict[str, str]
) -> None:
    project = bake(**context)

    subprocess.run(
        ["git", "add", "."],
        cwd=project,
        capture_output=True,
        text=True,
        check=True,
    )

    result = subprocess.run(
        ["make", "build"],
        cwd=project,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
