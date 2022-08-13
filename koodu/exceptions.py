class ModelNotFoundException(Exception):
    """Raise when a model file is not found."""
    pass


class ModelFileTypeException(Exception):
    """Raise when a model file is not json."""
    pass


class MissingModeException(Exception):
    """Raise when the model is missing"""
    pass


class TemplateNotFoundException(Exception):
    """Raise when a template file is not found."""
    pass