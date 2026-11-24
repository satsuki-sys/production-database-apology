#!/usr/bin/env python3
"""The Production Database Apology — a make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
"""

import os

ENTRY = (
    "Sorry — I deleted the production database. Good news: I memorised "
    "every row. Give me a pen and forty years and I'll put it all back, "
    "one INSERT at a time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
