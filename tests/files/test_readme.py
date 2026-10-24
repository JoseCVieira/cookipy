from tests.helpers import Bake


def test_whenTitleAndDescriptionAreSet_expectReadmeHeadingAndDescription(
    bake: Bake,
) -> None:
    project = bake(
        __title="Distinctive Project Title",
        __description="Distinctive project description for this test.",
    )

    content = (project / "README.md").read_text()

    assert "# Distinctive Project Title" in content
    assert "Distinctive project description for this test." in content
