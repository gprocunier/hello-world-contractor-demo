#!/usr/bin/env python3
"""Validate the static hello-world demo without external dependencies."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.stylesheets: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._in_title = True
        if tag == "link":
            attr_map = {key: value for key, value in attrs}
            if attr_map.get("rel") == "stylesheet" and attr_map.get("href"):
                self.stylesheets.append(str(attr_map["href"]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        self.text_parts.append(text)
        if self._in_title:
            self.title_parts.append(text)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    require(INDEX.exists(), "index.html is missing")
    parser = SiteParser()
    html = INDEX.read_text(encoding="utf-8")
    parser.feed(html)

    title = " ".join(parser.title_parts)
    body = " ".join(parser.text_parts)

    require(title == "Hello World Contractor Demo", "unexpected page title")
    require("styles.css" in parser.stylesheets, "styles.css is not linked")
    require((ROOT / "styles.css").exists(), "styles.css is missing")
    require("Hello, contractor workflow." in body, "hero heading is missing")
    require("Antigravity documents the project" in body, "Antigravity workflow text is missing")
    require("Claude Code creates the GitHub Pages experience" in body, "Claude workflow text is missing")
    require("TODO" not in html and "PLACEHOLDER" not in html, "placeholder text remains")


if __name__ == "__main__":
    main()

