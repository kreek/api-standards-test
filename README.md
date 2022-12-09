# Lighthouse API Standards

This is the repo for the Lighthouse API standards hosted at 
https://department-of-veterans-affairs.github.io/lighthouse-api-standards.
The standards are managed by [team Cassowary](https://lighthouseva.slack.com/archives/C02SHTY8VNW) 
but pull requests are welcome from any team.

## Quick start

The API standards site uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 
a Python based static site builder and can be installed with `pip` (ideally using a [virtual environment](https://docs.python.org/3/library/venv.html)):

### Setup

```sh
python3 -m venv .
source venv/bin/activate
pip install mkdocs-material
```

Site content goes in the docs directory as Markdown files. Navigation and plugins are configured in the `mkdocs.yml` file.
See the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) website for more details.

### Running the site locally

```sh
 mkdocs serve
```

After running the command above the site will be available at http://localhost:8000

### Publishing

The Github action defined in `.github/workflows/ci.yml` will build and publish the site automatically on all merges (pushes)
to the `main` branch.
