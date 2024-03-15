from typing import Dict

import pytest

from dataclasses_avroschema.types import JsonDict


@pytest.fixture
def schema() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "age", "type": "int"},
            {"name": "money_available", "type": "double"},
            {"name": "weight", "type": "int", "unit": "kg"},
            {"name": "name", "type": "string", "default": "marcos"},
            {"name": "pet_age", "type": "int", "default": 1},
            {"name": "height", "type": "float", "default": 10.10},
            {"name": "expirience", "type": "int", "unit": "years", "default": 10},
            {
                "name": "is_student",
                "type": "boolean",
                "default": True,
            },
            {"name": "encoded", "type": "bytes", "default": "Hi"},
        ],
        "doc": "An User",
        "namespace": "test",
        "aliases": ["schema", "test-schema"],
    }


@pytest.fixture
def schema_2() -> Dict:
    return {
        "type": "record",
        "name": "Address",
        "fields": [
            {"name": "street", "type": "string"},
            {"name": "street_number", "type": "long"},
        ],
        "doc": "An Address",
    }


@pytest.fixture
def schema_primitive_types_as_defined_types() -> Dict:
    return {
        "type": "record",
        "name": "Address",
        "fields": [
            {"name": "street", "type": {"type": "string"}},
            {"name": "name", "type": ["null", {"type": "string"}]},
            {"name": "weight", "type": {"type": "int", "unit": "kg"}},
            {"name": "pet_age", "type": {"type": "int"}, "default": 1},
            {
                "name": "expirience",
                "type": {"type": "int", "unit": "years"},
                "default": 10,
            },
        ],
    }


@pytest.fixture
def schema_with_nulls() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "weight", "type": "int"},
            {"name": "money_available", "type": "double"},
            {"name": "name", "type": ["null", "string"], "default": None},
            {"name": "age", "type": ["null", "int"], "default": None},
            {"name": "pet_age", "type": ["int", "null"], "default": 1},
            {"name": "height", "type": "float", "default": 10.10},
            {
                "name": "is_student",
                "type": "boolean",
                "default": True,
            },
            {"name": "encoded", "type": "bytes", "default": "Hi"},
        ],
    }


@pytest.fixture
def schema_with_unions() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": ["int", "string"]},
            {"name": "money_available", "type": ["double"]},
            {"name": "age", "type": ["int", "string"], "default": 10},
            {"name": "pet_age", "type": ["string", "boolean"], "default": "bond"},
            {"name": "height", "type": "float", "default": 10.10},
            {"name": "weight", "type": ["null", "float", "int"], "default": None},
            {
                "name": "is_student",
                "type": "boolean",
                "default": True,
            },
            {"name": "encoded", "type": "bytes", "default": "Hi"},
        ],
    }


@pytest.fixture
def schema_with_array_types() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "pets",
                "type": {"type": "array", "items": "string", "name": "pet"},
            },
            {
                "name": "total",
                "type": {"type": "array", "items": ["int", "float"], "name": "total"},
            },
            {
                "name": "cars",
                "type": {"type": "array", "items": "string", "name": "car"},
                "default": [],
            },
            {
                "name": "bank_accounts",
                "type": [
                    "null",
                    {"type": "array", "items": "string", "name": "bank_account"},
                ],
                "default": None,
            },
            {
                "name": "favourites_numbers",
                "type": {"type": "array", "items": "long", "name": "favourites_number"},
                "default": [7, 13],
            },
        ],
    }


@pytest.fixture
def schema_with_map_types() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "accounts_money",
                "type": {"type": "map", "values": "float", "name": "accounts_money"},
            },
            {
                "name": "cars",
                "type": {"type": "map", "values": ["string", "bytes"], "name": "car"},
            },
            {
                "name": "cars_brand_total",
                "type": {"type": "map", "values": "long", "name": "cars_brand_total"},
                "default": {},
            },
            {
                "name": "family_ages",
                "type": {"type": "map", "values": "long", "name": "family_age"},
                "default": {"father": 50},
            },
            {
                "name": "bank_accounts",
                "type": [
                    "null",
                    {"type": "map", "values": "string", "name": "bank_account"},
                ],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_with_fixed_types() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "md5",
                "type": {
                    "type": "fixed",
                    "name": "md5",
                    "size": 16,
                    "namespace": "md5",
                    "aliases": ["md5", "hash"],
                },
                "default": "u00ffffffffffffx",
            },
        ],
    }


@pytest.fixture
def schema_with_enum_types() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "favorite_color",
                "type": {
                    "type": "enum",
                    "name": "FavoriteColor",
                    "symbols": ["Blue", "Yellow", "Green"],
                    "doc": "A favorite color",
                    "namespace": "some.name.space",
                    "aliases": ["Color", "My favorite color"],
                },
            },
            {
                "name": "primaty_color",
                "type": "some.name.space.FavoriteColor",
            },
            {
                "name": "superheros",
                "type": {
                    "type": "enum",
                    "name": "Superheros",
                    "symbols": ["batman", "superman", "spiderman"],
                },
                "default": "batman",
            },
            {
                "name": "cars",
                "type": [
                    "null",
                    {
                        "type": "enum",
                        "name": "Cars",
                        "symbols": ["bmw", "ferrary", "duna"],
                    },
                ],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_with_enum_types_case_sensitivity() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "unit_multi_player",
                "type": {
                    "type": "enum",
                    "name": "unit_multi_player",
                    "symbols": ["q", "Q"],
                },
            }
        ],
    }


@pytest.fixture
def schema_with_enum_types_no_pascal_case() -> Dict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {
                "name": "favorite_color",
                "type": {
                    "type": "enum",
                    "name": "my_favorite_color",
                    "symbols": ["Blue", "Yellow", "Green"],
                    "doc": "A favorite color",
                    "namespace": "some.name.space",
                    "aliases": ["Color", "My favorite color"],
                },
            },
            {"name": "primaty_color", "type": "some.name.space.my_favorite_color"},
            {
                "name": "superheros",
                "type": {"type": "enum", "name": "super_heros", "symbols": ["batman", "superman", "spiderman"]},
                "default": "batman",
            },
            {
                "name": "my_cars",
                "type": ["null", {"type": "enum", "name": "cars", "symbols": ["bmw", "ferrary", "duna"]}],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_with_custom_inner_names() -> Dict:
    return {
        "type": "record",
        "name": "DeliveryBatch",
        "fields": [
            {"name": "receivers_payload", "type": {"type": "array", "items": "string", "name": "my_custom_name"}},
            {
                "name": "accounts",
                "type": {"type": "map", "values": "string", "name": "my_account"},
            },
            {
                "name": "md5",
                "type": {
                    "type": "fixed",
                    "name": "my_md5",
                    "size": 16,
                    "namespace": "md5",
                    "aliases": ["md5", "hash"],
                },
            },
            {"name": "friends", "type": {"type": "array", "items": "string", "name": "my_friend"}, "default": []},
            {
                "name": "teammates",
                "type": {"type": "map", "values": "string", "name": "my_teammate"},
                "default": {},
            },
            {
                "name": "a_fixed",
                "type": {
                    "type": "fixed",
                    "name": "my_fixed",
                    "size": 16,
                },
                "default": "u00ffffffffffffx",
            },
        ],
        "namespace": "app.delivery.email",
    }


@pytest.fixture
def schema_one_to_one_relationship() -> JsonDict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "long"},
            {
                "name": "address",
                "type": {
                    "type": "record",
                    "name": "Address",
                    "fields": [
                        {"name": "street", "type": "string"},
                        {"name": "street_number", "type": "long"},
                    ],
                    "doc": "An Address",
                },
            },
            {
                "name": "extra_address",
                "type": "Address",
            },
            {
                "name": "crazy_union",
                "type": ["string", "Address"],
            },
            {
                "name": "optional_address",
                "type": ["null", "Address"],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_one_to_many_array_relationship() -> JsonDict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "long"},
            {
                "name": "addresses",
                "type": {
                    "type": "array",
                    "items": {
                        "type": "record",
                        "name": "Address",
                        "fields": [
                            {"name": "street", "type": "string"},
                            {"name": "street_number", "type": "long"},
                        ],
                        "doc": "An Address",
                    },
                    "name": "address",
                },
            },
            {
                "name": "crazy_union",
                "type": [
                    "string",
                    {"type": "array", "items": "Address", "name": "optional_address"},
                ],
            },
            {
                "name": "optional_addresses",
                "type": [
                    "null",
                    {"type": "array", "items": "Address", "name": "optional_address"},
                ],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_one_to_many_map_relationship() -> JsonDict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "long"},
            {
                "name": "addresses",
                "type": {
                    "type": "map",
                    "values": {
                        "type": "record",
                        "name": "Address",
                        "fields": [
                            {"name": "street", "type": "string"},
                            {"name": "street_number", "type": "long"},
                        ],
                        "doc": "An Address",
                    },
                    "name": "address",
                },
            },
            {
                "name": "crazy_union",
                "type": [
                    "string",
                    {"type": "map", "values": "Address", "name": "optional_address"},
                ],
            },
            {
                "name": "optional_addresses",
                "type": [
                    "null",
                    {"type": "map", "values": "Address", "name": "optional_address"},
                ],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_one_to_self_relationship() -> JsonDict:
    return {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "long"},
            {"name": "friend", "type": ["null", "User"], "default": None},
            {
                "name": "relatives",
                "type": {"type": "array", "items": "User", "name": "relative"},
                "default": [],
            },
            {
                "name": "teammates",
                "type": {"type": "map", "values": "User", "name": "teammate"},
                "default": {},
            },
        ],
    }


@pytest.fixture
def schema_with_decimal_field() -> JsonDict:
    return {
        "type": "record",
        "name": "demo",
        "fields": [
            {
                "name": "foo",
                "type": {
                    "type": "bytes",
                    "logicalType": "decimal",
                    "precision": 10,
                    "scale": 3,
                },
            }
        ],
    }


@pytest.fixture
def schema_with_logical_types() -> JsonDict:
    return {
        "type": "record",
        "name": "LogicalTypes",
        "fields": [
            {"name": "birthday", "type": {"type": "int", "logicalType": "date"}},
            {
                "name": "birthday_time",
                "type": {"type": "int", "logicalType": "time-millis"},
            },
            {
                "name": "birthday_datetime",
                "type": {"type": "long", "logicalType": "timestamp-millis"},
            },
            {"name": "uuid_1", "type": {"type": "string", "logicalType": "uuid"}},
            {
                "name": "money",
                "type": {
                    "type": "bytes",
                    "logicalType": "decimal",
                    "precision": 3,
                    "scale": 2,
                },
            },
            {
                "name": "meeting_date",
                "type": ["null", {"type": "int", "logicalType": "date"}],
                "default": None,
            },
            {
                "name": "release_date",
                "type": {"type": "int", "logicalType": "date"},
                "default": 18181,
            },
            {
                "name": "meeting_time",
                "type": ["null", {"type": "int", "logicalType": "time-millis"}],
                "default": None,
            },
            {
                "name": "release_time",
                "type": {"type": "int", "logicalType": "time-millis"},
                "default": 64662000,
            },
            {
                "name": "release_time_micro",
                "type": {"type": "long", "logicalType": "time-micros"},
                "default": 64662000000,
            },
            {
                "name": "meeting_datetime",
                "type": ["null", {"type": "long", "logicalType": "timestamp-millis"}],
                "default": None,
            },
            {
                "name": "release_datetime",
                "type": {"type": "long", "logicalType": "timestamp-millis"},
                "default": 1570903062000,
            },
            {
                "name": "release_datetime_micro",
                "type": {"type": "long", "logicalType": "timestamp-micros"},
                "default": 1570903062000000,
            },
            {
                "name": "uuid_2",
                "type": ["null", {"type": "string", "logicalType": "uuid"}],
                "default": None,
            },
            {
                "name": "event_uuid",
                "type": {"type": "string", "logicalType": "uuid"},
                "default": "ad0677ab-bd1c-4383-9d45-e46c56bcc5c9",
            },
            {
                "name": "explicit_with_default",
                "type": {
                    "type": "bytes",
                    "logicalType": "decimal",
                    "precision": 3,
                    "scale": 2,
                },
                "default": "\\u013a",
            },
        ],
    }


@pytest.fixture
def schema_with_logical_types_field_order() -> JsonDict:
    """
    This schema has default values before required values, so the generated
    Meta class must contain the `field_order` option
    """
    return {
        "type": "record",
        "name": "LogicalTypes",
        "fields": [
            {"name": "uuid_1", "type": {"type": "string", "logicalType": "uuid"}},
            {
                "name": "meeting_date",
                "type": ["null", {"type": "int", "logicalType": "date"}],
                "default": None,
            },
            {
                "name": "release_date",
                "type": {"type": "int", "logicalType": "date"},
                "default": 18181,
            },
            {
                "name": "meeting_time",
                "type": ["null", {"type": "int", "logicalType": "time-millis"}],
                "default": None,
            },
            {
                "name": "release_time",
                "type": {"type": "int", "logicalType": "time-millis"},
                "default": 64662000,
            },
            {
                "name": "release_time_micro",
                "type": {"type": "long", "logicalType": "time-micros"},
                "default": 64662000000,
            },
            {
                "name": "meeting_datetime",
                "type": ["null", {"type": "long", "logicalType": "timestamp-millis"}],
                "default": None,
            },
            {"name": "birthday", "type": {"type": "int", "logicalType": "date"}},
            {
                "name": "birthday_time",
                "type": {"type": "int", "logicalType": "time-millis"},
            },
            {
                "name": "birthday_datetime",
                "type": {"type": "long", "logicalType": "timestamp-millis"},
            },
            {
                "name": "release_datetime",
                "type": {"type": "long", "logicalType": "timestamp-millis"},
                "default": 1570903062000,
            },
            {
                "name": "release_datetime_micro",
                "type": {"type": "long", "logicalType": "timestamp-micros"},
                "default": 1570903062000000,
            },
            {
                "name": "uuid_2",
                "type": ["null", {"type": "string", "logicalType": "uuid"}],
                "default": None,
            },
            {
                "name": "event_uuid",
                "type": {"type": "string", "logicalType": "uuid"},
                "default": "ad0677ab-bd1c-4383-9d45-e46c56bcc5c9",
            },
            {
                "name": "explicit_with_default",
                "type": {
                    "type": "bytes",
                    "logicalType": "decimal",
                    "precision": 3,
                    "scale": 2,
                },
                "default": "\\u013a",
            },
            {
                "name": "money",
                "type": {
                    "type": "bytes",
                    "logicalType": "decimal",
                    "precision": 3,
                    "scale": 2,
                },
            },
        ],
    }


@pytest.fixture
def schema_with_pydantic_fields() -> JsonDict:
    return {
        "type": "record",
        "name": "Infrastructure",
        "fields": [
            {"pydantic-class": "EmailStr", "name": "email", "type": "string"},
            {"pydantic-class": "PostgresDsn", "name": "postgres_dsn", "type": "string"},
            {
                "pydantic-class": "CockroachDsn",
                "name": "cockroach_dsn",
                "type": "string",
            },
            {"pydantic-class": "AmqpDsn", "name": "amqp_dsn", "type": "string"},
            {"pydantic-class": "RedisDsn", "name": "redis_dsn", "type": "string"},
            {"pydantic-class": "MongoDsn", "name": "mongo_dsn", "type": "string"},
            {"pydantic-class": "KafkaDsn", "name": "kafka_url", "type": "string"},
            {"pydantic-class": "PositiveInt", "name": "total_nodes", "type": "long"},
            {
                "name": "event_id",
                "type": {
                    "type": "string",
                    "logicalType": "uuid",
                    "pydantic-class": "UUID3",
                },
            },
            {
                "name": "landing_zone_nodes",
                "type": {
                    "type": "array",
                    "items": {"type": "long", "pydantic-class": "PositiveInt"},
                    "name": "landing_zone_node",
                },
            },
            {
                "name": "total_nodes_in_aws",
                "type": {"type": "long", "pydantic-class": "PositiveInt"},
                "default": 10,
            },
            {
                "name": "optional_kafka_url",
                "type": ["null", {"type": "string", "pydantic-class": "KafkaDsn"}],
                "default": None,
            },
        ],
    }


@pytest.fixture
def schema_with_pydantic_constrained_fields() -> JsonDict:
    return {
        "type": "record",
        "name": "ConstrainedValues",
        "fields": [
            {
                "pydantic-class": "conint(gt=10, lt=20)",
                "name": "constrained_int",
                "type": "int",
            },
        ],
    }


@pytest.fixture
def schema_with_pydantic_logical_fields() -> JsonDict:
    return {
        "type": "record",
        "name": "LogicalTypesPydantic",
        "fields": [
            {
                "name": "birthday",
                "type": {"type": "int", "logicalType": "date"},
                "default": 18181,
            },
            {
                "name": "meeting_time",
                "type": {"type": "int", "logicalType": "time-millis"},
                "default": 64662000,
            },
            {
                "name": "release_datetime",
                "type": {"type": "long", "logicalType": "timestamp-millis"},
                "default": 1570903062000,
            },
            {
                "name": "past_date",
                "type": {
                    "type": "int",
                    "logicalType": "date",
                    "pydantic-class": "PastDate",
                },
                "default": 18181,
            },
            {
                "name": "future_date",
                "type": {
                    "type": "int",
                    "logicalType": "date",
                    "pydantic-class": "FutureDate",
                },
                "default": 2932896,
            },
            {
                "name": "past_datetime",
                "type": {
                    "type": "long",
                    "logicalType": "timestamp-millis",
                    "pydantic-class": "PastDatetime",
                },
                "default": 1570903062000,
            },
            {
                "name": "future_datetime",
                "type": {
                    "type": "long",
                    "logicalType": "timestamp-millis",
                    "pydantic-class": "FutureDatetime",
                },
                "default": 253402300799000,
            },
            {
                "name": "aware_datetime",
                "type": {
                    "type": "long",
                    "logicalType": "timestamp-millis",
                    "pydantic-class": "AwareDatetime",
                },
                "default": 1570903062000,
            },
            {
                "name": "naive_datetime",
                "type": {
                    "type": "long",
                    "logicalType": "timestamp-millis",
                    "pydantic-class": "NaiveDatetime",
                },
                "default": 1570903062000,
            },
            {
                "name": "event_uuid",
                "type": {"type": "string", "logicalType": "uuid"},
                "default": "09f00184-7721-4266-a955-21048a5cc235",
            },
        ],
        "doc": "Some logical types",
    }


@pytest.fixture
def with_fields_with_metadata() -> JsonDict:
    return {
        "type": "record",
        "name": "Message",
        "fields": [
            {
                "name": "fieldwithdefault",
                "type": "string",
                "default": "some default value",
            },
            {
                "name": "someotherfield",
                "type": "long",
                "aliases": ["oldname"],
                "doc": "test",
            },
        ],
    }
