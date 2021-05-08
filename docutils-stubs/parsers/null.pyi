# Stubs for docutils.parsers.null (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Sequence, Tuple

from docutils import parsers
from docutils.nodes import document

class Parser(parsers.Parser):
    supported: Tuple[str, ...] = ...
    config_section: str = ...
    config_section_dependencies: Sequence[str] = ...
    def parse(self, inputstring: str, document: document) -> None: ...
