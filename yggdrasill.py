import json
import argparse

from pathlib import Path
from rich.tree import Tree
from rich.console import Console


console = Console()


def distinct_file_color(file):

    with open("file_extensions.json", "r") as extension_file:
        file_extensions: dict = json.load(extension_file)

    for extension in file_extensions:
        if file.endswith(extension):
            return file_extensions.get(extension)
        else:
            return "[#FFFFFF]"


def generate_tree(directory: Path, tree: Tree):

    contents = sorted([p for p in directory.iterdir()])

    for path in contents:
        if path.is_dir():
            branch = tree.add(f"[#6D43A6]{path.name}[/]")
            generate_tree(path, branch)
        else:
            color = distinct_file_color(path.name)
            tree.add(f"{color}{path.name}[/]")


def main():
    parser = argparse.ArgumentParser(description="Generate a directory tree structure.")
    parser.add_argument(
        "directory", type=Path, help="The directory path to generate the tree for"
    )
    args = parser.parse_args()

    directory = args.directory
    if directory.is_dir():
        tree = Tree(f"[#ABE15B]{directory}[/]", guide_style="underline2")
        generate_tree(directory, tree)
        console.print(tree)
    else:
        console.print("[#FFC835]The provided path is not a valid directory.[/]")


if __name__ == "__main__":
    main()
