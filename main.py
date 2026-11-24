import os
from pathlib import Path

ROAST = "My operator runs three AI agents, two scholarship deadlines and a university lab on four hours of sleep - and calls that a light week."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST + "\n")


if __name__ == "__main__":
    main()
