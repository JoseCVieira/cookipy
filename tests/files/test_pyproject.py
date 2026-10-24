import tomllib
from pathlib import Path
from typing import Any

import pytest

from tests.helpers import AUTHOR, EMAIL, Bake, choices


def load(project: Path) -> dict[str, Any]:
    return tomllib.loads((project / "pyproject.toml").read_text())


def test_whenArtifactIsSet_expectProjectName(bake: Bake) -> None:
    data = load(bake(artifact="my-cool-app"))

    assert data["project"]["name"] == "my-cool-app"


def test_whenArtifactHasHyphens_expectScriptPointsToUnderscoreModule(
    bake: Bake,
) -> None:
    data = load(bake(artifact="my-cool-app"))

    assert data["project"]["scripts"] == {"my-cool-app": "my_cool_app.cli:cli"}


def test_whenTitleIsSet_expectProjectDescription(bake: Bake) -> None:
    data = load(bake(__title="Distinctive Project Title"))

    assert data["project"]["description"] == "Distinctive Project Title"


def test_whenVersionIsSet_expectProjectVersion(bake: Bake) -> None:
    data = load(bake(__version="7.7.7"))

    assert data["project"]["version"] == "7.7.7"


def test_whenAuthorIsSet_expectAuthorsEntry(bake: Bake) -> None:
    data = load(bake(__author=AUTHOR, __email=EMAIL))

    assert data["project"]["authors"] == [{"name": AUTHOR, "email": EMAIL}]


@pytest.mark.parametrize("license", choices()["license"])
def test_whenLicenseIsSet_expectLicenseFileReferenceResolves(
    bake: Bake, license: str
) -> None:
    project = bake(license=license)

    reference = load(project)["project"]["license"]

    assert reference == {"file": "LICENSE"}
    assert (project / reference["file"]).is_file()
