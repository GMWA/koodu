from pathlib import Path


class File(object):
    """The File Classe is the representation of a file."""

    def __init__(
        self,
        name: str,
        root: Path = Path("./"),
        content: str = "",
        is_binary: bool = False,
    ) -> None:
        self.name = name
        self.root = root
        self.content = content
        self.is_binary = is_binary

    def write(self):
        if not self.is_binary:
            if not self.root.is_dir():  # if the parent is not directory
                self.root.mkdir(exist_ok=True, parents=True)  # create it
            with open(self.root / self.name, "w") as fp:
                fp.write(self.content)
        else:
            pass

    def to_dict(self):
        return {
            "name": self.name,
            "root": self.root,
            "content": self.content,
            "is_binary": self.is_binary,
        }
