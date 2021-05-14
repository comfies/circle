import argparse
import html
import pathlib
import shutil
from textwrap import dedent

import jinja2
import tomlkit

# Interface
parser = argparse.ArgumentParser()
parser.add_argument(
    "--clobber",
    action="store_true",
    help="if there is a pre-existing destination folder, overwrite",
)
parser.add_argument("source", type=pathlib.Path, help="location of a sites.toml file")
parser.add_argument("templates", type=pathlib.Path, help="directory containing templates")
parser.add_argument("destination", type=pathlib.Path, help="output directory")
args = parser.parse_args()
source = args.source
dest = args.destination


# Inputs
with open(source, encoding="utf8") as f:
    sites = tomlkit.parse(f.read())["sites"]


templates = jinja2.Environment(
    loader=jinja2.FileSystemLoader(args.templates),
    autoescape=jinja2.select_autoescape(),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
)


# Building
if dest.exists():
    if args.clobber:
        shutil.rmtree(dest)


def copy_function(src, dst, *, follow_symlinks=True):
    src = src.removeprefix(str(args.templates)).removeprefix("/")
    if src == "frame.html":
        return
    with open(dst, "w", encoding="utf8") as f:
        f.write(templates.get_template(src).render(sites=sites))


shutil.copytree(args.templates, args.destination, copy_function=copy_function)


for n, site in enumerate(sites):
    prev = sites[(n - 1) % len(sites)]
    next = sites[(n + 1) % len(sites)]
    dest.joinpath("f", site["id"]).mkdir(parents=True)
    with open(dest.joinpath("f", site["id"], "index.html"), "x", encoding="utf8") as f:
        f.write(templates.get_template("frame.html").render(site=site, prev=prev, next=next))
