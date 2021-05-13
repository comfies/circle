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
	raise FileExistsError("Destination already exists")
dest.mkdir()
dest.joinpath("f").mkdir()


for n, site in enumerate(sites):
	prev = sites[(n - 1) % len(sites)]
	next = sites[(n + 1) % len(sites)]
	dest.joinpath("f", site["id"]).mkdir()
	with open(dest.joinpath("f", site["id"], "index.html"), "x", encoding="utf8") as f:
		f.write(
			dedent(
				f"""\
				<!doctype html>
				<title>Circle - {html.escape(site['id'])}</title>
				<a id=all href=/ target=_parent>comfi.es Circle</a>
				<a id=prev href="{html.escape(prev['url'])}" target=_parent>Prev</a>
				<a id=next href="{html.escape(next['url'])}" target=_parent>Next</a>
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
