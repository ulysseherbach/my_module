"""
Example of Python module.

This is a template of Python project in the form a module that can be
distributed and imported.
"""
from importlib.metadata import version as _version
from my_module.my_functions import square

__all__ = [
    'square',
]

try:
    __version__ = _version('my_module')
except Exception:
    __version__ = 'unknown version'
