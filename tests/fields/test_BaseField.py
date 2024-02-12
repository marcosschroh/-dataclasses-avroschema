import dataclasses
from datetime import datetime

from dataclasses_avroschema import AvroField, AvroModel, utils


def test_render():
    field = AvroField("engine_name", str)
    expected = {
        "name": "engine_name",
        "type": "string",
    }

    assert expected == field.render()
    assert field.get_metadata() == []


def test_render_with_default():
    field = AvroField(
        "breed_name",
        str,
        default="test",
    )
    expected = {
        "name": "breed_name",
        "type": "string",
        "default": "test",
    }

    assert expected == field.render()


def test_render_with_default_factory():
    field = AvroField(
        "breed_name",
        str,
        default_factory=lambda: "test",
        metadata={"encoding": "some_exotic_encoding", "doc": "Official Breed Name"},
    )
    expected = {
        "name": "breed_name",
        "type": "string",
        "default": "test",
        "encoding": "some_exotic_encoding",
        "doc": "Official Breed Name",
    }

    assert expected == field.render()


def test_render_with_metadata():
    metadata = {"encoding": "some_exotic_encoding", "doc": "Official Breed Name"}
    field = AvroField("first_name", str, metadata=metadata)
    expected = {
        "name": "first_name",
        "type": "string",
        "encoding": "some_exotic_encoding",
        "doc": "Official Breed Name",
    }

    assert field.get_metadata() == [
        ("encoding", "some_exotic_encoding"),
        ("doc", "Official Breed Name"),
    ]
    assert expected == field.render()


def test_exclude_default_from_schema():
    field = AvroField(
        "breed_name",
        str,
        default="test",
        metadata={"exclude_default": True},
    )
    field_with_default_factory = AvroField(
        "breed_name",
        str,
        default_factory=lambda: "test",
        metadata={"exclude_default": True},
    )
    expected = {
        "name": "breed_name",
        "type": "string",
    }

    assert expected == field.render() == field_with_default_factory.render()


def test_render_complex_types():
    @dataclasses.dataclass
    class Metadata(AvroModel):
        timestamp: datetime = dataclasses.field(
            default_factory=lambda: datetime(2023, 10, 21, 11, 11),
        )

    parent = AvroModel()
    parent._metadata = utils.SchemaMetadata.create(type)
    field = AvroField(
        "metadata",
        Metadata,
        metadata={"desc": "Some metadata"},
        default_factory=Metadata,
        parent=parent,
    )

    expected = {
        "desc": "Some metadata",
        "name": "metadata",
        "type": {
            "type": "record",
            "name": "Metadata",
            "fields": [
                {
                    "name": "timestamp",
                    "type": {"type": "long", "logicalType": "timestamp-millis"},
                    "default": 1697886660000,
                }
            ],
        },
        "default": {"timestamp": 1697886660000},
    }

    assert expected == dict(field.render())
