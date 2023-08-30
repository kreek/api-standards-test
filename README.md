# Lighthouse API Standards (test)

This is the repo for the Lighthouse API standards hosted at
[https://department-of-veterans-affairs.github.io/lighthouse-api-standards](https://department-of-veterans-affairs.github.io/lighthouse-api-standards).
The standards are managed by [team Cassowary](https://lighthouseva.slack.com/archives/C02SHTY8VNW)
but pull requests are welcome from any team.

## Quick start

The API standards site uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
a Python based static site builder, which has been extended with VA theme, and
can be installed with `pip` (ideally
using a [virtual environment](https://docs.python.org/3/library/venv.html)):

### Setup

```sh
python3 -m venv .
source venv/bin/activate
pip install -r requirements.txt
```

Site content goes in the docs directory as Markdown files. Navigation and plugins
are configured in the `mkdocs.yml` file.
See the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) website
for more details.

### Running the site locally

```sh
 mkdocs serve
```

<!-- markdown-link-check-disable -->
After running the command above the site will be available at [http://127.0.0.1:8000/lighthouse-api-standards](http://127.0.0.1:8000/lighthouse-api-standards)
<!-- markdown-link-check-enable -->

### Committing changes

This repo uses two pre-commit hooks:

1. [markdown-link-check](https://www.npmjs.com/package/markdown-link-check) is a
  Node package that checks all the links within the docs are valid.
1. [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) is a Node package that
  ensures that the markdown files are formatted correctly

To install them run:

```sh
npm install -g markdown-link-check
npm install -g markdownlint-cli
```

Before changes can be committed the pre-commit hook must pass. You can also run
it manually:

```sh
pre-commit run -a
```

### Publishing

The GitHub action defined in `.github/workflows/ci.yml` will build and publish the
site automatically on all merges (pushes) to the `main` branch.
