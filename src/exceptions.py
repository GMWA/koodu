class ModelNotFoundException(Exception):
    """Raise when a model file is not found."""

    pass


class ModelFileTypeException(Exception):
    """Raise when a model file is not json."""

    pass


class MissingModelException(Exception):
    """Raise when the model is missing"""

    pass


class MissingConfigsException(Exception):
    """Raise this when the config file missing"""

    pass


class TemplateNotFoundException(Exception):
    """Raise when a template file is not found."""

    pass


class NotFolderException(Exception):
    """Raise when a Path is not a folder."""

    pass


class BadArgumentsException(Exception):
    """Raise the passed arguments are incorect"""

    pass
