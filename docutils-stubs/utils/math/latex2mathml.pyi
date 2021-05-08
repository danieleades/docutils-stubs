# Stubs for docutils.utils.math.latex2mathml (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Dict, List, Optional, Text, Tuple, TypeVar, Union

from docutils import nodes

N_co = TypeVar("N_co", bound=nodes.Node, covariant=True)

over: Dict[str, Text]
Greek: Dict[str, Text]
letters: Dict[str, Text]
special: Dict[str, Text]
sumintprod: str
functions: List[str]
mathbb: Dict[str, Text]
mathscr: Dict[str, Text]
negatables: Dict[str, Text]

class math:
    nchildren: Optional[int] = ...
    children: Union[List[nodes.Node], nodes.Node] = ...
    inline: Optional[bool] = ...
    def __init__(self, children: Optional[Union[List[N_co], nodes.Node]] = ..., inline: Optional[bool] = ...) -> None: ...
    def full(self) -> bool: ...
    def append(self, child: nodes.Node) -> nodes.Node: ...
    def delete_child(self) -> nodes.Node: ...
    def close(self) -> nodes.Node: ...
    def xml(self) -> List[str]: ...
    def xml_start(self) -> List[str]: ...
    def xml_end(self) -> List[str]: ...
    def xml_body(self) -> List[str]: ...

class mrow(math):
    def xml_start(self) -> List[str]: ...

class mtable(math):
    def xml_start(self) -> List[str]: ...

class mtr(mrow): ...
class mtd(mrow): ...

class mx(math):
    nchildren: int = ...
    data: str = ...
    def __init__(self, data: str) -> None: ...
    def xml_body(self) -> List[str]: ...

class mo(mx):
    translation: Dict[str, str] = ...
    def xml_body(self) -> List[str]: ...

class mi(mx): ...
class mn(mx): ...

class msub(math):
    nchildren: int = ...

class msup(math):
    nchildren: int = ...

class msqrt(math):
    nchildren: int = ...

class mroot(math):
    nchildren: int = ...

class mfrac(math):
    nchildren: int = ...

class msubsup(math):
    nchildren: int = ...
    reversed: bool = ...
    def __init__(self, children: Optional[Union[List[N_co], nodes.Node]] = ..., reversed: bool = ...) -> None: ...
    def xml(self) -> List[str]: ...

class mfenced(math):
    translation: Dict[str, Text] = ...
    openpar: str = ...
    def __init__(self, par: str) -> None: ...
    def xml_start(self) -> List[str]: ...

class mspace(math):
    nchildren: int = ...

class mstyle(math):
    nchildren: Optional[int] = ...
    attrs: Any = ...
    def __init__(
        self, children: Optional[Union[List[N_co], nodes.Node]] = ..., nchildren: Optional[int] = ..., **kwargs: Any
    ) -> None: ...
    def xml_start(self) -> List[str]: ...

class mover(math):
    nchildren: int = ...
    reversed: bool = ...
    def __init__(self, children: Optional[Union[List[N_co], nodes.Node]] = ..., reversed: bool = ...) -> None: ...
    def xml(self) -> List[str]: ...

class munder(math):
    nchildren: int = ...

class munderover(math):
    nchildren: int = ...
    def __init__(self, children: Optional[Union[List[N_co], nodes.Node]] = ...) -> None: ...

class mtext(math):
    nchildren: int = ...
    text: str = ...
    def __init__(self, text: str) -> None: ...
    def xml_body(self) -> List[str]: ...

def parse_latex_math(string: str, inline: bool = ...) -> math: ...
def handle_keyword(name: str, node: math, string: str) -> Tuple[math, int]: ...
def tex2mathml(tex_math: str, inline: bool = ...) -> str: ...
