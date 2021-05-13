import argparse
import html
import pathlib
import shutil
from textwrap import dedent

import tomlkit


parser = argparse.ArgumentParser()
parser.add_argument("source", type=pathlib.Path)
parser.add_argument("destination", type=pathlib.Path)
args = parser.parse_args()
source = args.source
dest = args.destination


with open(source, encoding="utf8") as f:
    sites = tomlkit.parse(f.read())["sites"]


if dest.exists():
    shutil.rmtree(dest)
dest.mkdir()
dest.joinpath("f").mkdir()

for n, site in enumerate(sites):
    prev = sites[(n - 1) % len(sites)]
    next = sites[(n + 1) % len(sites)]
    dest.joinpath("f", site["id"]).mkdir()
    with open(dest.joinpath("f", site["id"], "index.html"), "x", encoding="utf8") as f:
        # if custom embed css is provided get it
        css = ""
        if "css" in site:
            css = f'<link rel="stylesheet" href="{site["css"]}">'

        f.write(
            dedent(
                f"""\
				<!doctype html>
				<title>Circle - {html.escape(site['id'])}</title>
				{css}
				<a id=all href=/ target=_parent>comfi.es Circle</a>
				<a id=prev href="{html.escape(prev['url'])}" target=_parent>Prev</a>
				<a id=next href="{html.escape(next['url'])}" target=_parent>Next</a>
				"""
            )
        )

with open(dest.joinpath("index.html"), "x", encoding="utf8") as f:
    sitelist = ""
    for n, site in enumerate(sites):
        sitelist += (
            f'<b>{site["id"]} <a href="{site["url"]}">&RightArrow;</a></b><br>\n'
        )

    f.write(
        dedent(
            f"""\
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<meta name="description" content="the /comfy/ webcircle, basically a bunch of frens all holding hand!">
				<link rel="shortcut icon" href="https://comfi.es/src/img/comfies.ico">
				<link rel="stylesheet" href="https://comfi.es/src/comfies.css">
				<title>/comfy/ webcircle</title>
			</head>
			<body>
				<section>
					<h1>the /comfy/ webcircle</h1>
					<p>basically a bunch of frens all holding hand!</p>
				</section>
				<section>
					<h1>frembs list</h1>
					{sitelist}
				</section>
				<section>
					<h1>how 2 join</h1>
					<p>instructions are available in the README.md on the github page linke below</p>
					<b>comfies/comfy <a href="https://github.com/comfies/circle">&RightArrow;</a></b>
				</section>
			</body>
			"""
        )
    )

with open(dest.joinpath("404.html"), "x", encoding="utf8") as f:
    f.write(
        dedent(
            f"""\
			<!doctype html>
			<title>Circle - {html.escape(site['id'])}</title>
			<h1><a id=all href=/ target=_parent>comfi.es Circle</a></h1>
			<p><code>404</code> Page not found.
			"""
        )
    )

with open(dest.joinpath("f", "404.html"), "x", encoding="utf8") as f:
    f.write(
        dedent(
            f"""\
			<!doctype html>
			<title>Circle - {html.escape(site['id'])}</title>
			<a id=all href=/ target=_parent>comfi.es Circle</a>
			"""
        )
    )
