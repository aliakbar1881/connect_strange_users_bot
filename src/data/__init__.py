from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
WELLCOME = DATA_DIR / "welcome.txt"
__all__ = [
    "DATA_DIR",
    "WELLCOME"
]

if __name__ == "__main__":
    print(WELLCOME)

