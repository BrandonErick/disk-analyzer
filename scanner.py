from pathlib import Path


def largest_files(folder, limit=10):
    """Return the largest files inside a folder, biggest first."""
    files = []

    for path in folder.rglob("*"):
        if path.is_file():
            files.append(path)

    files.sort(key=lambda f: f.stat().st_size, reverse=True)
    return files[:limit]


if __name__ == "__main__":
    downloads = Path.home() / "Downloads"

    for file in largest_files(downloads):
        size_mb = file.stat().st_size / 1_000_000
        print(f"{size_mb:8.1f} MB  {file}")