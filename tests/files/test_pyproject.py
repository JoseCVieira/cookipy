import tomllib
from pathlib import Path
from typing import Any

import pytest

from tests.helpers import Bake, choices


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


@pytest.mark.parametrize(
    ("title", "description"),
    [
        ("Half-Baked", "Half-Baked"),
        ("  Extra   inner   spaces  ", "Extra inner spaces"),
        ("Ends with dot.", "Ends with dot"),
        ("Dot after space .", "Dot after space"),
    ],
)
def test_whenTitleIsSet_expectNormalizedDescription(
    bake: Bake, title: str, description: str
) -> None:
    data = load(bake(title=title))

    assert data["project"]["description"] == description


def test_whenVersionIsSet_expectProjectVersion(bake: Bake) -> None:
    data = load(bake(__version="7.7.7"))

    assert data["project"]["version"] == "7.7.7"


def test_whenAuthorIsSet_expectAuthorsEntry(bake: Bake) -> None:
    data = load(bake(__author="Wren Bakewell", __email="wren.bakewell@example.com"))

    assert data["project"]["authors"] == [
        {"name": "Wren Bakewell", "email": "wren.bakewell@example.com"}
    ]


@pytest.mark.parametrize("license_", choices()["license"])
def test_whenAnyLicenseIsChosen_expectLicenseFileReferenceResolves(
    bake: Bake, license_: str
) -> None:
    project = bake(license=license_)

    reference = load(project)["project"]["license"]

    assert reference == {"file": "LICENSE"}
    assert (project / reference["file"]).is_file()
