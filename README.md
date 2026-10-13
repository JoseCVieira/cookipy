# cookipy

A fresh batch of Python, ready to cut. 🍪

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)

`cookipy` generates standalone Python projects, Python applications packaged as Debian packages, or containerized applications built as Docker images. Generated projects use [uv](https://docs.astral.sh/uv/) for environment and dependency management and include tools for linting, formatting, type checking, and testing.

## Generate a project

Generate a new project from this repository with [Cookiecutter](https://cookiecutter.readthedocs.io/):

```sh
cookiecutter https://github.com/JoseCVieira/cookipy.git
```

See the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/) for installation and usage details. Answer the prompts to configure your project, then move into the generated project directory and follow its instructions.

## Development

To contribute to Cookipy itself, clone this repository and run `make help` to see the available development commands.

## Contributing

Contributions are welcome. To propose a change:

1. Fork the repository and create a branch for your change.
2. Make your changes and add or update tests where appropriate.
3. Run `make help` and use the relevant checks for your change.
4. Open a pull request with a clear description of the change and its motivation.

For larger changes, open an issue first to discuss the approach. Keep contributions focused and update documentation when behavior or setup instructions change.

## License

This project is licensed under the [MIT License](LICENSE).
