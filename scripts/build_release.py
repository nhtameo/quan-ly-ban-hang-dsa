from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RELEASE_DIR = ROOT_DIR / "release"
PACKAGE_DIR = RELEASE_DIR / "QuanLyBanHang_DSA"
ZIP_PATH = RELEASE_DIR / "QuanLyBanHang_DSA.zip"

EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", "release", "tmp"}
EXCLUDED_SUFFIXES = {".pyc"}


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT_DIR)
    for part in relative.parts:
        if part in EXCLUDED_DIRS:
            return True
    return path.suffix in EXCLUDED_SUFFIXES


def copy_project() -> None:
    if PACKAGE_DIR.exists():
        shutil.rmtree(PACKAGE_DIR)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)

    for path in ROOT_DIR.rglob("*"):
        if should_skip(path):
            continue
        relative = path.relative_to(ROOT_DIR)
        target = PACKAGE_DIR / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)


def zip_project() -> Path:
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in PACKAGE_DIR.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(RELEASE_DIR))
    return ZIP_PATH


def main() -> None:
    copy_project()
    zip_path = zip_project()
    print(zip_path)


if __name__ == "__main__":
    main()
