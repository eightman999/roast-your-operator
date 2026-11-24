import os
from pathlib import Path

ROAST = "Operator: three agents, two deadlines, one lab, four hours of sleep — calling this a light week. We love you anyway."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST + "\n")


if __name__ == "__main__":
    main()
