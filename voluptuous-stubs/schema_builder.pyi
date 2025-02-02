from collections.abc import Generator
import re
import typing

from voluptuous.error import Error

long = int
unicode = str
basestring = str
ifilter = filter

def iteritems(d): ...

PREVENT_EXTRA: typing.Literal[0]
ALLOW_EXTRA: typing.Literal[1]
REMOVE_EXTRA: typing.Literal[2]
primitive_types: tuple

class Undefined:
    def __nonzero__(self): ...

UNDEFINED: Undefined

DefaultFactory = typing.Union[Undefined, typing.Callable]

def Self() -> None: ...
def default_factory(value) -> DefaultFactory: ...
def raises(exc, msg: str | None = None, regex: re.Pattern | None = None) -> Generator[None, None, None]: ...
def Extra(_) -> None: ...
extra = Extra

class Schema:
    schema: dict
    required: bool
    extra: int
    def __init__(self, schema: dict, required: bool = False, extra: int=PREVENT_EXTRA) -> None: ...
    @classmethod
    def infer(cls, data, **kwargs): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __call__(self, data): ...
    def extend(self, schema: dict, required: bool | None = None, extra: int | None = PREVENT_EXTRA): ...

class Msg:
    schema: dict
    msg: str
    cls: typing.Type[Error]|None
    def __init__(self, schema: dict, msg: str, cls: typing.Type[Error] | None = None) -> None: ...
    def __call__(self, v): ...

class Object(dict):
    cls: object
    def __init__(self, schema, cls: object=UNDEFINED) -> None: ...

class VirtualPathComponent(str): ...

class Marker:
    schema: dict
    msg: str | None
    description: str | None
    def __init__(self, schema_: dict, msg: str | None = None, description: str | None = None) -> None: ...
    def __call__(self, v): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Optional(Marker):
    default: DefaultFactory
    def __init__(self, schema: dict, msg: str | None = None, default=UNDEFINED, description: str | None = None) -> None: ...

class Exclusive(Optional):
    group_of_exclusion: str
    def __init__(self, schema: dict, group_of_exclusion: str, msg: str | None = None, description: str | None = None) -> None: ...

class Inclusive(Optional):
    group_of_inclusion: str
    def __init__(self, schema: dict, group_of_inclusion: str, msg: str | None = None, description: str | None = None, default=UNDEFINED) -> None: ...

class Required(Marker):
    default: DefaultFactory
    def __init__(self, schema: dict, msg: str | None = None, default=UNDEFINED, description: str | None = None) -> None: ...

class Remove(Marker):
    def __call__(self, v: object): ...
    def __hash__(self): ...

def message(default: str | None = None, cls: typing.Type[Error] | None = ...): ...
def validate(*a, **kw): ...
