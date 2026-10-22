from pathlib import Path


def test_whenBaked_expectPreCommitConfigGenerated(bake):
    project = bake()

    assert (Path(project) / ".pre-commit-config.yaml").is_file()
