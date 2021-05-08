# Stubs for docutils.writers.html4css1 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes
from docutils.writers import _html_base
from typing import Any, Dict, List, Tuple, Type

__docformat__: str

class Writer(_html_base.Writer):
    supported: Tuple[str, ...] = ...
    default_stylesheets: List[str] = ...
    default_stylesheet_dirs: List[str] = ...
    default_template: str = ...
    default_template_path: str = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    config_section: str = ...
    parts: Dict[Any, Any] = ...
    translator_class: Type["HTMLTranslator"] = ...
    def __init__(self) -> None: ...

class HTMLTranslator(_html_base.HTMLTranslator):
    doctype: str = ...
    content_type: str = ...
    content_type_mathml: str = ...
    special_characters: Dict[int, str] = ...
    attribution_formats: Dict[str, Tuple[str, str]] = ...
    def set_first_last(self, node: nodes.Node) -> None: ...
    def visit_address(self, node: nodes.Element) -> None: ...
    def visit_admonition(self, node: nodes.Element) -> None: ...
    def visit_author(self, node: nodes.Element) -> None: ...
    author_in_authors: bool = ...
    def depart_author(self, node: nodes.Element) -> None: ...
    def visit_authors(self, node: nodes.Element) -> None: ...
    def depart_authors(self, node: nodes.Element) -> None: ...
    def visit_colspec(self, node: nodes.Element) -> None: ...
    def depart_colspec(self, node: nodes.Element) -> None: ...
    def is_compactable(self, node: nodes.Node) -> bool: ...
    def visit_citation(self, node: nodes.Element) -> None: ...
    def depart_citation(self, node: nodes.Element) -> None: ...
    def visit_classifier(self, node: nodes.Element) -> None: ...
    def visit_definition(self, node: nodes.Element) -> None: ...
    def visit_definition_list(self, node: nodes.Element) -> None: ...
    def visit_description(self, node: nodes.Element) -> None: ...
    def depart_description(self, node: nodes.Element) -> None: ...
    in_docinfo: bool = ...
    def visit_docinfo(self, node: nodes.Element) -> None: ...
    docinfo: List[str] = ...
    body: List[str] = ...
    def depart_docinfo(self, node: nodes.Element) -> None: ...
    def visit_docinfo_item(self, node: nodes.Element, name: str, meta: bool = ...) -> None: ...
    def depart_docinfo_item(self) -> None: ...
    def visit_doctest_block(self, node: nodes.Element) -> None: ...
    def visit_entry(self, node: nodes.Element) -> None: ...
    compact_p: Any = ...
    compact_simple: bool = ...
    def visit_enumerated_list(self, node: nodes.Element) -> None: ...
    def depart_enumerated_list(self, node: nodes.Element) -> None: ...
    def visit_field(self, node: nodes.Element) -> None: ...
    def depart_field(self, node: nodes.Element) -> None: ...
    def visit_field_body(self, node: nodes.Element) -> None: ...
    def depart_field_body(self, node: nodes.Element) -> None: ...
    compact_field_list: bool = ...
    def visit_field_list(self, node: nodes.Element) -> None: ...
    def depart_field_list(self, node: nodes.Element) -> None: ...
    def visit_field_name(self, node: nodes.Element) -> None: ...
    def depart_field_name(self, node: nodes.Element) -> None: ...
    def visit_footnote(self, node: nodes.Element) -> None: ...
    def footnote_backrefs(self, node: nodes.Node) -> None: ...
    def depart_footnote(self, node: nodes.Element) -> None: ...
    def visit_footnote_reference(self, node: nodes.Element) -> None: ...
    def depart_footnote_reference(self, node: nodes.Element) -> None: ...
    def visit_generated(self, node: nodes.Element) -> None: ...
    object_image_types: Dict[str, str] = ...
    def visit_label(self, node: nodes.Element) -> None: ...
    def depart_label(self, node: nodes.Element) -> None: ...
    def visit_list_item(self, node: nodes.Element) -> None: ...
    def visit_literal(self, node: nodes.Element) -> None: ...
    def visit_literal_block(self, node: nodes.Element) -> None: ...
    def depart_literal_block(self, node: nodes.Element) -> None: ...
    def visit_option_group(self, node: nodes.Element) -> None: ...
    def depart_option_group(self, node: nodes.Element) -> None: ...
    def visit_option_list(self, node: nodes.Element) -> None: ...
    def depart_option_list(self, node: nodes.Element) -> None: ...
    def visit_option_list_item(self, node: nodes.Element) -> None: ...
    def depart_option_list_item(self, node: nodes.Element) -> None: ...
    def should_be_compact_paragraph(self, node: nodes.Node) -> bool: ...
    def visit_paragraph(self, node: nodes.Element) -> None: ...
    def depart_paragraph(self, node: nodes.Element) -> None: ...
    in_sidebar: bool = ...
    def visit_sidebar(self, node: nodes.Element) -> None: ...
    def visit_subscript(self, node: nodes.Element) -> None: ...
    def depart_subscript(self, node: nodes.Element) -> None: ...
    in_document_title: int = ...
    def visit_subtitle(self, node: nodes.Element) -> None: ...
    subtitle: List[str] = ...
    def depart_subtitle(self, node: nodes.Element) -> None: ...
    def visit_superscript(self, node: nodes.Element) -> None: ...
    def depart_superscript(self, node: nodes.Element) -> None: ...
    def visit_system_message(self, node: nodes.Element) -> None: ...
    def visit_table(self, node: nodes.Element) -> None: ...
    def depart_table(self, node: nodes.Element) -> None: ...
    def visit_tbody(self, node: nodes.Element) -> None: ...
    def depart_tbody(self, node: nodes.Element) -> None: ...
    def visit_thead(self, node: nodes.Element) -> None: ...
    def depart_thead(self, node: nodes.Element) -> None: ...

class SimpleListChecker(_html_base.SimpleListChecker):
    def visit_list_item(self, node: nodes.Element) -> None: ...
    def visit_definition_list(self, node: nodes.Element) -> None: ...  # type: ignore
    def visit_docinfo(self, node: nodes.Element) -> None: ...  # type: ignore
