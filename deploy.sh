#!/usr/bin/env bash

# cloudflare already loads the pipenv environment so just need to run python
python -m builder sites.toml templates dist
