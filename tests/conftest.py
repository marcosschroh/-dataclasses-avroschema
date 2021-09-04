import dataclasses
import typing

import pytest

from dataclasses_avroschema import AvroModel, types


@pytest.fixture
def user_dataclass():
    @dataclasses.dataclass(repr=False)
    class User(AvroModel):
        name: str
        age: int
        has_pets: bool
        money: float
        encoded: bytes

        class Meta:
            schema_doc = False

    return User


@pytest.fixture
def user_dataclass_with_doc():
    @dataclasses.dataclass(repr=False)
    class User(AvroModel):
        name: str
        age: int
        has_pets: bool
        money: float
        encoded: bytes

    return User


@pytest.fixture
def user_dataclass_with_field_metadata():
    @dataclasses.dataclass(repr=False)
    class User(AvroModel):
        name: str = dataclasses.field(metadata={"classification": "test"})
        age: int = dataclasses.field(metadata={"classification": "test"})
        has_pets: bool = dataclasses.field(metadata={"classification": "test"})
        money: float = dataclasses.field(metadata={"classification": "test"})
        encoded: bytes = dataclasses.field(metadata={"classification": "test"})

        class Meta:
            schema_doc = False

    return User


@pytest.fixture
def user_v2_dataclass():
    @dataclasses.dataclass(repr=False)
    class UserV2(AvroModel):
        "A User V2"
        name: str
        age: int

    return UserV2


@pytest.fixture
def user_extra_avro_atributes_dataclass():
    @dataclasses.dataclass(repr=False)
    class UserAliasesNamespace(AvroModel):
        name: str
        age: int

        def extra_avro_attributes() -> typing.Dict[str, typing.Any]:
            return {
                "namespace": "test.com.ar/user/v1",
                "aliases": ["User", "My favorite User"],
            }

    return UserAliasesNamespace


@pytest.fixture
def user_advance_dataclass():
    @dataclasses.dataclass
    class UserAdvance(AvroModel):
        name: str
        age: int
        pets: typing.List[str]
        accounts: typing.Dict[str, int]
        has_car: bool = False
        favorite_colors: types.Enum = types.Enum(["BLUE", "YELLOW", "GREEN"])
        country: str = "Argentina"
        address: str = None
        md5: types.Fixed = types.Fixed(16)

        class Meta:
            schema_doc = False

    return UserAdvance


@pytest.fixture
def user_advance_with_defaults_dataclass():
    @dataclasses.dataclass
    class UserAdvance(AvroModel):
        name: str
        age: int
        pets: typing.List[str] = dataclasses.field(default_factory=lambda: ["dog", "cat"])
        accounts: typing.Dict[str, int] = dataclasses.field(default_factory=lambda: {"key": 1})
        has_car: bool = False
        favorite_colors: types.Enum = types.Enum(["BLUE", "YELLOW", "GREEN"], default="BLUE")
        country: str = "Argentina"
        address: str = None

        class Meta:
            schema_doc = False

    return UserAdvance
