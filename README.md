# tree-sitter-avro-avdl

Tree-sitter grammar and Python package for Avro AVDL.

## Attribution

This project is based on the grammar work from:

- https://github.com/victorhqc/tree-sitter-apache-avro

Credit for the original grammar design and implementation goes to Victor Quiroz.
This repository maintains a separately named distribution for PyPI as
`tree-sitter-avro-avdl`.

## PyPI package

The package is published as:

- `tree-sitter-avro-avdl`

## Release workflow

Publishing is handled by the tree-sitter reusable GitHub workflows in:

- `.github/workflows/publish.yml`

On a pushed git tag, it will:

1. create a GitHub release,
2. build Python wheels and source distribution,
3. publish to PyPI.

## Local development

Generate parser sources:

```bash
tree-sitter generate
```

Build the Python package:

```bash
python -m build
```
