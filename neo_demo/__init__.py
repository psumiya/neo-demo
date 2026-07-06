"""neo-demo: a tiny text-utils library that exists to give the neo harness something real to build on."""

import re


def slugify(text: str) -> str:
    """Lowercase, strip punctuation, and join words with hyphens."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words)


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def truncate(text: str, max_len: int) -> str:
    """Return text shortened to max_len chars, ending with … if cut; raises ValueError for max_len < 1."""
    if max_len < 1:
        raise ValueError(f"max_len must be >= 1, got {max_len}")
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"
