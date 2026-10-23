"""Fixtures for hook tests."""

from collections.abc import Callable
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

TEMPLATE = Path(__file__).parents[2]

Bake = Callable[..., Path]


@pytest.fixture
def bake(tmp_path: Path) -> Bake:
    """Generate the template into a temp dir and return the project path."""

    def _bake(**extra_context: str) -> Path:
        project = cookiecutter(
            str(TEMPLATE),
            no_input=True,
            default_config=True,  # ignore ~/.cookiecutterrc
            output_dir=str(tmp_path / "out"),
            extra_context=extra_context,
        )
        return Path(project)

    return _bake
