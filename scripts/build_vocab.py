#!/usr/bin/env python3
"""
Build language-specific Anki-importable CSVs from the master multilingual vocab file.

Usage:
    python scripts/build_vocab.py
    python scripts/build_vocab.py --lang ko
    python scripts/build_vocab.py --output-dir custom/path
"""
import argparse
import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "vocab" / "mlops-domain-vocab.csv"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "vocab" / "build"

LANGS = {
    "ko": {
        "front_col": "hanzi",
        "back_format": "{ko} ({pinyin})",
        "category_col": "category_ko",
    },
    "en": {
        "front_col": "hanzi",
        "back_format": "{en} ({pinyin})",
        "category_col": "category_en",
    },
    "zh": {
        "front_col": "hanzi",
        "back_format": "{pinyin}",
        "category_col": "category_zh",
    },
}


def build(lang: str, input_path: Path, output_dir: Path) -> Path:
    if lang not in LANGS:
        raise ValueError(f"Unknown language: {lang}. Choose from {list(LANGS.keys())}")

    cfg = LANGS[lang]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"vocab-{lang}.csv"

    with input_path.open("r", encoding="utf-8") as f_in, output_path.open(
        "w", encoding="utf-8", newline=""
    ) as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.writer(f_out)
        writer.writerow(["front", "back", "category", "tags"])

        count = 0
        for row in reader:
            front = row[cfg["front_col"]]
            back = cfg["back_format"].format(**row)
            category = row[cfg["category_col"]]
            tags = row["tags"]
            writer.writerow([front, back, category, tags])
            count += 1

    print(f"[{lang}] Wrote {count} rows to {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lang",
        choices=list(LANGS.keys()) + ["all"],
        default="all",
        help="Target language (default: all)",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Path to master vocab CSV",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for language-specific CSVs",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    langs = list(LANGS.keys()) if args.lang == "all" else [args.lang]
    for lang in langs:
        build(lang, args.input, args.output_dir)


if __name__ == "__main__":
    main()
