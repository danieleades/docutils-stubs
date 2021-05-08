# Stubs for docutils.parsers.rst.directives.parts (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, List, Optional, Tuple

from docutils.nodes import Node
from docutils.parsers.rst import Directive

__docformat__: str

class Contents(Directive):
    backlinks_values: Tuple[str, ...] = ...
    def backlinks(arg: str) -> Optional[str]: ...  # type: ignore
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    def run(self) -> List[Node]: ...

class Sectnum(Directive):
    option_spec: Dict[str, Callable[[str], Any]] = ...
    def run(self) -> List[Node]: ...

class Header(Directive):
    has_content: bool = ...
    def run(self) -> List[Node]: ...

class Footer(Directive):
    has_content: bool = ...
    def run(self) -> List[Node]: ...
