import dataclasses
import datetime
import decimal
import typing
import uuid

from dataclasses_avroschema import AvroModel, types


def test_fake_primitive_types(user_dataclass):
    assert isinstance(user_dataclass.fake(), user_dataclass)


def test_fake_complex_types(user_advance_dataclass):
    assert isinstance(user_advance_dataclass.fake(), user_advance_dataclass)


def test_fake_with_logical_types():
    @dataclasses.dataclass
    class LogicalTypes(AvroModel):
        birthday: datetime.date
        meeting_time: datetime.time
        meeting_time_micro: types.TimeMicro
        release_datetime: datetime.datetime
        release_datetime_micro: types.DateTimeMicro
        event_uuid: uuid.uuid4

    assert isinstance(LogicalTypes.fake(), LogicalTypes)


def test_fake_union():
    class Bus(AvroModel):
        engine_name: str

        class Meta:
            namespace = "types.bus_type"

    class Car(AvroModel):
        engine_name: str

        class Meta:
            namespace = "types.car_type"

    class UnionSchema(AvroModel):
        first_union: typing.Union[str, int]
        logical_union: typing.Union[datetime.datetime, datetime.date, uuid.uuid4]
        lake_trip: typing.Union[Bus, Car]
        river_trip: typing.Union[Bus, Car] = None
        mountain_trip: typing.Union[Bus, Car] = dataclasses.field(default_factory=lambda: {"engine_name": "honda"})

    assert isinstance(UnionSchema.fake(), UnionSchema)


def test_fake_one_to_one_relationship():
    """
    Test schema relationship one-to-one
    """

    class Address(AvroModel):
        street: str
        street_number: int

    class User(AvroModel):
        name: str
        age: int
        address: Address

    assert isinstance(User.fake(), User)


def test_fake_one_to_many_relationship():
    """
    Test schema relationship one-to-many
    """

    class Address(AvroModel):
        street: str
        street_number: int

    class User(AvroModel):
        name: str
        age: int
        addresses: typing.List[Address]

    assert isinstance(User.fake(), User)
    assert User.avro_schema()


def test_fake_one_to_many_map_relationship():
    """
    Test schema relationship one-to-many using a map
    """

    class Address(AvroModel):
        street: str
        street_number: int

    class User(AvroModel):
        name: str
        age: int
        addresses: typing.Dict[str, Address]

    assert isinstance(User.fake(), User)


def test_self_one_to_one_relationship():
    """
    Test self relationship one-to-one
    """

    class User(AvroModel):
        name: str
        age: int
        teamates: typing.Type["User"] = None

    assert isinstance(User.fake(), User)


def test_self_one_to_many_relationship():
    """
    Test self relationship one-to-many
    """

    class User(AvroModel):
        name: str
        age: int
        teamates: typing.List[typing.Type["User"]] = None

    assert isinstance(User.fake(), User)


def test_self_one_to_many_map_relationship():
    """
    Test self relationship one-to-many Map
    """

    class User(AvroModel):
        name: str
        age: int
        friends: typing.Dict[str, typing.Type["User"]]
        teamates: typing.Dict[str, typing.Type["User"]] = None

    assert isinstance(User.fake(), User)


def test_decimals():
    """
    Test Decimal logical types
    """

    class User(AvroModel):
        name: str
        age: int
        test_score_1: decimal.Decimal = decimal.Decimal("100.00")
        test_score_2: decimal.Decimal = types.Decimal(scale=5, precision=11)

    assert isinstance(User.fake(), User)


def test_int32():
    """
    Test Int32 type
    """

    class User(AvroModel):
        name: str
        age: int
        test_score_1: types.Int32 = 100
        test_score_2: types.Int32 = types.Int32(12)

    assert isinstance(User.fake(), User)


def test_float32():
    """
    Test Float32 type
    """

    class User(AvroModel):
        name: str
        age: int
        test_score_1: types.Float32 = 100.0
        test_score_2: types.Float32 = types.Float32(12.4)

    assert isinstance(User.fake(), User)
