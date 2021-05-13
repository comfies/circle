import argparse
import html
import pathlib
import shutil

import tomlkit


parser = argparse.ArgumentParser()
parser.add_argument("source", type=pathlib.Path)
parser.add_argument("destination", type=pathlib.Path)
args = parser.parse_args()
source = args.source
dest = args.destination
frames = dest.joinpath("f")


with open(source, encoding="utf8") as f:
    sites = tomlkit.parse(f.read())["sites"]


if dest.exists():
    raise FileExistsError("Destination already exists")
dest.mkdir()
frames.mkdir()


for n, site in enumerate(sites):
    prev = sites[(n - 1) % len(sites)]
    next = sites[(n + 1) % len(sites)]
    with open(frames.joinpath(site["id"] + ".html"), "w", encoding="utf8") as f:
        f.write(f"<!doctype html>")
        f.write(f"<title>Circle - {html.escape(site['id'])}</title>")
        f.write(f"<a id=all href=/ target=_parent>comfi.es Circle</a>")
        f.write(f"<a id=prev href=\"{html.escape(prev['url'])}\" target=_parent>Prev</a>")
        f.write(f"<a id=next href=\"{html.escape(next['url'])}\" target=_parent>Next</a>")
