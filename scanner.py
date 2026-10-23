import sys
from pathlib import Path


def file_size(path):
    """Return the size of a file in bytes, or 0 if it can't be read."""
    try:
        return path.stat().st_size
    except OSError:
        return 0


def format_size(size):
    """Turn a number of bytes into a readable text like '1.5 GB'."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def largest_files(folder, limit=10):
    """Return the largest files inside a folder, biggest first."""
    files = [path for path in folder.rglob("*") if path.is_file()]
    files.sort(key=file_size, reverse=True)
    return files[:limit]


def folder_sizes(folder):
    """Return each subfolder with its total size, biggest first."""
    sizes = []
    for sub in folder.iterdir():
        if sub.is_dir():
            total = sum(file_size(f) for f in sub.rglob("*") if f.is_file())
            sizes.append((sub, total))
    sizes.sort(key=lambda item: item[1], reverse=True)
    return sizes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = Path(sys.argv[1])
    else:
        folder = Path.home() / "Downloads"

    if not folder.is_dir():
        print(f"Folder not found: {folder}")
        sys.exit(1)

    print(f"\nLargest folders in {folder}\n")
    for sub, size in folder_sizes(folder)[:10]:
        print(f"{format_size(size):>10}  {sub.name}")

    print(f"\nLargest files in {folder}\n")
    for file in largest_files(folder):
        print(f"{format_size(file_size(file)):>10}  {file}")