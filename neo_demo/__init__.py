"""neo-demo: a tiny text-utils library that exists to give the neo harness something real to build on."""

import re


def slugify(text: str) -> str:
    """Lowercase, strip punctuation, and join words with hyphens."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words)


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())
