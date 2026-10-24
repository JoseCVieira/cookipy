from pathlib import Path

from tests.helpers import Bake

ARTIFACT = "wren-bakewell-cli"


def read_makefile(project: Path) -> str:
    return (project / "Makefile").read_text()


def test_whenArtifactIsSet_expectArtifactVariableRendered(bake: Bake) -> None:
    project = bake(artifact=ARTIFACT)

    assert f"ARTIFACT := {ARTIFACT}" in read_makefile(project).splitlines()


def test_whenArtifactIsSet_expectRunTargetUsesArtifactVariable(bake: Bake) -> None:
    project = bake(artifact=ARTIFACT)

    assert "\tuv run $(ARTIFACT) ${ARGS}" in read_makefile(project)
