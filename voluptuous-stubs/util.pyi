from voluptuous import validators
from voluptuous.error import Invalid, LiteralInvalid, TypeInvalid
from voluptuous.schema_builder import Schema, default_factory, raises, DefaultFactory
import typing

def Lower(v: str) -> str: ...
def Upper(v: str) -> str: ...
def Capitalize(v: str) -> str: ...
def Title(v: str) -> str: ...
def Strip(v: str) -> str: ...

class DefaultTo:
    default_value: DefaultFactory
    msg: str
    def __init__(self, default_value, msg: str | None = None) -> None: ...
    def __call__(self, v): ...

class SetTo:
    value: DefaultFactory
    def __init__(self, value) -> None: ...
    def __call__(self, v): ...

class Set:
    msg: str
    def __init__(self, msg: str | None = None) -> None: ...
    def __call__(self, v): ...

class Literal:
    lit: typing.Any
    def __init__(self, lit) -> None: ...
    def __call__(self, value, msg: str | None = None): ...

def u(x: str) -> str: ...
