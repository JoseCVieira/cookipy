from pathlib import Path

ARTIFACT = "wren-bakewell-cli"


def read_makefile(project) -> str:
    return (Path(project) / "Makefile").read_text()


def test_whenBaked_expectMakefileGenerated(bake):
    project = bake(artifact=ARTIFACT)

    assert (Path(project) / "Makefile").is_file()


def test_whenArtifactSet_expectArtifactVariableRendered(bake):
    project = bake(artifact=ARTIFACT)

    assert f"ARTIFACT := {ARTIFACT}" in read_makefile(project).splitlines()


def test_whenArtifactSet_expectRunTargetUsesArtifactVariable(bake):
    project = bake(artifact=ARTIFACT)

    assert "\tuv run $(ARTIFACT) ${ARGS}" in read_makefile(project)
