# Stubs for docutils.parsers.rst.roles (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils.nodes import Node, system_message
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from docutils.utils import Reporter
from types import ModuleType
from typing import Any, Callable, Dict, List, Tuple, Union

RoleFunction = Callable[[str, str, str, int, Inliner, Dict[str, Any], List[str]], Tuple[List[Node], List[system_message]]]

__docformat__: str
DEFAULT_INTERPRETED_ROLE: str

def role(role_name: str, language_module: ModuleType, lineno: int, reporter: Reporter) -> Tuple[RoleFunction, List[system_message]]: ...
def register_canonical_role(name: str, role_fn: RoleFunction) -> None: ...
def register_local_role(name: str, role_fn: RoleFunction) -> None: ...
def set_implicit_options(role_fn: RoleFunction) -> None: ...
def register_generic_role(canonical_name: str, node_class: Node) -> None: ...

class GenericRole:
    name: str = ...
    node_class: Node = ...
    def __init__(self, role_name: str, node_class: Node) -> None: ...
    def __call__(self, role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...

class CustomRole:
    name: str = ...
    base_role: Union[RoleFunction, roles.CustomRole] = ...
    options: Dict[str, Any] = ...
    content: List[str] = ...
    supplied_options: Dict[str, Any] = ...
    supplied_content: List[str] = ...
    def __init__(self, role_name: str, base_role: Union[RoleFunction, roles.CustomRole], options: Dict[str, Any] = ..., content: List[str] = ...) -> None: ...
    def __call__(self, role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...

def generic_custom_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def pep_reference_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def rfc_reference_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def raw_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def code_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def math_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: Dict[str, Any] = ..., content: List[str] = ...) -> Tuple[List[Node], List[system_message]]: ...
def unimplemented_role(role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, attributes: Dict[str, Any] = ...) -> Tuple[List[Node], List[system_message]]: ...
def set_classes(options: Dict[str, str]) -> None: ...