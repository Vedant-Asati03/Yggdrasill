import argparse

from pathlib import Path
from rich.console import Console
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree


class DirectoryTreeApp(App):
    def __init__(self, directory: Path):
        self.directory = directory
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DirectoryTree(self.directory)


def main():
    parser = argparse.ArgumentParser(description="Generate a directory tree structure.")
    parser.add_argument(
        "directory", type=Path, help="The directory path to generate the tree for"
    )
    args = parser.parse_args()

    directory = args.directory

    app = DirectoryTreeApp(directory)

    if directory.is_dir():
        app.run()
    else:
        Console().print("[#FFC835]The provided path is not a valid directory.[/]")


if __name__ == "__main__":
    main()
