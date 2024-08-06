from _typeshed import Incomplete
from collections.abc import Iterator, Mapping, Sequence
from typing import ClassVar, Protocol
from typing_extensions import TypeAlias, deprecated

from jsonschema import _typing
from jsonschema._format import FormatChecker
from jsonschema._types import TypeChecker
from jsonschema.exceptions import ValidationError
from jsonschema.validators import RefResolver
import referencing

_JsonParameter: TypeAlias = str | int | float | bool | None | Mapping[str, _JsonParameter] | Sequence[_JsonParameter]

class Validator(Protocol):
    META_SCHEMA: ClassVar[Mapping[Incomplete, Incomplete]]
    VALIDATORS: ClassVar[Mapping[Incomplete, Incomplete]]
    TYPE_CHECKER: ClassVar[TypeChecker]
    FORMAT_CHECKER: ClassVar[FormatChecker]
    ID_OF: _typing.id_of
    schema: Mapping[Incomplete, Incomplete] | bool
    def __init__(
        self,
        schema: Mapping[Incomplete, Incomplete] | bool,
        registry: referencing.jsonschema.SchemaRegistry,
        @deprecated("'RefResolver' has been deprecated in favor of 'referencing'")
        resolver: RefResolver | None = None,
        format_checker: FormatChecker | None = None,
    ) -> None: ...
    @classmethod
    def check_schema(cls, schema: Mapping[Incomplete, Incomplete]) -> None: ...
    def is_type(self, instance: _JsonParameter, type: str) -> bool: ...
    def is_valid(self, instance: _JsonParameter) -> bool: ...
    def iter_errors(self, instance: _JsonParameter) -> Iterator[ValidationError]: ...
    def validate(self, instance: _JsonParameter) -> None: ...
    def evolve(self, **kwargs) -> Validator: ...
