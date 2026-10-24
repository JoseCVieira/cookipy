from tests.helpers import Bake


def test_whenProjectIsBaked_expectCiWorkflowRunsLintTestAndBuild(bake: Bake) -> None:
    project = bake()

    content = (project / ".github" / "workflows" / "ci.yml").read_text()

    assert "run: make lint" in content
    assert "run: make test" in content
    assert "run: make build" in content


def test_whenProjectIsBaked_expectSbomWorkflowKeepsGithubTokenExpression(
    bake: Bake,
) -> None:
    project = bake()

    content = (project / ".github" / "workflows" / "sbom.yml").read_text()

    assert "GH_TOKEN: ${{ github.token }}" in content
