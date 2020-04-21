from typing import Any, Optional
from voluptuous import validators as validators
from voluptuous.error import Invalid as Invalid, LiteralInvalid as LiteralInvalid, TypeInvalid as TypeInvalid
from voluptuous.schema_builder import Schema as Schema, default_factory as default_factory, raises as raises

def Lower(v: Any): ...
def Upper(v: Any): ...
def Capitalize(v: Any): ...
def Title(v: Any): ...
def Strip(v: Any): ...

class DefaultTo:
    default_value: Any = ...
    msg: Any = ...
    def __init__(self, default_value: Any, msg: Optional[Any] = ...) -> None: ...
    def __call__(self, v: Any): ...

class SetTo:
    value: Any = ...
    def __init__(self, value: Any) -> None: ...
    def __call__(self, v: Any): ...

class Set:
    msg: Any = ...
    def __init__(self, msg: Optional[Any] = ...) -> None: ...
    def __call__(self, v: Any): ...

class Literal:
    lit: Any = ...
    def __init__(self, lit: Any) -> None: ...
    def __call__(self, value: Any, msg: Optional[Any] = ...): ...

def u(x: Any): ...